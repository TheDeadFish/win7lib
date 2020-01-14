#include "k32_vista.h"

static 
BOOL getQueuedCompletionStatus(
	HANDLE CompletionPort,
	LPOVERLAPPED_ENTRY lpEnt,
	DWORD dwMilliseconds
) {
	return GetQueuedCompletionStatus(CompletionPort, 
		&lpEnt->dwNumberOfBytesTransferred,
		&lpEnt->lpCompletionKey,
		&lpEnt->lpOverlapped, dwMilliseconds);
}

BOOL WINAPI GetQueuedCompletionStatusEx(
  HANDLE             CompletionPort,
  LPOVERLAPPED_ENTRY lpCompletionPortEntries,
  ULONG              ulCount,
  PULONG             ulNumEntriesRemoved,
  DWORD              dwMilliseconds,
  BOOL               fAlertable
) {
	
	// validate arguments
	if(!lpCompletionPortEntries
	|| !ulCount || !ulNumEntriesRemoved) {
		RtlSetLastWin32Error(ERROR_INVALID_PARAMETER);
		return FALSE; }

	// partial implementation error
	if(fAlertable)
		kex_fatal("GetQueuedCompletionStatusEx: fAlertable");
		
	// retrieve multiple entries
	int i = 0;
	for(;i < ulCount; i++)
	{	
		if(!getQueuedCompletionStatus(CompletionPort, 
		lpCompletionPortEntries+i, dwMilliseconds)) break;
		dwMilliseconds = 0;
	}

	*ulNumEntriesRemoved = i;
	return !!i;
}
