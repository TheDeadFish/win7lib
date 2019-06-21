#include <ntndk.h>
#include "stdshit.h"

/*
NTSTATUS NTAPI RtlAppendUnicodeToString(
  PUNICODE_STRING Destination,
  PCWSTR          Source
); */

static
BOOL IsNt6Process(void) 
{
	return NtCurrentPeb()->OSMajorVersion >= 6;
}

NTSTATUS NTAPI RtlAppendUnicodeToString_hook(
  PUNICODE_STRING Destination,
  PCWSTR          Source
) {
	if(IsNt6Process()) Source = L"\\krnlex\\ntdll.dll";
	return RtlAppendUnicodeToString(Destination, Source);
}

__attribute__ ((dllimport))
NTSTATUS NTAPI LdrGetKnownDllSectionHandle(void* a, void* b, void* c);
NTSTATUS NTAPI LdrGetKnownDllSectionHandle_hook(void* a, void* b, void* c)
{
	if(IsNt6Process()) return STATUS_UNSUCCESSFUL;
	return LdrGetKnownDllSectionHandle(a, b, c);
}
