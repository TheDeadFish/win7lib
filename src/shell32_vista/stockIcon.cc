#include "precomp.h"

#define SIID_MAX_ICONS 140

const WCHAR g_szShellIcons[] = L"Software\\Microsoft\\"
	"Windows\\CurrentVersion\\Explorer\\Shell Icons";
const WCHAR* const g_szIconsMods[] = {L"shell32.dll"};
		
extern HIMAGELIST g_himlIcons;  
extern HIMAGELIST g_himlIconsSmall;
BYTE g_shellIconMask[(SIID_MAX_ICONS+7)/8];

extern "C"
int WINAPI SHGetIconOverlayIndexW(LPCTSTR, int);

const 
WORD g_wIconIndex[] = {
	134, // SIID_AUTOLIST
	140, // SIID_PRINTERNET
	172, // SIID_SERVERSHARE
	196, // SIID_PRINTERFAX
	199, // SIID_PRINTERFAXNET
	141, // SIID_PRINTERFILE
	133, // SIID_STACK
	294, // SIID_MEDIASVCD
	4,  // SIID_STUFFEDFOLDER !
	54,  // SIID_DRIVEUNKNOWN
	291, // SIID_DRIVEDVD
	222, // SIID_MEDIADVD
	297, // SIID_MEDIADVDRAM
	318, // SIID_MEDIADVDRW
	298, // SIID_MEDIADVDR
	304, // SIID_MEDIADVDROM
	292, // SIID_MEDIACDAUDIOPLUS
	296, // SIID_MEDIACDRW
	295, // SIID_MEDIACDR
	260, // SIID_MEDIACDBURN
	302, // SIID_MEDIABLANKCD
	294, // SIID_MEDIACDROM
	225, // SIID_AUDIOFILES !
	226, // SIID_AUDIOFILES !
	224, // SIID_VIDEOFILES !
	227, // SIID_MIXEDFILES !
	4,  // SIID_FOLDERBACK !!
	4,  // SIID_FOLDERFRONT !!
	-1,  // SIID_SHIELD
	-1,  // SIID_WARNING
	-1,  // SIID_INFO
	-1,  // SIID_ERROR
	194, // SIID_KEY
	271, // SIID_SOFTWARE
	242, // SIID_RENAME
	240, // SIID_DELETE
	41,  // SIID_MEDIAAUDIODVD !
	222, // SIID_MEDIAMOVIEDVD !
	294, // SIID_MEDIAENHANCEDCD !
	222, // SIID_MEDIAENHANCEDDVD !
	302, // SIID_MEDIAHDDVD !
	302, // SIID_MEDIABLURAY !
	294, // SIID_MEDIAVCD !
	298, // SIID_MEDIADVDPLUSR !
	318, // SIID_MEDIADVDPLUSRW !
	16,  // SIID_DESKTOPPC
	-1,  // SIID_MOBILEPC
	269, // SIID_USERS
	308, // SIID_MEDIASMARTMEDIA
	303, // SIID_MEDIACOMPACTFLASH
	310, // SIID_DEVICECELLPHONE
	309, // SIID_DEVICECAMERA
	317, // SIID_DEVICEVIDEOCAMERA
	299, // SIID_DEVICEAUDIOPLAYER
	-1,  // SIID_NETWORKCONNECT
	273, // SIID_INTERNET
	-1,  // SIID_ZIPFILE
	274, // SIID_SETTINGS (106)
	
	-1,  // (107)
	271, // (108) !
	237, // (109)
	236, // (110) !
	238, // (111)
	-1,  // (112)
	139, // (113)
	171, // (114)
	-1,  // (115)
	249, // (116)
	169, // (117)
	170, // (118)
	198, // (119)
	168, // (120)
	197, // (121)
	-1,  // (122)
	-1,  // (123)
	-1,  // (124)
	-1,  // (125)
	224, // (126)
	269, // (127) !
	-1,  // (128)
	-1,  // (129)
	-1,  // (120)
	-1,  // (131)
	
	302, // SIID_DRIVEHDDVD
	302, // SIID_DRIVEBD
	302, // SIID_MEDIAHDDVDROM
	302, // SIID_MEDIAHDDVDR
	302, // SIID_MEDIAHDDVDRAM
	302, // SIID_MEDIABDROM
	302, // SIID_MEDIABDR
	302, // SIID_MEDIABDRE
	
	-1,  // SIID_CLUSTEREDDRIVE
};

HRESULT WINAPI GetShellIconLocation(
	int siid, SHSTOCKICONINFO *psii)
{
	if(siid >= SIID_MAX_ICONS) 
		return E_INVALIDARG;
	
	if(!bTstMem(g_shellIconMask, siid)) {
		
		// lookup icon in registry
		WCHAR buff[12];
		DWORD cbData = sizeof(psii->szPath);
		if(!SHRegGetValueW(HKEY_LOCAL_MACHINE,
		g_szShellIcons, _itow(siid, buff, 10),
		SRRF_RT_REG_SZ,	0, psii->szPath, &cbData)){
			psii->iIcon = PathParseIconLocationW(psii->szPath);
		} else { bSetMem(g_shellIconMask, siid); goto L1; }
	
	} else {
	
		// lookup icon in table
		L1: int modIndex = 0; int iconIndex = siid;
		if(iconIndex < 49) { iconIndex++; }
		else { iconIndex -= 49;
		
		
			// 
			iconIndex = g_wIconIndex[iconIndex];
		}
		psii->iIcon = -iconIndex;
		
		// get icon module name
		UINT nLen = GetSystemDirectoryW(psii->szPath, MAX_PATH);
		if(((nLen-1) >= MAX_PATH-1)||(!PathAppendW(psii->szPath,
		g_szIconsMods[modIndex]))) return 0x8007006F;
	}
	
	// adjust icon index
    if (psii->iIcon == -1)
      psii->iIcon = 0;
    return 0;
}
	
extern "C"
HRESULT WINAPI SHGetStockIconInfo(
	SHSTOCKICONID siid, UINT uFlags,
	SHSTOCKICONINFO *psii
)
{
	// validate & initialize SHSTOCKICONINFO
	if((!psii)||(psii->cbSize != sizeof(*psii)))
		return E_INVALIDARG;
	psii->iSysImageIndex = -1; psii->iIcon = -1;
	psii->hIcon = 0; psii->szPath[0] = 0;
	if(uFlags & ~(SHGFI_SMALLICON | SHGFI_ICON | SHGFI_SHELLICONSIZE |
	SHGFI_SYSICONINDEX | SHGFI_LINKOVERLAY | SHGFI_SELECTED))
		return E_INVALIDARG;

	// lookup icon index
	HRESULT hRes = GetShellIconLocation(siid, psii);
	if((!SUCCEEDED(hRes))||!(uFlags & (SHGFI_ICON 
		| SHGFI_SYSICONINDEX))) return hRes;
	int iIcon = Shell_GetCachedImageIndex(psii->szPath, psii->iIcon, 0);
	if(iIcon < 0) return E_FAIL;
	if(uFlags & SHGFI_SYSICONINDEX) { psii->iSysImageIndex = iIcon; }
	if(uFlags & SHGFI_ICON) {
	
		// get link overlay index	
		int iOverlayIndex;
		if(uFlags & SHGFI_LINKOVERLAY) { iOverlayIndex = 
			SHGetIconOverlayIndexW(0, IDO_SHGIOI_LINK);
			if(iOverlayIndex < 0) goto L1;
		} else { L1: iOverlayIndex = 0; }
		
		// create the icon
		HIMAGELIST himl, himlSmall;
		if(!Shell_GetImageLists(&himl, &himlSmall)) return E_FAIL;
		BOOL bSM = uFlags & SHGFI_SMALLICON;
		UINT flags = INDEXTOOVERLAYMASK(iOverlayIndex);
		if (uFlags & SHGFI_SELECTED) flags |= ILD_BLEND50;		
		HICON hIcon = ImageList_GetIcon(bSM ? 
			himlSmall : himl, iIcon, flags);
		
		// resize the icon
		if (hIcon && !(uFlags & SHGFI_SHELLICONSIZE)) {
		int cx = GetSystemMetrics(bSM ? SM_CXSMICON : SM_CXICON);
		int cy = GetSystemMetrics(bSM ? SM_CYSMICON : SM_CYICON);
		hIcon = (HICON)CopyImage(hIcon, IMAGE_ICON, cx, cy, 
			LR_COPYRETURNORG | LR_COPYDELETEORG); }
		if(!(psii->hIcon = hIcon)) return E_FAIL;
	
	}
	return 0;	
}
