#include "precomp.h"
#include "strsafe.h"

extern "C"
HRESULT WINAPI CShellItem_CreateInstance(
	IUnknown *pUnkOuter, REFIID riid, void **ppvObject)
{
	asm volatile("int3");
	return 0;
}
