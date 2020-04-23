#include "../k32_vista.h"
#include <stdio.h>
int 
WINAPI 
GetLocaleInfoW_(
  LCID   Locale,
  LCTYPE LCType,
  LPWSTR lpLCData,
  int    cchData
) {
	if(LCType == LOCALE_SNAME)
		return LCIDToLocaleName(Locale, lpLCData, cchData, 0);
	return GetLocaleInfoW(Locale, LCType, lpLCData, cchData);
}


int 
WINAPI 
GetLocaleInfoEx(
  LPCWSTR lpLocaleName,
  LCTYPE  LCType,
  LPWSTR  lpLCData,
  int     cchData
) {
  LCID Locale = LocaleNameToLCID(lpLocaleName, LOCALE_ALLOW_NEUTRAL_NAMES);
  if(LCType == LOCALE_SNAME)
		return LCIDToLocaleName(Locale, lpLCData, cchData, LOCALE_ALLOW_NEUTRAL_NAMES);
  return GetLocaleInfoW_(Locale, LCType, lpLCData, cchData);
}


int 
WINAPI 
GetNumberFormatEx(
  LPCWSTR          lpLocaleName,
  DWORD            dwFlags,
  LPCWSTR          lpValue,
  const NUMBERFMTW *lpFormat,
  LPWSTR           lpNumberStr,
  int              cchNumber
) {
  LCID Locale = LocaleNameToLCID(lpLocaleName, 0);
  return GetNumberFormatW(Locale, dwFlags, lpValue, 
    lpFormat, lpNumberStr, cchNumber);
}

BOOL 
WINAPI
IsValidLocaleName(LPCWSTR lpLocaleName)
{
  LCID lcid = LocaleNameToLCID(lpLocaleName, 
    LOCALE_ALLOW_NEUTRAL_NAMES);
  return IsValidLocale(lcid, LCID_INSTALLED);
}
