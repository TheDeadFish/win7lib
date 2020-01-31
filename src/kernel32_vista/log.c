#include "k32_vista.h"

void WINAPI kex_fatal(const char* msg)
{
	HMODULE hMod = LoadLibraryA("user32.dll");
	FARPROC proc = GetProcAddress(hMod, "MessageBoxA");
	(typeof(&MessageBoxA))proc(
		NULL, msg, "kernelEx error", MB_OK);
	RaiseException(EXCEPTION_BREAKPOINT, 0,0,0);
}
