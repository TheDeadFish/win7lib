#include "ntdll.h"

NTSTATUS NTAPI RtlAppendUnicodeStringToString_hook1(
  PUNICODE_STRING  Destination,
  PCUNICODE_STRING Source
) {
	RtlAppendUnicodeToString(Destination, L"\\SysWOW6X\\");
	
	PUNICODE_STRING defPath = &(NtCurrentPeb()->ProcessParameters->DllPath);
	RI(&defPath->Length,0) += RI(&Destination->Length,0);
	int len = defPath->Length + 2; defPath->MaximumLength = len;
	PWSTR src = defPath->Buffer;
	PWSTR dst = defPath->Buffer = BaseAllocHeap(len);

	while(1) { 
		WCHAR ch = *src; *dst++ = ch; 
		if(ch == ';') break; src++; }
	wcscpy(dst, Destination->Buffer);
	dst = PW(dst, Destination->Length);
	wcscpy(dst, src);
	
	return 0;
}

