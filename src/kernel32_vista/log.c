#include "k32_vista.h"

void kex_fatal(const char* msg)
{
	MessageBoxA(NULL, msg, "kernelEx error", MB_OK);
	RaiseException(EXCEPTION_BREAKPOINT, 0,0,0);
}
