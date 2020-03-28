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
@ stdcall GetQueuedCompletionStatusEx(ptr ptr long ptr long long)

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

# process.c functions
@ stdcall InitializeProcThreadAttributeList(ptr long long ptr)
@ stdcall UpdateProcThreadAttribute(ptr long long ptr long ptr ptr)
@ stdcall DeleteProcThreadAttributeList(ptr)



@ stdcall GetTickCount64() KERNEL32.GetTickCount
@ stdcall GetCurrentProcessorNumberEx(ptr) NTDLLEX.RtlGetCurrentProcessorNumberEx


# fileops.c
@ stdcall GetFileInformationByHandleEx(ptr long ptr long)
@ stdcall OpenFileById(ptr ptr long long ptr long)
@ stdcall SetStdHandleEx(long ptr ptr)

# time.c
@ stdcall GetSystemTimePreciseAsFileTime(ptr)
