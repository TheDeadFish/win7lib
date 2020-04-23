#include "../k32_vista.h"
extern const char locale_table[];

#define ENUM_DELTA_NEXT() {  \
	int ch, dx = 0; asm("1: movzx (%3), %1;" \
	"inc %3; shl $7, %2; btr $7, %1; lea (%1,%2), %2; jb 1b" \
	: "+r"(val), "=r"(ch), "+r"(dx), "+r"(pos)); \
	if(!dx) break; val += dx; LDI_AND(len, pos, 15); }
	
#define ENUM_DELTA_LINK(x) \
	if(!(flags & LOCALE_ALLOW_NEUTRAL_NAMES)) { \
	int link; MOVZX(link, pos[-1]); if(link &= -16) \
		{ val &= 255; val |= (link<<6); x; }}

#define ENUM_DELTA_STR_TABLE_418(xxx, ...) ({ \
	const BYTE* pos = locale_table; int len, val = 0;  \
	if(xxx) { len = 21; goto L1; } else { pos += 21; } \
	for(;; pos += len) { ENUM_DELTA_NEXT(); L1: __VA_ARGS__; }})
	
static int isAlpha(int ch) { ch |= 0x20; 
	return ((ch >= 'a') && (ch <= 'z')); }
static int cmpi(int x, int y) { return 
	XOR(x, y)&&((x & ~0x20)|| !isAlpha(y)); }

static LPWSTR strcpyn_zxbw(LPWSTR dst, const char* src, int len) {
	const char* end = src+len; for(; src < end; src++) {
		*(int*)dst = *(BYTE*)src; dst++; } return dst; }
static int strcmpn_zxbw(LPCWSTR ws, LPCSTR s, int len) {
	for(int i = 0; i < len; i++) { 
		if(cmpi(ws[i], ((BYTE*)s)[i])) return 1; }
	return 0; }
		
		
static 
LCID LCIDmapDefault(LCID lcid)
{
	if(lcid == LOCALE_SYSTEM_DEFAULT)
		return GetSystemDefaultLCID();
	if((lcid & ~0xC00) == 0)
		return GetUserDefaultLCID();
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
	
	// lookup the name
	int nlen = lstrlenW(name);
	ENUM_DELTA_STR_TABLE_418(1, if(nlen == len) {
		if(!val) return GetSystemDefaultLCID();
		if(!strcmpn_zxbw(name, pos, len)){ 
			ENUM_DELTA_LINK(); return val; }});
	
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

WAS_LINK:
	ENUM_DELTA_STR_TABLE_418(0,
		if(val == lcid) { 
			ENUM_DELTA_LINK(lcid = val; goto WAS_LINK);
			if(count != 0) { if(count <= len) { 
					SetLastError(	ERROR_INSUFFICIENT_BUFFER); 
					return 0; }
				strcpyn_zxbw(lpName, pos, len); 
			} return len+1;
		}
	);
	
BAD_PARAM:
	SetLastError(ERROR_INVALID_PARAMETER); 
	return 0;
}
