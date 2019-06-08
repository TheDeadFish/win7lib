#include "precomp.h"
#include "csidlmap.h"

extern "C"
HRESULT WINAPI CShellItem_CreateInstance(
	IUnknown *pUnkOuter, REFIID riid, void **ppvObject);

// 100% complete
extern "C"
HRESULT WINAPI SHCreateItemFromIDList(
	PCIDLIST_ABSOLUTE pidl, REFIID riid, void **ppv)
{
	*ppv = 0; IPersistIDList* ipidl;
	HRESULT hRes = CShellItem_CreateInstance(
		0, IID_IPersistIDList, (void**)&ipidl);
	if(SUCCEEDED(hRes)) { 
		hRes = ipidl->SetIDList(pidl);
		if(SUCCEEDED(hRes)) 
			hRes = ipidl->QueryInterface(riid, ppv);
		ipidl->Release();
	} 
	return hRes;
}

// 100% complete
extern "C"
HRESULT WINAPI SHCreateItemWithParent(
	PCIDLIST_ABSOLUTE pidlParent, IShellFolder *psfParent,
	PCUITEMID_CHILD pidl, REFIID riid, void **ppvItem)
{
	*ppvItem = 0; IParentAndItem* ipai;
	HRESULT hRes = CShellItem_CreateInstance(
		0, IID_IParentAndItem, (void**)&ipai);	
	if(SUCCEEDED(hRes)) { 
		hRes = ipai->SetParentAndItem(
			pidlParent, psfParent, pidl);
		if(SUCCEEDED(hRes))
			hRes = ipai->QueryInterface(riid, ppvItem);
		ipai->Release();
	}
	return hRes;
}

// internal functionality missing
extern "C"
HRESULT SHCreateItemFromParsingName(PCWSTR pszPath,
	IBindCtx *pbc, REFIID riid, void **ppv)
{
	*ppv = 0; PIDLIST_ABSOLUTE pidl; 
	HRESULT hRes = SHParseDisplayName(pszPath, pbc, &pidl, 0,0);
	if(SUCCEEDED(hRes)) {
		hRes = SHCreateItemFromIDList(pidl, riid, ppv);
		ILFree(pidl); }
	return hRes;
}

// 
HRESULT WINAPI SHGetFolderPathEx_(
	REFKNOWNFOLDERID rfid, DWORD dwFlags,
	HANDLE hToken, LPWSTR pszPath)
{
	// lookup the folder
	CSIDL_MAP* csidl = (CSIDL_MAP*)bsearch(
		&rfid, csidl_map, ARRAY_SIZE(csidl_map), 
		sizeof(*csidl_map), csidl_cmp);
	if(!csidl) return E_INVALIDARG;
	
	// map the flags
	DWORD fID = csidl->fID;
	if(dwFlags & KF_FLAG_CREATE) fID |= CSIDL_FLAG_CREATE;
	if(dwFlags & KF_FLAG_DONT_VERIFY) fID |= KF_FLAG_DONT_VERIFY;
	if(dwFlags & KF_FLAG_NO_ALIAS) fID |= CSIDL_FLAG_NO_ALIAS;
	
	// execute SHGetFolderPath
	HRESULT hRes = SHGetFolderPath(0, fID, hToken, dwFlags & 
		KF_FLAG_DEFAULT_PATH ? SHGFP_TYPE_CURRENT : 0, pszPath);
	if(!SUCCEEDED(hRes) || !csidl->strIdx) return hRes;
	return StringCchCatW(pszPath, MAX_PATH, csidl_str[csidl->strIdx]);
}

extern "C"
HRESULT WINAPI SHGetFolderPathEx(
	REFKNOWNFOLDERID rfid, DWORD dwFlags,
	HANDLE hToken, LPWSTR pszPath, UINT cchPath)
{
	// get folder path	
	WCHAR buff[MAX_PATH];
	HRESULT hRes = SHGetFolderPathEx_(
		rfid, dwFlags, hToken, buff);
	if(!SUCCEEDED(hRes)) return hRes;
	return StringCchCopyW(pszPath, cchPath, buff);
}

extern "C"
HRESULT SHGetKnownFolderPath(
	REFKNOWNFOLDERID rfid, DWORD dwFlags,
	HANDLE hToken, PWSTR *ppszPath) 
{
	*ppszPath = 0; WCHAR buff[MAX_PATH];
	HRESULT hRes = SHGetFolderPathEx_(
		rfid, dwFlags, hToken, buff);
	if(!SUCCEEDED(hRes)) return hRes;
	return SHStrDupW(buff, ppszPath);
}
