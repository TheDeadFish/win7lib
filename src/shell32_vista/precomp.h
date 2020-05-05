#ifndef _PRECOMP_H__
#define _PRECOMP_H__

#include <windows.h>
#include <shlobj.h>
#include <shlwapi.h>
#include <ndk/ntndk.h>

#undef Shell_GetCachedImageIndex


#define ARRAY_SIZE(x) (sizeof(x) / sizeof(x[0]))
static inline bool bSetMem(void* mem, int i) {
	bool ret; asm("bts %2, %1" : "=ccc"(ret),
	"+m"(*(char*)mem) : "r"(i) : "memory"); return ret; }
static inline bool bTstMem(void* mem, int i) {
	bool ret; asm("bt %2, %1" : "=ccc"(ret) 
		: "m"(*(char*)mem), "r"(i)); return ret; }

extern "C"
HRESULT WINAPI StringCchCopyW(LPWSTR  pszDest,
	size_t  cchDest, LPCWSTR pszSrc);
extern "C"
HRESULT WINAPI StringCchCatW(LPWSTR  pszDest,
	size_t  cchDest, LPCWSTR pszSrc);
	
HICON WINAPI ImageList_GetIcon(
  HIMAGELIST himl, int i, UINT flags);

/*****************************************************************************
 * IParentAndItem interface
 */

#ifndef __IParentAndItem_INTERFACE_DEFINED__
#define __IParentAndItem_INTERFACE_DEFINED__
DEFINE_GUID(IID_IParentAndItem, 0xb3a4b685, 0xb685, 0x4805, 
	0x99,0xd9, 0x5d,0xea,0xd2,0x87,0x32,0x36);
MIDL_INTERFACE("b3a4b685-b685-4805-99d9-5dead2873236")
IParentAndItem : public IUnknown
{
    virtual HRESULT STDMETHODCALLTYPE SetParentAndItem(
        PCIDLIST_ABSOLUTE pidlParent,
        IShellFolder *psf,
        PCUITEMID_CHILD pidlChild) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetParentAndItem(
        PIDLIST_ABSOLUTE *ppidlParent,
        IShellFolder **ppsf,
        PITEMID_CHILD *ppidlChild) = 0;

};
#ifdef __CRT_UUID_DECL
__CRT_UUID_DECL(IParentAndItem, 0xb3a4b685, 0xb685, 0x4805, 0x99,0xd9, 0x5d,0xea,0xd2,0x87,0x32,0x36)
#endif
#endif

#endif /* _PRECOMP_H__ */
