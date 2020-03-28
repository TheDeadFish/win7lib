#include "rtl_vista.h"

/**********************************************************************
 *           RtlGetCurrentProcessorNumberEx [NTDLL.@]
 */
void WINAPI RtlGetCurrentProcessorNumberEx(PROCESSOR_NUMBER *processor)
{
    FIXME("(%p) :semi-stub\n", processor);
    processor->Group = 0;
    processor->Number = NtGetCurrentProcessorNumber();
    processor->Reserved = 0;
}



/******************************************************************************
 *  RtlGetNtVersionNumbers   (NTDLL.@)
 *
 * Get the version numbers of the run time library.
 *
 * PARAMS
 *  major [O] Destination for the Major version
 *  minor [O] Destination for the Minor version
 *  build [O] Destination for the Build version
 *
 * RETURNS
 *  Nothing.
 *
 * NOTES
 * Introduced in Windows XP (NT5.1)
 */
void WINAPI RtlGetNtVersionNumbers( LPDWORD major, LPDWORD minor, LPDWORD build )
{
    RTL_OSVERSIONINFOW x; RtlGetVersion(&x);
    RTL_OSVERSIONINFOW* current_version = &x;

    if (major) *major = current_version->dwMajorVersion;
    if (minor) *minor = current_version->dwMinorVersion;
    /* FIXME: Does anybody know the real formula? */
    if (build) *build = (0xF0000000 | current_version->dwBuildNumber);
}
