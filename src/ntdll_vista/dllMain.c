#include <windows.h>
#include "modmap.c"

BOOL WINAPI
VirtualProtect(PVOID lpAddress, SIZE_T dwSize,
	DWORD flNewProtect, PDWORD lpflOldProtect)
{
	return !NtProtectVirtualMemory((HANDLE)0xFFFFFFFF, 
		&lpAddress, &dwSize, flNewProtect, lpflOldProtect);
}

VOID APIENTRY
RaiseException(DWORD dwExceptionCode,DWORD dwExceptionFlags,
	DWORD nNumberOfArguments, CONST ULONG_PTR *lpArguments)
{
	EXCEPTION_RECORD ExceptionRecord = {};
	ExceptionRecord.ExceptionCode = dwExceptionCode;
	ExceptionRecord.ExceptionFlags = dwExceptionFlags;
	RtlRaiseException(&ExceptionRecord);
}


static HANDLE loadDll(const UNICODE_STRING* str) {
	HANDLE hMod;
	if(LdrLoadDll(0, 0, (PUNICODE_STRING)str, &hMod)) {
		MessageBoxW(NULL, L"dll load error", 
			str->Buffer, MB_OK);
	}
	
	return hMod;
}



BOOL WINAPI DllMainCRTStartup(HANDLE hInst, ULONG ul_reason_for_call, LPVOID lpReserved)
{
	static const UNICODE_STRING k32ExName = {
		24, 24, L"krnl32ex.dll"};
	if(ul_reason_for_call == DLL_PROCESS_ATTACH) {
		modMap_init(hInst, loadDll(&k32ExName)); }
	return TRUE;
}
