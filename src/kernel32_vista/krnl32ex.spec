@ stdcall InitializeSRWLock(ptr) NTDLLEX.RtlInitializeSRWLock
@ stdcall AcquireSRWLockExclusive(ptr) NTDLLEX.RtlAcquireSRWLockExclusive
@ stdcall AcquireSRWLockShared(ptr) NTDLLEX.RtlAcquireSRWLockShared
@ stdcall ReleaseSRWLockExclusive(ptr) NTDLLEX.RtlReleaseSRWLockExclusive
@ stdcall ReleaseSRWLockShared(ptr) NTDLLEX.RtlReleaseSRWLockShared

@ stdcall InitializeConditionVariable(ptr) NTDLLEX.RtlInitializeConditionVariable
@ stdcall SleepConditionVariableCS(ptr ptr long)
@ stdcall SleepConditionVariableSRW(ptr ptr long long)
@ stdcall WakeAllConditionVariable(ptr) NTDLLEX.RtlWakeAllConditionVariable
@ stdcall WakeConditionVariable(ptr) NTDLLEX.RtlWakeConditionVariable

@ stdcall InitializeCriticalSectionEx(ptr long long)




@ stdcall GetTimeFormatEx(wstr long ptr wstr ptr long)
@ stdcall GetDateFormatEx(wstr long ptr wstr ptr long wstr)

@ stdcall CancelIoEx(long ptr)
@ stdcall CancelSynchronousIo(ptr)

@ stdcall GetFinalPathNameByHandleW(ptr wstr long long)

@ stdcall CreateSymbolicLinkW(wstr wstr long) 
