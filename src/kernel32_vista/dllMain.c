#include "k32_vista.h"

BOOL WINAPI DllMainCRTStartup(HANDLE hInst, ULONG ul_reason_for_call, LPVOID lpReserved)
{
	return TRUE;
}

DWORD WINAPI
BaseSetLastNTError(IN NTSTATUS Status)
{
	DWORD dwErrCode;
	dwErrCode = RtlNtStatusToDosError(Status);
	SetLastError(dwErrCode);
	return dwErrCode;
}
