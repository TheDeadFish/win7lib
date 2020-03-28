#include "k32_vista.h"

/***********************************************************************
 *              GetSystemTimePreciseAsFileTime  (KERNEL32.@)
 *
 *  Get the current time in utc format with greater accuracy.
 *
 *  PARAMS
 *   time [out] Destination for the current utc time
 *
 *  RETURNS
 *   Nothing.
 */
 
 
NTSYSAPI LONGLONG NTAPI RtlGetSystemTimePrecise();
 
void WINAPI GetSystemTimePreciseAsFileTime( FILETIME *time )
{
    LARGE_INTEGER t;

    t.QuadPart = RtlGetSystemTimePrecise();
    time->dwLowDateTime = t.u.LowPart;
    time->dwHighDateTime = t.u.HighPart;
}
