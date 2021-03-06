
#pragma once

/* PSDK/NDK Headers */
//#define WIN32_NO_STATUS
//#include <windef.h>
//#include <winbase.h>
#include <windows.h>

#include <ndk/ntndk.h>

DWORD WINAPI
BaseSetLastNTError(IN NTSTATUS Status);
PWCHAR WINAPI FilenameA2W(LPCSTR NameA, BOOL alloc);
DWORD WINAPI FilenameU2A_FitOrFail(LPSTR  DestA,
	INT destLen, PUNICODE_STRING SourceU);

#define UNIMPLEMENTED
#define REPARSE_DATA_BUFFER_HEADER_SIZE   FIELD_OFFSET(REPARSE_DATA_BUFFER, GenericReparseBuffer)
#define DPRINT1(...)
#define bIsFileApiAnsi AreFileApisANSI()

#define FIXME(...)
#define TRACE(...)

LCID WINAPI LocaleNameToLCID(LPCWSTR name, DWORD flags);


// logging stuff
void WINAPI kex_fatal(const char* msg);
void WINAPI key_warn(const char* msg);

#include "stdshit.h"
