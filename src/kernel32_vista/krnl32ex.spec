@ stdcall InitializeSRWLock(ptr) NTDLL.RtlInitializeSRWLock
@ stdcall AcquireSRWLockExclusive(ptr) NTDLL.RtlAcquireSRWLockExclusive
@ stdcall AcquireSRWLockShared(ptr) NTDLL.RtlAcquireSRWLockShared
@ stdcall ReleaseSRWLockExclusive(ptr) NTDLL.RtlReleaseSRWLockExclusive
@ stdcall ReleaseSRWLockShared(ptr) NTDLL.RtlReleaseSRWLockShared

@ stdcall InitializeConditionVariable(ptr) NTDLL.RtlInitializeConditionVariable
@ stdcall SleepConditionVariableCS(ptr ptr long)
@ stdcall SleepConditionVariableSRW(ptr ptr long long)
@ stdcall WakeAllConditionVariable(ptr) NTDLL.RtlWakeAllConditionVariable
@ stdcall WakeConditionVariable(ptr) NTDLL.RtlWakeConditionVariable

@ stdcall InitializeCriticalSectionEx(ptr long long)




@ stdcall GetTimeFormatEx(wstr long ptr wstr ptr long)
@ stdcall GetDateFormatEx(wstr long ptr wstr ptr long wstr)

@ stdcall CancelIoEx(long ptr)
@ stdcall CancelSynchronousIo(ptr)

@ stdcall GetFinalPathNameByHandleW(ptr wstr long long)

@ stdcall CreateSymbolicLinkW(wstr wstr long) 

@ stdcall SetFileInformationByHandle(long long ptr long)

# PSAPI forwards
@ stdcall K32EmptyWorkingSet(long) PSAPI.EmptyWorkingSet
@ stdcall K32EnumDeviceDrivers(ptr long ptr) PSAPI.EnumDeviceDrivers
@ stdcall K32EnumPageFilesA(ptr ptr) PSAPI.EnumPageFilesA
@ stdcall K32EnumPageFilesW(ptr ptr) PSAPI.EnumPageFilesW
@ stdcall K32EnumProcessModules(long ptr long ptr) PSAPI.EnumProcessModules
@ stdcall K32EnumProcessModulesEx(long ptr long ptr long) PSAPI.EnumProcessModulesEx
@ stdcall K32EnumProcesses(ptr long ptr) PSAPI.EnumProcesses
@ stdcall K32GetDeviceDriverBaseNameA(ptr ptr long) PSAPI.GetDeviceDriverBaseNameA
@ stdcall K32GetDeviceDriverBaseNameW(ptr ptr long) PSAPI.GetDeviceDriverBaseNameW
@ stdcall K32GetDeviceDriverFileNameA(ptr ptr long) PSAPI.GetDeviceDriverFileNameA
@ stdcall K32GetDeviceDriverFileNameW(ptr ptr long) PSAPI.GetDeviceDriverFileNameW
@ stdcall K32GetMappedFileNameA(long ptr ptr long) PSAPI.GetMappedFileNameA
@ stdcall K32GetMappedFileNameW(long ptr ptr long) PSAPI.GetMappedFileNameW
@ stdcall K32GetModuleBaseNameA(long long ptr long) PSAPI.GetModuleBaseNameA
@ stdcall K32GetModuleBaseNameW(long long ptr long) PSAPI.GetModuleBaseNameW
@ stdcall K32GetModuleFileNameExA(long long ptr long) PSAPI.GetModuleFileNameExA
@ stdcall K32GetModuleFileNameExW(long long ptr long) PSAPI.GetModuleFileNameExW
@ stdcall K32GetModuleInformation(long long ptr long) PSAPI.GetModuleInformation
@ stdcall K32GetPerformanceInfo(ptr long) PSAPI.GetPerformanceInfo
@ stdcall K32GetProcessImageFileNameA(long ptr long) PSAPI.GetProcessImageFileNameA
@ stdcall K32GetProcessImageFileNameW(long ptr long) PSAPI.GetProcessImageFileNameW
@ stdcall K32GetProcessMemoryInfo(long ptr long) PSAPI.GetProcessMemoryInfo
@ stdcall K32GetWsChanges(long ptr long) PSAPI.GetWsChanges
@ stdcall K32GetWsChangesEx(long ptr ptr) PSAPI.GetWsChangesEx
@ stdcall K32InitializeProcessForWsWatch(long) PSAPI.InitializeProcessForWsWatch
@ stdcall K32QueryWorkingSet(long ptr long) PSAPI.QueryWorkingSet
@ stdcall K32QueryWorkingSetEx(long ptr long) PSAPI.QueryWorkingSetEx
