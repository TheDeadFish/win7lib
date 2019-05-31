#include "k32_vista.h"
#include <ddk/mountmgr.h>
#include "stdshit.h"

typedef struct { 
	union { UNICODE_STRING us; USHORT Length; };
	WCHAR Buffer[]; } UNICODE_BUFFER;

static inline
BOOL WINAPI BasepGetObjectNTName(
	HANDLE handle, UNICODE_BUFFER** ppUStr)
{
	ULONG pUStrSize = sizeof(UNICODE_STRING) + MAX_PATH*2;
	UNICODE_BUFFER* pUStr; BOOL retVal = FALSE;
		
	while(1) { 
		if(!(pUStr = BaseAllocHeap(pUStrSize))) break;
		NTSTATUS status = NtQueryObject(handle, 
			ObjectNameInformation, pUStr, pUStrSize, &pUStrSize);
		if(NT_SUCCESS(status)) { retVal = TRUE; break; }
		BaseFreeHeap(pUStr); ZEROREG(pUStr);
		if(status != STATUS_BUFFER_OVERFLOW) {
			BaseSetLastNTError(status); break; }
	}
	
	*ppUStr = pUStr; return retVal;
}

static inline
BOOL WINAPI BasepGetFileNameLength(
	HANDLE handle, int* nameIndex)
{
	FILE_NAME_INFORMATION fni; IO_STATUS_BLOCK isb;
	ULONG pUStrSize = sizeof(UNICODE_STRING);
	NTSTATUS status = NtQueryInformationFile(handle, 
		&isb, &fni, sizeof(fni), FileNameInformation);
	*nameIndex = fni.FileNameLength;
	if(status != STATUS_BUFFER_OVERFLOW) {
		BaseSetLastNTError(status); return 0; }
	return 1;
}

HANDLE WINAPI BasepOpenMountMgr(void)
{
	return CreateFileW(MOUNTMGR_DOS_DEVICE_NAME,
		0, FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
		NULL, OPEN_EXISTING, 0, NULL);
}

WCHAR* WINAPI BasepMountMgrIsVolumeName(WCHAR* name, int len)
{
	if((len == 96 || (len == 98 && name[48] == '\\')) &&      
   name[0] == '\\'&& (name[1] == '?' || name[1] == '\\') && 
   name[2] == '?' && name[3] == '\\' && name[4] == 'V' &&   
   name[5] == 'o' && name[6] == 'l' && name[7] == 'u' &&    
   name[8] == 'm' && name[9] == 'e' && name[10] == '{' &&   
   name[19] == '-' && name[24] == '-' && name[29] == '-' && 
   name[34] == '-' && name[47] == '}')return name; return 0;
}

WCHAR* WINAPI BasepGetVolumeGUIDFromNTName(WCHAR* buff)
{
	// open mount manager
	HANDLE hDevice = BasepOpenMountMgr();
	if(hDevice == INVALID_HANDLE_VALUE) 
		return 0;
		
	// query mount points
	DWORD outSize = 576; void* outBuff;
	while(1) {
		if(!(outBuff = BaseAllocHeap(outSize))) goto CLEANUP;
		
		// prepare input buffer (MOUNTMGR_MOUNT_POINT)
		void* mmp = outBuff; STOSDN(mmp,0,5); RB(outBuff,16) = 24; 
		CPYFIX(WCHAR*, buff2, buff); CPYFIX(int, inSize, *buff2);
		STOSD(mmp, *buff2); memcpy(mmp, buff2+1, inSize);
		
		// execute the query
		if(DeviceIoControl(hDevice, IOCTL_MOUNTMGR_QUERY_POINTS, 
			outBuff, outSize, outBuff, outSize, &outSize, 0)) break;
		ERR_FREE: BaseFreeHeap(outBuff); ZEROREG(outBuff);
		if(GetWin32Err() != ERROR_MORE_DATA) goto CLEANUP;
	}
	
	// locate guid entry
	MOUNTMGR_MOUNT_POINTS* mmps = outBuff;
	MOUNTMGR_MOUNT_POINT* mmp = mmps->MountPoints-1;
	MOUNTMGR_MOUNT_POINT* mmpe = mmp+mmps->NumberOfMountPoints;
	while(1) { if(mmp >= mmpe) { SetLastError(
		ERROR_NOT_SUPPORTED); goto ERR_FREE; } mmp++;
		WCHAR* name = BasepMountMgrIsVolumeName(PW(mmps, mmp->
			SymbolicLinkNameOffset), mmp->SymbolicLinkNameLength);
		if(name) { MEMFIX(mmp->SymbolicLinkNameLength);
			int len = mmp->SymbolicLinkNameLength; RW(outBuff,0)
			= len; memcpy(outBuff+2, name, len); goto CLEANUP; }
	} 
		
CLEANUP:
	CloseHandle(hDevice);
	return outBuff;
}

WCHAR* WINAPI BasepGetVolumeDosLetterNameFromNTName(WCHAR* buff)
{
	// open mount manager
	HANDLE hDevice = BasepOpenMountMgr();
	if(hDevice == INVALID_HANDLE_VALUE) 
		return 0;
	
	// query dos volume path
	DWORD outSize = 248; void* outBuff;
	while(1) {
		if(!(outBuff = BaseAllocHeap(outSize+6))) goto CLEANUP;
		if(DeviceIoControl(hDevice, IOCTL_MOUNTMGR_QUERY_DOS_VOLUME_PATH, 
			buff, *buff+2, outBuff+6, outSize, &outSize, 0)) break;
		ERR_FREE: BaseFreeHeap(outBuff); ZEROREG(outBuff);
		if(GetWin32Err() != ERROR_MORE_DATA) goto CLEANUP;
	} 
	
	// prepend "\\?\"
	int buffLen = RI(outBuff,6);
	RI(outBuff, 0) = buffLen+4; 
	RI(outBuff,2) = 0x005C005C; 
	RI(outBuff, 6) = 0x005C003F;
	
	// check if volume name
	if(BasepMountMgrIsVolumeName(outBuff+10, buffLen)) {
		SetLastError(ERROR_PATH_NOT_FOUND); goto ERR_FREE; }
	
CLEANUP:
	CloseHandle(hDevice);
	return outBuff;
}

DWORD WINAPI GetFinalPathNameByHandleW(
  HANDLE hFile, LPWSTR lpszFilePath,
  DWORD cchFilePath, DWORD dwFlags)
{
	NTSTATUS status; int retVal = 0;
	UNICODE_BUFFER* objName = 0; VARFIX(objName);
	void* baseName = 0; MEMFIX(baseName);
	WCHAR* NamePtr1; int NameLen1;
	WCHAR* NamePtr2; int NameLen2;
	
	/* validate arguments */
	VARSET(status, STATUS_INVALID_HANDLE);
	if(hFile == (HANDLE)-1) goto ERR;
	VARSET(status, STATUS_INVALID_PARAMETER);
	if(!isSingleBit(dwFlags & (VOLUME_NAME_GUID | VOLUME_NAME_NT 
		| VOLUME_NAME_NONE))) goto ERR;
	
	/* get object name */
	if(!BasepGetObjectNTName(hFile, &objName)) goto CLEANUP;
	if(!BasepGetFileNameLength(hFile, &NameLen2)) goto CLEANUP;
	
	/* split object name */
	NameLen1 = objName->Length - NameLen2;
	NamePtr1 = objName->Buffer-1; *NamePtr1 = NameLen1;
	NamePtr2 = PW(objName->Buffer, NameLen1);
	//VARSET(status, STATUS_ACCESS_DENIED);
	if(*NamePtr2 != '\\') { status =
		STATUS_ACCESS_DENIED; goto ERR; }

	/* process volume name */
	if(dwFlags & (VOLUME_NAME_NT|VOLUME_NAME_NONE)) {
		if(dwFlags & VOLUME_NAME_NONE) { *NamePtr1 = 0; }
	} else { 
		if(dwFlags & VOLUME_NAME_GUID) {
			NamePtr1 = BasepGetVolumeGUIDFromNTName(NamePtr1);
		} else {if(!_wcsnicmp(NamePtr1, L"\x16\\Device\\MUP", 12)) {
				NamePtr1 = L"\xE\\\\?\\UNC"; goto DO_COPY; }
			NamePtr1 = BasepGetVolumeDosLetterNameFromNTName(NamePtr1);
		}	if(!(baseName = NamePtr1)) goto CLEANUP;
	}

	/* perform the copy */
	DO_COPY: NameLen1 = *NamePtr1;
	retVal = (NameLen1 + NameLen2)>>1;
	if(retVal >= cchFilePath) { retVal++; status = 
		STATUS_BUFFER_OVERFLOW; goto ERR; }
	memcpy(lpszFilePath, NamePtr1+1, NameLen1);
	memcpy(PW(lpszFilePath,NameLen1), NamePtr2, NameLen2);
	*PW(PW(lpszFilePath,NameLen1),NameLen2) = 0;
	
	
	/* error cleanup */
	if(0) { ERR: BaseSetLastNTError(status); }
CLEANUP: BaseFreeHeap(baseName);
	BaseFreeHeap(objName);
	return retVal;
}
