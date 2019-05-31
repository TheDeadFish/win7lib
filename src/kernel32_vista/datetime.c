#include "k32_vista.h"

int 
WINAPI 
GetTimeFormatEx(
  _In_opt_   LPCWSTR lpLocaleName,
  _In_       DWORD dwFlags,
  _In_opt_   const SYSTEMTIME *lpTime,
  _In_opt_   LPCWSTR lpFormat,
  _Out_opt_  LPWSTR lpTimeStr,
  _In_       int cchTime
)
{
	LCID locale = LocaleNameToLCID(lpLocaleName, 0);
	return GetTimeFormatW(locale,
						  dwFlags,
						  lpTime,
						  lpFormat,
						  lpTimeStr,
						  cchTime);
}

int 
WINAPI 
GetDateFormatEx(
  _In_opt_   LPCWSTR lpLocaleName,
  _In_       DWORD dwFlags,
  _In_opt_   const SYSTEMTIME *lpDate,
  _In_opt_   LPCWSTR lpFormat,
  _Out_opt_  LPWSTR lpDateStr,
  _In_       int cchDate,
  _In_opt_   LPCWSTR lpCalendar
)
{
	LCID locale = LocaleNameToLCID(lpLocaleName, 0);
	return GetDateFormatW(locale,
						  dwFlags,
						  lpDate,
						  lpFormat,
						  lpDateStr,
						  cchDate);	
}
