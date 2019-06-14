#include <ntndk.h>

/*
NTSTATUS NTAPI RtlAppendUnicodeToString(
  PUNICODE_STRING Destination,
  PCWSTR          Source
); */

NTSTATUS NTAPI RtlAppendUnicodeToString_hook(
  PUNICODE_STRING Destination,
  PCWSTR          Source
) {
	
	return RtlAppendUnicodeToString(
		Destination, L"krnlex\\ntdll.dll");
}
