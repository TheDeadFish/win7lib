#include "k32_vista.h"

BOOL WINAPI CancelIoEx(HANDLE hFile, LPOVERLAPPED lpOverlapped) { 
	if(!lpOverlapped) CancelIo(hFile); return TRUE; }
BOOL WINAPI CancelSynchronousIo(HANDLE hFile) {	return TRUE; }
