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

