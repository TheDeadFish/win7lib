#include "k32_vista.h"
extern const char locale_table[];

#define lodsb(ptr, ax) ({ asm ("lodsb" :"+a"(ax), "=S"(ptr) : "S"(ptr)); })
#define lodsw(ptr, ax) ({ asm ("lodsw" :"+a"(ax), "=S"(ptr) : "S"(ptr)); })

#define ENUM_DELTA_STR_TABLE_418(_tab_, ...) ({ \
	const char* pos = _tab_; int val = 0;  \
	while(1) { int _ch_ = 0; lodsb(pos, _ch_); int len = _ch_; \
		if(((char)_ch_) == 0) break; if(((char)_ch_) < 0) { \
		if(_ch_ & 0x40) { lodsw(pos, _ch_); } else { lodsb(pos, _ch_); } \
		_ch_ <<= 6; _ch_ ^= len; } val += _ch_ >> 4;  \
		len &= 15; __VA_ARGS__; pos += len; }})
		

static LPWSTR strcpyn_zxbw(LPWSTR dst, const char* src, int len) {
	const char* end = src+len; for(; src < end; src++) {
		*dst = *(BYTE*)src; dst++; } *dst = 0; return dst; }
static int strcmpn_zxbw(LPCWSTR ws, LPCSTR s, int len) {
	for(int i = 0; i < len; i++) { int x = (ws[i] - 
		((BYTE*)s)[i]); if(x) return x; } return 0; }
		
		
static 
LCID LCIDmapDefault(LCID lcid)
{
	if(lcid == LOCALE_SYSTEM_DEFAULT)
		return GetSystemDefaultLCID();
	if(lcid == LOCALE_USER_DEFAULT)
		return GetSystemDefaultLCID();
	return lcid;
}

/***********************************************************************
 *           LocaleNameToLCID  (KERNEL32.@)
 */
LCID WINAPI LocaleNameToLCID( 
	LPCWSTR name, DWORD flags)
{
	if(name == NULL)
		return GetUserDefaultLCID();
	if(!lstrcmpW(name, L"!sys-default-locale"))
		return GetSystemDefaultLCID();
	
	// lookup the name
	int nlen = lstrlenW(name);
	ENUM_DELTA_STR_TABLE_418(locale_table, if((nlen == len) 
		&& (!strcmpn_zxbw(name, pos, len))) { return val; });
	
BAD_PARAM:
	SetLastError(ERROR_INVALID_PARAMETER); 
	return 0;
	
}


/***********************************************************************
 *           LCIDToLocaleName  (KERNEL32.@)
 */
INT WINAPI LCIDToLocaleName(LCID lcid, 
	LPWSTR lpName, INT count, DWORD flags)
{
	if (count < 0 || (count && !lpName)) 
		goto BAD_PARAM;
		
	lcid = LCIDmapDefault(lcid);
	ENUM_DELTA_STR_TABLE_418(locale_table,
		if(val == lcid) { if(count <= len) { 
			SetLastError(	ERROR_INSUFFICIENT_BUFFER); }
			else { strcpyn_zxbw(lpName, pos, len); } 
			return len+1; }
	);
	
BAD_PARAM:
	SetLastError(ERROR_INVALID_PARAMETER); 
	return 0;
}
