@ stdcall InitializeSRWLock(ptr) NTDLLEX.RtlInitializeSRWLock
@ stdcall AcquireSRWLockExclusive(ptr) NTDLLEX.RtlAcquireSRWLockExclusive
@ stdcall AcquireSRWLockShared(ptr) NTDLLEX.RtlAcquireSRWLockShared
@ stdcall ReleaseSRWLockExclusive(ptr) NTDLLEX.RtlReleaseSRWLockExclusive
@ stdcall ReleaseSRWLockShared(ptr) NTDLLEX.RtlReleaseSRWLockShared

@ stdcall InitializeConditionVariable(ptr) ntdll.RtlInitializeConditionVariable
@ stdcall SleepConditionVariableCS(ptr ptr long)
@ stdcall SleepConditionVariableSRW(ptr ptr long long)
@ stdcall WakeAllConditionVariable(ptr) ntdll.RtlWakeAllConditionVariable
@ stdcall WakeConditionVariable(ptr) ntdll.RtlWakeConditionVariable

@ stdcall InitializeCriticalSectionEx(ptr long long)
