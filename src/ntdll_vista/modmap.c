#include "rtl_vista.h"
#include "stdshit.h"
#include "hotpatch.h"

#include <conio.h>

static PVOID getDllBase(PLIST_ENTRY Ent) {
	return CONTAINING_RECORD(Ent, LDR_DATA_TABLE_ENTRY, 
		InInitializationOrderLinks)->DllBase; }
static PLIST_ENTRY getDllHead() { return &NtCurrentPeb()
	->Ldr->InInitializationOrderModuleList; }
static PVOID getSysDll(PVOID* hk32) {
	PLIST_ENTRY ntdll = getDllHead()->Flink;
	*hk32 = getDllBase(ntdll->Flink);
	return getDllBase(ntdll); }

// module mapper
#define HMOD_MAX 16
typedef struct ModMap 
	{ PVOID from, to; } ModMap;
static ModMap modMap[HMOD_MAX];
static int nModMap;

static void* oldGetProcAddr;
static NTSTATUS WINAPI GetProcAddr (
		PVOID DllHandle, PANSI_STRING a,
		ULONG b, PVOID *c, BOOLEAN d) 
{
	NTSTATUS x = HOTCALL(GetProcAddr, 
		oldGetProcAddr)(DllHandle, a, b, c, d);
	if(x) { 
		int i = 0; 		
		do{ if(DllHandle == modMap[i].from) {
			x = HOTCALL(GetProcAddr, oldGetProcAddr)
				(modMap[i].to, a, b, c, d); break; }
		} while(++i < nModMap); }
			
	// display warning
	if(x) {
		printf("GetProcAddr: %X, %s\n", 
			DllHandle, a->Buffer); 
	}
	
	
	
	
	return x;
}

static 
void modMap_init(PVOID hNtEx, PVOID hK32Ex) 
{
	_cprintf("modMap_init 0\n");

	// get system modules
	nModMap = 2; 
	modMap[0].to = hNtEx; modMap[1].to = hK32Ex;
	modMap[0].from = getSysDll(&modMap[1].from);
	
	_cprintf("modMap_init 1\n");
	
	// hook LdrpGetProcedureAddress
	//HOTPATCH(hotPatch_getCall(
	//	IMPGET4(LdrGetProcedureAddress),0),
	//	GetProcAddr, &oldGetProcAddr);
}

