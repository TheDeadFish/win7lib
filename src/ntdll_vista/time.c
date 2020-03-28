#include "rtl_vista.h"

/***********************************************************************
 *       RtlGetSystemTimePrecise [NTDLL.@]
 *
 * Get a more accurate current system time.
 *
 * RETURNS
 *   The current system time.
 */
LONGLONG WINAPI RtlGetSystemTimePrecise( void )
{
    LONGLONG time;
    NtQuerySystemTime((PLARGE_INTEGER)&time);
    return time;
}
