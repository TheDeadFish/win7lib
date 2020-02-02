#include "k32_vista.h"

/***********************************************************************
*             GetFileInformationByHandleEx (KERNEL32.@)
*/
BOOL 
WINAPI 
GetFileInformationByHandleEx( 
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
	int directoryMode = -1;

	switch (class)
	{
	case FileBasicInfo: // 0
		ficls = FileBasicInformation;
		Length = sizeof(FILE_BASIC_INFO);
		break;
		
	case FileStandardInfo: // 1
		ficls = FileStandardInformation;
		Length = sizeof(FILE_STANDARD_INFO);
		break;
		
	case FileNameInfo: // 2
		ficls = FileNameInformation;
		Length = sizeof(FILE_NAME_INFO);
		break;
		
	case FileStreamInfo: // 7
		ficls = FileStreamInformation;
		Length = sizeof(FILE_STREAM_INFORMATION);
		break;
		
	case FileCompressionInfo: // 8
		ficls = FileCompressionInformation;
		Length = sizeof(FILE_COMPRESSION_INFO);
		break;
		
	case FileAttributeTagInfo: // 9
		ficls = FileAttributeTagInformation;
		Length = sizeof(FILE_ATTRIBUTE_TAG_INFO);
		break;
		
	case FileIdBothDirectoryInfo: // a
		ficls = FileIdBothDirectoryInformation;
		Length = sizeof(FILE_ID_BOTH_DIR_INFO);
		directoryMode = 0;
		break;	
	
	case FileIdBothDirectoryRestartInfo: // b
		ficls = FileIdBothDirectoryInformation;
		Length = sizeof(FILE_ID_BOTH_DIR_INFO);
		directoryMode = 1;
		break;	
	
	case FileRemoteProtocolInfo: // d
		ficls = 0x37; //FileRemoteProtocolInformation;
		Length = sizeof(FILE_REMOTE_PROTOCOL_INFO);
		break;

	default:
		SetLastError(ERROR_INVALID_PARAMETER);
		return 0;
	}
	
	if(Length > size) {
		SetLastError(ERROR_BAD_LENGTH);
		return 0; 
	}
	
	if(directoryMode >= 0) 
	{
		status = NtQueryDirectoryFile(hFile, 0, 0, 0, 
			&IoStatusBlock, info, size, ficls, 0, 0, directoryMode);
		if(status == STATUS_PENDING) {
			status = NtWaitForSingleObject(hFile, 0, 0);
			if(!NT_SUCCESS(status)) goto SET_ERR;
			status = IoStatusBlock.Status;
		}
	} else {
		status = NtQueryInformationFile(hFile, &IoStatusBlock, info, size, ficls);
	}
	
	if(!NT_SUCCESS(status)) { SET_ERR:
		BaseSetLastNTError(status); return 0; }
	if((class != FileStreamInfo) ||
	IoStatusBlock.Information) return 1;
	BaseSetLastNTError(STATUS_END_OF_FILE);
	return 0;
}

/***********************************************************************
 *             OpenFileById (KERNEL32.@)
 */
HANDLE WINAPI OpenFileById(
  _In_     HANDLE                hFile,
  _In_     LPFILE_ID_DESCRIPTOR  lpFileID,
  _In_     DWORD                 dwDesiredAccess,
  _In_     DWORD                 dwShareMode,
  _In_opt_ LPSECURITY_ATTRIBUTES lpSecurityAttributes,
  _In_     DWORD                 dwFlags
){
	ACCESS_MASK DesiredAccess;
	ULONG CreateOptions;
	HANDLE result;
	OBJECT_ATTRIBUTES attr;
	NTSTATUS status;
	IO_STATUS_BLOCK io;
	UNICODE_STRING objectName;

	if (!lpFileID || (lpFileID->dwSize < sizeof(FILE_ID_DESCRIPTOR)))
	{
	    SetLastError( ERROR_INVALID_PARAMETER );
	    return INVALID_HANDLE_VALUE;
	}
	
	switch(lpFileID->Type)
	{
	case FileIdType:
		objectName.Length = sizeof(LARGE_INTEGER);
		objectName.MaximumLength = sizeof(LARGE_INTEGER);
		objectName.Buffer = (WCHAR *)&lpFileID->FileId;
		break;
	
	case ObjectIdType:
		objectName.Length = sizeof(GUID);
		objectName.MaximumLength = sizeof(GUID);	
		objectName.Buffer = (WCHAR *)&lpFileID->ObjectId;
		break;
		
	default:
		SetLastError( ERROR_INVALID_PARAMETER );
		return INVALID_HANDLE_VALUE;
	}
	
	
	DesiredAccess = dwDesiredAccess | 
		SYNCHRONIZE | FILE_READ_ATTRIBUTES;
	CreateOptions = FILE_OPEN_BY_FILE_ID;
	
	if (dwFlags & FILE_FLAG_WRITE_THROUGH)
		CreateOptions | FILE_WRITE_THROUGH;
	
	if (dwFlags & FILE_FLAG_NO_BUFFERING)
		CreateOptions |= FILE_NO_INTERMEDIATE_BUFFERING;
		
	if (dwFlags & FILE_FLAG_SEQUENTIAL_SCAN) 
		CreateOptions |= FILE_SEQUENTIAL_ONLY;

	if (dwFlags & FILE_FLAG_RANDOM_ACCESS) 
		CreateOptions |= FILE_RANDOM_ACCESS;		
		
	if (dwFlags & FILE_FLAG_BACKUP_SEMANTICS)
	    CreateOptions |= FILE_OPEN_FOR_BACKUP_INTENT;
	
	if (!(dwFlags & FILE_FLAG_OVERLAPPED))
		CreateOptions |= FILE_SYNCHRONOUS_IO_NONALERT;
		
	if(dwFlags & FILE_FLAG_DELETE_ON_CLOSE) {
		DesiredAccess |= DELETE;
		CreateOptions |= FILE_DELETE_ON_CLOSE; }
		
	if(dwFlags & FILE_FLAG_OPEN_REPARSE_POINT)
		CreateOptions |= FILE_OPEN_REPARSE_POINT;
		
	if (dwFlags & FILE_FLAG_OPEN_NO_RECALL)
		CreateOptions |= FILE_OPEN_NO_RECALL;

	attr.Length                   = sizeof(attr);
	attr.RootDirectory            = hFile;
	attr.Attributes               = OBJ_CASE_INSENSITIVE;
	attr.ObjectName               = &objectName;
	attr.SecurityDescriptor       = NULL;
	attr.SecurityQualityOfService = NULL;
	
	status = NtCreateFile( &result, DesiredAccess, &attr, &io, NULL,
	                       0, dwShareMode, FILE_OPEN, CreateOptions, NULL, 0);
	if (status != STATUS_SUCCESS)
	{
		BaseSetLastNTError( status );
	    return INVALID_HANDLE_VALUE;
	}
	return result;
}

BOOL 
WINAPI 
SetStdHandleEx(
	DWORD  nStdHandle,
	HANDLE hHandle,
	HANDLE* oldHandle  
)
{
	DWORD ofs;

	if(oldHandle) *oldHandle = 0;
	switch(nStdHandle)
	{
	case STD_INPUT_HANDLE: ofs = FIELD_OFFSET(
		RTL_USER_PROCESS_PARAMETERS, StandardInput); break;
	case STD_OUTPUT_HANDLE: ofs = FIELD_OFFSET(
		RTL_USER_PROCESS_PARAMETERS, StandardOutput); break;
	case STD_ERROR_HANDLE: ofs = FIELD_OFFSET(
		RTL_USER_PROCESS_PARAMETERS, StandardError); break;
	default: BaseSetLastNTError(
		STATUS_INVALID_HANDLE); return 0;
	}
	
	void* pp = NtCurrentPeb()->ProcessParameters;
	HANDLE old = *(HANDLE*)(pp + ofs);
	*(HANDLE*)(pp + ofs) = hHandle;
	asm volatile(""); 
	if(oldHandle) *oldHandle = old;
	return TRUE;
}
