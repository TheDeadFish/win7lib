#include "k32_vista.h"
#include "stdshit.h"

NTSYSAPI NTSTATUS NTAPI
RtlDosPathNameToNtPathName_U_WithStatus(
	PWSTR DosFileName, PUNICODE_STRING NtFileName,
	PWSTR *FilePart, PRTL_RELATIVE_NAME_U RelativeName);

NTSTATUS WINAPI Win32Rename(HANDLE FileHandle, 
	PFILE_RENAME_INFORMATION pfri, DWORD size)
{
	UNICODE_STRING ntName;
	PFILE_RENAME_INFORMATION fileInfo;
	int fileInfoSz;
	IO_STATUS_BLOCK ioStatus;
	NTSTATUS status;

	// get NT filename
	if(size < sizeof(*pfri)) return STATUS_INFO_LENGTH_MISMATCH;
	status = RtlDosPathNameToNtPathName_U_WithStatus(pfri->FileName, &ntName, 0, 0);
	if(!NT_SUCCESS(status)) return status;
	
	// allocate FileInformation buffer
	fileInfoSz = ntName.Length + sizeof(FILE_RENAME_INFORMATION);
	if(!(fileInfo = BaseAllocHeap(fileInfoSz))) {
		status = STATUS_NO_MEMORY; goto ERR_CLEANUP; }
		
	// initialize FileInformation buffer
	fileInfo->ReplaceIfExists = pfri->ReplaceIfExists;
	fileInfo->RootDirectory = pfri->RootDirectory;
	fileInfo->FileNameLength = ntName.Length;
	memcpy(fileInfo->FileName, ntName.Buffer, ntName.Length);
	
	// call NtSetInformationFile
	status = NtSetInformationFile(FileHandle, &ioStatus,
		fileInfo, fileInfoSz, FileRenameInformation);

	// cleanup return
ERR_CLEANUP:
	BaseFreeHeap(fileInfo);
	BaseFreeHeap(ntName.Buffer);
	return status;
}

/***********************************************************************
*			 SetFileInformationByHandleEx (KERNEL32.@)
*/

BOOL 
WINAPI 
SetFileInformationByHandle( 
	HANDLE hFile, 
	FILE_INFO_BY_HANDLE_CLASS class, 
	LPVOID info, 
	DWORD size 
)
{
	NTSTATUS status;
	IO_STATUS_BLOCK IoStatusBlock;
	
	ULONG Length;
	FILE_INFORMATION_CLASS ficls;
	
	switch (class)
	{
	case FileBasicInfo: // 0
		ficls = FileBasicInformation;
		Length = sizeof(FILE_BASIC_INFO);
		break;
		
	case FileRenameInfo:
		status = Win32Rename(hFile, info, size);
		goto CHK_STATUS;

	case FileDispositionInfo: // 4
		ficls = FileDispositionInformation;
		Length = sizeof(FILE_DISPOSITION_INFO);
		break;
		
	case FileAllocationInfo: // 5
		ficls = FileAllocationInformation;
		Length = sizeof(FILE_ALLOCATION_INFO);
		break;
	
	case FileEndOfFileInfo: // 6
		ficls = FileEndOfFileInformation;
		Length = sizeof(FILE_END_OF_FILE_INFO);
		break;
		
	case FileIoPriorityHintInfo: // 12
		ficls = FileIoPriorityHintInformation;
		Length = sizeof(FILE_IO_PRIORITY_HINT_INFO);
		if(*(DWORD*)info >= 3) goto ERR_PARAM;
		break;
	
	default: ERR_PARAM: status = 
		STATUS_INVALID_PARAMETER; goto ERR_STATUS;
	}
		
	if(Length > size) { status = STATUS_INFO_LENGTH_MISMATCH; goto ERR_STATUS; }
	status = NtSetInformationFile(hFile, &IoStatusBlock, info, Length, ficls);
	CHK_STATUS: if(NT_SUCCESS(status)) return TRUE;
	ERR_STATUS: BaseSetLastNTError(status); return FALSE;
}
