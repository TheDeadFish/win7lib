#include "ntdll.h"

// its sad that its come to this
typedef struct { int data[4]; } m128;
static inline
void move16(void* dst, const void* src) {
	asm("movups %1, %%xmm0; movups %%xmm0, %0" : 
		"=m"(*((m128*)dst)) : "m"(*((m128*)src))); }
		

const WCHAR SysWOW6X[] = L"SysWOW6X";

BOOLEAN NTAPI
RtlDoesFileExists_UstrEx(
	PCUNICODE_STRING FileName,
	BOOLEAN SucceedIfBusy);
	
PWSTR NTAPI prefixCmp(PWSTR Name, PWSTR prefix)
{
	while(1) {
		int ch1 = *Name; int ch2 = *prefix;
		Name += 1; prefix += 1; if(!ch2) { 
			return isSep(ch1) ? Name : 0; }
		if(!cmpiW(ch1, ch2)) return 0;
	}
}

static
PWSTR isSystemDir(PCUNICODE_STRING FileName)
{
	// compare system root
	PWSTR tmp = prefixCmp(FileName->Buffer,
		SharedUserData->NtSystemRoot);
	if(!tmp) return 0;
	
	// compare system32
	PWSTR xx = prefixCmp(tmp, L"System32");
	if(!xx) xx = prefixCmp(tmp, L"SysWOW64");
	return xx;
}

BOOLEAN NTAPI
RtlDoesFileExists_UstrEx_redir(
	PCUNICODE_STRING FileName,
	BOOLEAN SucceedIfBusy
) {
	PWSTR tmp = isSystemDir(FileName);
	if(tmp) { move16(tmp-9, SysWOW6X);
		BOOLEAN ret = RtlDoesFileExists_UstrEx(FileName, 0);
		if(ret) return ret; tmp[-2] = '4'; }
	return RtlDoesFileExists_UstrEx(FileName, 0);
}

NTSTATUS NTAPI RtlAppendUnicodeStringToString_hook1(
  PUNICODE_STRING  Destination,
  PCUNICODE_STRING Source
) {
	RtlAppendUnicodeStringToString(Destination, Source);
	move16(PW(Destination->Buffer,Destination->Length-18), SysWOW6X);
	return 0;
}
