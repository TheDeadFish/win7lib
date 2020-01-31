@ stdcall ActivateActCtx(ptr ptr) KERNEL32.ActivateActCtx
@ stdcall AddAtomA(str) KERNEL32.AddAtomA
@ stdcall AddAtomW(wstr) KERNEL32.AddAtomW
@ stdcall AddConsoleAliasA(str str str) KERNEL32.AddConsoleAliasA
@ stdcall AddConsoleAliasW(wstr wstr wstr) KERNEL32.AddConsoleAliasW
@ stdcall AddLocalAlternateComputerNameA(str ptr) KERNEL32.AddLocalAlternateComputerNameA
@ stdcall AddLocalAlternateComputerNameW(wstr ptr) KERNEL32.AddLocalAlternateComputerNameW
@ stdcall AddRefActCtx(ptr) KERNEL32.AddRefActCtx
@ stdcall AddVectoredContinueHandler(long ptr) ntdll.RtlAddVectoredContinueHandler
@ stdcall AddVectoredExceptionHandler(long ptr) ntdll.RtlAddVectoredExceptionHandler
@ stdcall AllocConsole() KERNEL32.AllocConsole
@ stdcall AllocateUserPhysicalPages(long ptr ptr) KERNEL32.AllocateUserPhysicalPages
@ stdcall AreFileApisANSI() KERNEL32.AreFileApisANSI
@ stdcall AssignProcessToJobObject(ptr ptr) KERNEL32.AssignProcessToJobObject
@ stdcall AttachConsole(long) KERNEL32.AttachConsole
@ stdcall BackupRead(ptr ptr long ptr long long ptr) KERNEL32.BackupRead
@ stdcall BackupSeek(ptr long long ptr ptr ptr) KERNEL32.BackupSeek
@ stdcall BackupWrite(ptr ptr long ptr long long ptr) KERNEL32.BackupWrite
@ stdcall BaseCheckAppcompatCache(long long long ptr) KERNEL32.BaseCheckAppcompatCache
@ stdcall BaseCheckRunApp(long ptr long long long long long long long long) KERNEL32.BaseCheckRunApp
@ stdcall BaseCleanupAppcompatCacheSupport(ptr) KERNEL32.BaseCleanupAppcompatCacheSupport
@ stdcall BaseDumpAppcompatCache() KERNEL32.BaseDumpAppcompatCache
@ stdcall BaseFlushAppcompatCache() KERNEL32.BaseFlushAppcompatCache
@ stdcall BaseInitAppcompatCacheSupport() KERNEL32.BaseInitAppcompatCacheSupport
@ stdcall BaseIsAppcompatInfrastructureDisabled()  KERNEL32.BaseIsAppcompatInfrastructureDisabled
@ stdcall -version=0x501-0x502 BaseProcessInitPostImport() KERNEL32.BaseProcessInitPostImport
@ stdcall BaseQueryModuleData(str str ptr ptr ptr) KERNEL32.BaseQueryModuleData
@ stdcall BaseUpdateAppcompatCache(long long long) KERNEL32.BaseUpdateAppcompatCache
@ stdcall BasepCheckBadapp(long ptr long long long long long long long) KERNEL32.BasepCheckBadapp
@ stdcall BasepCheckWinSaferRestrictions(long long long long long long) KERNEL32.BasepCheckWinSaferRestrictions
@ stdcall BasepFreeAppCompatData(ptr ptr) KERNEL32.BasepFreeAppCompatData
@ stdcall Beep(long long) KERNEL32.Beep
@ stdcall BeginUpdateResourceA(str long) KERNEL32.BeginUpdateResourceA
@ stdcall BeginUpdateResourceW(wstr long) KERNEL32.BeginUpdateResourceW
@ stdcall BindIoCompletionCallback(long ptr long) KERNEL32.BindIoCompletionCallback
@ stdcall BuildCommDCBA(str ptr) KERNEL32.BuildCommDCBA
@ stdcall BuildCommDCBAndTimeoutsA(str ptr ptr) KERNEL32.BuildCommDCBAndTimeoutsA
@ stdcall BuildCommDCBAndTimeoutsW(wstr ptr ptr) KERNEL32.BuildCommDCBAndTimeoutsW
@ stdcall BuildCommDCBW(wstr ptr) KERNEL32.BuildCommDCBW
@ stdcall CallNamedPipeA(str ptr long ptr long ptr long) KERNEL32.CallNamedPipeA
@ stdcall CallNamedPipeW(wstr ptr long ptr long ptr long) KERNEL32.CallNamedPipeW
@ stdcall CancelDeviceWakeupRequest(long) KERNEL32.CancelDeviceWakeupRequest
@ stdcall CancelIo(long) KERNEL32.CancelIo
@ stdcall CancelTimerQueueTimer(long long) KERNEL32.CancelTimerQueueTimer
@ stdcall CancelWaitableTimer(long) KERNEL32.CancelWaitableTimer
@ stdcall ChangeTimerQueueTimer(ptr ptr long long) KERNEL32.ChangeTimerQueueTimer
@ stdcall CheckNameLegalDOS8Dot3A(str str long long long) KERNEL32.CheckNameLegalDOS8Dot3A
@ stdcall CheckNameLegalDOS8Dot3W(wstr str long long long) KERNEL32.CheckNameLegalDOS8Dot3W
@ stdcall CheckRemoteDebuggerPresent(long ptr) KERNEL32.CheckRemoteDebuggerPresent
@ stdcall ClearCommBreak(long) KERNEL32.ClearCommBreak
@ stdcall ClearCommError(long ptr ptr) KERNEL32.ClearCommError
@ stdcall CloseConsoleHandle(long) KERNEL32.CloseConsoleHandle
@ stdcall CloseHandle(long) KERNEL32.CloseHandle
@ stdcall CloseProfileUserMapping() KERNEL32.CloseProfileUserMapping
@ stdcall CmdBatNotification(long) KERNEL32.CmdBatNotification
@ stdcall CommConfigDialogA(str long ptr) KERNEL32.CommConfigDialogA
@ stdcall CommConfigDialogW(wstr long ptr) KERNEL32.CommConfigDialogW
@ stdcall CompareFileTime(ptr ptr) KERNEL32.CompareFileTime
@ stdcall CompareStringA(long long str long str long) KERNEL32.CompareStringA
@ stdcall CompareStringW(long long wstr long wstr long) KERNEL32.CompareStringW
@ stdcall ConnectNamedPipe(long ptr) KERNEL32.ConnectNamedPipe
@ stdcall ConsoleMenuControl(long long long) KERNEL32.ConsoleMenuControl
@ stdcall ContinueDebugEvent(long long long) KERNEL32.ContinueDebugEvent
@ stdcall ConvertDefaultLocale (long) KERNEL32.ConvertDefaultLocale
@ stdcall ConvertFiberToThread() KERNEL32.ConvertFiberToThread
@ stdcall ConvertThreadToFiber(ptr) KERNEL32.ConvertThreadToFiber
@ stdcall ConvertThreadToFiberEx(ptr long) KERNEL32.ConvertThreadToFiberEx
@ stdcall CopyFileA(str str long) KERNEL32.CopyFileA
@ stdcall CopyFileExA (str str ptr ptr ptr long) KERNEL32.CopyFileExA
@ stdcall CopyFileExW (wstr wstr ptr ptr ptr long) KERNEL32.CopyFileExW
@ stdcall CopyFileW(wstr wstr long) KERNEL32.CopyFileW
@ stdcall CopyLZFile(long long)  KERNEL32.CopyLZFile
@ stdcall CreateActCtxA(ptr) KERNEL32.CreateActCtxA
@ stdcall CreateActCtxW(ptr) KERNEL32.CreateActCtxW
@ stdcall CreateConsoleScreenBuffer(long long ptr long ptr) KERNEL32.CreateConsoleScreenBuffer
@ stdcall CreateDirectoryA(str ptr) KERNEL32.CreateDirectoryA
@ stdcall CreateDirectoryExA(str str ptr) KERNEL32.CreateDirectoryExA
@ stdcall CreateDirectoryExW(wstr wstr ptr) KERNEL32.CreateDirectoryExW
@ stdcall CreateDirectoryW(wstr ptr) KERNEL32.CreateDirectoryW
@ stdcall CreateEventA(ptr long long str) KERNEL32.CreateEventA
@ stdcall CreateEventW(ptr long long wstr) KERNEL32.CreateEventW
@ stdcall CreateFiber(long ptr ptr) KERNEL32.CreateFiber
@ stdcall CreateFiberEx(long long long ptr ptr) KERNEL32.CreateFiberEx
@ stdcall CreateFileA(str long long ptr long long long) KERNEL32.CreateFileA
@ stdcall CreateFileMappingA(long ptr long long long str) KERNEL32.CreateFileMappingA
@ stdcall CreateFileMappingW(long ptr long long long wstr) KERNEL32.CreateFileMappingW
@ stdcall CreateFileW(wstr long long ptr long long long) KERNEL32.CreateFileW
@ stdcall CreateHardLinkA(str str ptr) KERNEL32.CreateHardLinkA
@ stdcall CreateHardLinkW(wstr wstr ptr) KERNEL32.CreateHardLinkW
@ stdcall CreateIoCompletionPort(long long long long) KERNEL32.CreateIoCompletionPort
@ stdcall CreateJobObjectA(ptr str) KERNEL32.CreateJobObjectA
@ stdcall CreateJobObjectW(ptr wstr) KERNEL32.CreateJobObjectW
@ stdcall CreateJobSet(long ptr long) KERNEL32.CreateJobSet
@ stdcall CreateMailslotA(ptr long long ptr) KERNEL32.CreateMailslotA
@ stdcall CreateMailslotW(ptr long long ptr) KERNEL32.CreateMailslotW
@ stdcall CreateMemoryResourceNotification(long) KERNEL32.CreateMemoryResourceNotification
@ stdcall CreateMutexA(ptr long str) KERNEL32.CreateMutexA
@ stdcall CreateMutexW(ptr long wstr) KERNEL32.CreateMutexW
@ stdcall CreateNamedPipeA(str long long long long long long ptr) KERNEL32.CreateNamedPipeA
@ stdcall CreateNamedPipeW(wstr long long long long long long ptr) KERNEL32.CreateNamedPipeW
@ stdcall -version=0x501-0x502 CreateNlsSecurityDescriptor(ptr long long) KERNEL32.CreateNlsSecurityDescriptor
@ stdcall CreatePipe(ptr ptr ptr long) KERNEL32.CreatePipe
@ stdcall CreateProcessA(str str ptr ptr long long ptr str ptr ptr) KERNEL32.CreateProcessA
@ stdcall CreateProcessInternalA(ptr str str ptr ptr long long ptr str ptr ptr long) KERNEL32.CreateProcessInternalA
@ stdcall CreateProcessInternalW(ptr wstr wstr ptr ptr long long ptr wstr ptr ptr long) KERNEL32.CreateProcessInternalW
@ stdcall CreateProcessW(wstr wstr ptr ptr long long ptr wstr ptr ptr) KERNEL32.CreateProcessW
@ stdcall CreateRemoteThread(long ptr long ptr long long ptr) KERNEL32.CreateRemoteThread
@ stdcall CreateSemaphoreA(ptr long long str) KERNEL32.CreateSemaphoreA
@ stdcall CreateSemaphoreW(ptr long long wstr) KERNEL32.CreateSemaphoreW
@ stdcall -i386 CreateSocketHandle() KERNEL32.CreateSocketHandle
@ stdcall CreateTapePartition(long long long long) KERNEL32.CreateTapePartition
@ stdcall CreateThread(ptr long ptr long long ptr) KERNEL32.CreateThread
@ stdcall CreateTimerQueue () KERNEL32.CreateTimerQueue
@ stdcall CreateTimerQueueTimer(ptr long ptr ptr long long long) KERNEL32.CreateTimerQueueTimer
@ stdcall CreateToolhelp32Snapshot(long long) KERNEL32.CreateToolhelp32Snapshot
@ stdcall CreateWaitableTimerA(ptr long str) KERNEL32.CreateWaitableTimerA
@ stdcall CreateWaitableTimerW(ptr long wstr) KERNEL32.CreateWaitableTimerW
@ stdcall DeactivateActCtx(long ptr) KERNEL32.DeactivateActCtx
@ stdcall DebugActiveProcess(long) KERNEL32.DebugActiveProcess
@ stdcall DebugActiveProcessStop(long) KERNEL32.DebugActiveProcessStop
@ stdcall DebugBreak() ntdll.DbgBreakPoint
@ stdcall DebugBreakProcess(long) KERNEL32.DebugBreakProcess
@ stdcall DebugSetProcessKillOnExit(long) KERNEL32.DebugSetProcessKillOnExit
@ stdcall DecodePointer(ptr) ntdll.RtlDecodePointer
@ stdcall DecodeSystemPointer(ptr) ntdll.RtlDecodeSystemPointer
@ stdcall DefineDosDeviceA(long str str) KERNEL32.DefineDosDeviceA
@ stdcall DefineDosDeviceW(long wstr wstr) KERNEL32.DefineDosDeviceW
@ stdcall DelayLoadFailureHook(str str) KERNEL32.DelayLoadFailureHook
@ stdcall DeleteAtom(long) KERNEL32.DeleteAtom
@ stdcall DeleteCriticalSection(ptr) ntdll.RtlDeleteCriticalSection
@ stdcall DeleteFiber(ptr) KERNEL32.DeleteFiber
@ stdcall DeleteFileA(str) KERNEL32.DeleteFileA
@ stdcall DeleteFileW(wstr) KERNEL32.DeleteFileW
@ stdcall DeleteTimerQueue(long) KERNEL32.DeleteTimerQueue
@ stdcall DeleteTimerQueueEx (long long) KERNEL32.DeleteTimerQueueEx
@ stdcall DeleteTimerQueueTimer(long long long) KERNEL32.DeleteTimerQueueTimer
@ stdcall DeleteVolumeMountPointA(str) KERNEL32.DeleteVolumeMountPointA
@ stdcall DeleteVolumeMountPointW(wstr) KERNEL32.DeleteVolumeMountPointW
@ stdcall DeviceIoControl(long long ptr long ptr long ptr ptr) KERNEL32.DeviceIoControl
@ stdcall DisableThreadLibraryCalls(long) KERNEL32.DisableThreadLibraryCalls
@ stdcall DisconnectNamedPipe(long) KERNEL32.DisconnectNamedPipe
@ stdcall DnsHostnameToComputerNameA (str ptr ptr) KERNEL32.DnsHostnameToComputerNameA
@ stdcall DnsHostnameToComputerNameW (wstr ptr ptr) KERNEL32.DnsHostnameToComputerNameW
@ stdcall DosDateTimeToFileTime(long long ptr) KERNEL32.DosDateTimeToFileTime
@ stdcall DosPathToSessionPathA(long str str) KERNEL32.DosPathToSessionPathA
@ stdcall DosPathToSessionPathW(long wstr wstr) KERNEL32.DosPathToSessionPathW
@ stdcall DuplicateConsoleHandle(long long long long) KERNEL32.DuplicateConsoleHandle
@ stdcall DuplicateHandle(long long long ptr long long long) KERNEL32.DuplicateHandle
@ stdcall EncodePointer(ptr) ntdll.RtlEncodePointer
@ stdcall EncodeSystemPointer(ptr) ntdll.RtlEncodeSystemPointer
@ stdcall EndUpdateResourceA(long long) KERNEL32.EndUpdateResourceA
@ stdcall EndUpdateResourceW(long long) KERNEL32.EndUpdateResourceW
@ stdcall EnterCriticalSection(ptr) ntdll.RtlEnterCriticalSection
@ stdcall EnumCalendarInfoA(ptr long long long) KERNEL32.EnumCalendarInfoA
@ stdcall EnumCalendarInfoExA(ptr long long long) KERNEL32.EnumCalendarInfoExA
@ stdcall EnumCalendarInfoExW(ptr long long long) KERNEL32.EnumCalendarInfoExW
@ stdcall EnumCalendarInfoW(ptr long long long) KERNEL32.EnumCalendarInfoW
@ stdcall EnumDateFormatsA(ptr long long) KERNEL32.EnumDateFormatsA
@ stdcall EnumDateFormatsExA(ptr long long) KERNEL32.EnumDateFormatsExA
@ stdcall EnumDateFormatsExW(ptr long long) KERNEL32.EnumDateFormatsExW
@ stdcall EnumDateFormatsW(ptr long long) KERNEL32.EnumDateFormatsW
@ stdcall EnumLanguageGroupLocalesA(ptr long long ptr) KERNEL32.EnumLanguageGroupLocalesA
@ stdcall EnumLanguageGroupLocalesW(ptr long long ptr) KERNEL32.EnumLanguageGroupLocalesW
@ stdcall EnumResourceLanguagesA(long str str ptr long) KERNEL32.EnumResourceLanguagesA
@ stdcall EnumResourceLanguagesW(long wstr wstr ptr long) KERNEL32.EnumResourceLanguagesW
@ stdcall EnumResourceNamesA(long str ptr long) KERNEL32.EnumResourceNamesA
@ stdcall EnumResourceNamesW(long wstr ptr long) KERNEL32.EnumResourceNamesW
@ stdcall EnumResourceTypesA(long ptr long) KERNEL32.EnumResourceTypesA
@ stdcall EnumResourceTypesW(long ptr long) KERNEL32.EnumResourceTypesW
@ stdcall EnumSystemCodePagesA(ptr long) KERNEL32.EnumSystemCodePagesA
@ stdcall EnumSystemCodePagesW(ptr long) KERNEL32.EnumSystemCodePagesW
@ stdcall EnumSystemFirmwareTables(long ptr long) KERNEL32.EnumSystemFirmwareTables
@ stdcall EnumSystemGeoID(long long ptr) KERNEL32.EnumSystemGeoID
@ stdcall EnumSystemLanguageGroupsA(ptr long ptr) KERNEL32.EnumSystemLanguageGroupsA
@ stdcall EnumSystemLanguageGroupsW(ptr long ptr) KERNEL32.EnumSystemLanguageGroupsW
@ stdcall EnumSystemLocalesA(ptr long) KERNEL32.EnumSystemLocalesA
@ stdcall EnumSystemLocalesW(ptr long) KERNEL32.EnumSystemLocalesW
@ stdcall EnumTimeFormatsA(ptr long long) KERNEL32.EnumTimeFormatsA
@ stdcall EnumTimeFormatsW(ptr long long) KERNEL32.EnumTimeFormatsW
@ stdcall EnumUILanguagesA(ptr long long) KERNEL32.EnumUILanguagesA
@ stdcall EnumUILanguagesW(ptr long long) KERNEL32.EnumUILanguagesW
@ stdcall EnumerateLocalComputerNamesA(ptr long str ptr) KERNEL32.EnumerateLocalComputerNamesA
@ stdcall EnumerateLocalComputerNamesW(ptr long wstr ptr) KERNEL32.EnumerateLocalComputerNamesW
@ stdcall EraseTape(ptr long long) KERNEL32.EraseTape
@ stdcall EscapeCommFunction(long long) KERNEL32.EscapeCommFunction
@ stdcall ExitProcess(long) KERNEL32.ExitProcess
@ stdcall ExitThread(long) KERNEL32.ExitThread
@ stdcall ExitVDM(long long) KERNEL32.ExitVDM
@ stdcall ExpandEnvironmentStringsA(str ptr long) KERNEL32.ExpandEnvironmentStringsA
@ stdcall ExpandEnvironmentStringsW(wstr ptr long) KERNEL32.ExpandEnvironmentStringsW
@ stdcall ExpungeConsoleCommandHistoryA(long) KERNEL32.ExpungeConsoleCommandHistoryA
@ stdcall ExpungeConsoleCommandHistoryW(long) KERNEL32.ExpungeConsoleCommandHistoryW
@ stdcall FatalAppExitA(long str) KERNEL32.FatalAppExitA
@ stdcall FatalAppExitW(long wstr) KERNEL32.FatalAppExitW
@ stdcall FatalExit(long) KERNEL32.FatalExit
@ stdcall FileTimeToDosDateTime(ptr ptr ptr) KERNEL32.FileTimeToDosDateTime
@ stdcall FileTimeToLocalFileTime(ptr ptr) KERNEL32.FileTimeToLocalFileTime
@ stdcall FileTimeToSystemTime(ptr ptr) KERNEL32.FileTimeToSystemTime
@ stdcall FillConsoleOutputAttribute(long long long long ptr) KERNEL32.FillConsoleOutputAttribute
@ stdcall FillConsoleOutputCharacterA(long long long long ptr) KERNEL32.FillConsoleOutputCharacterA
@ stdcall FillConsoleOutputCharacterW(long long long long ptr) KERNEL32.FillConsoleOutputCharacterW
@ stdcall FindActCtxSectionGuid(long ptr long ptr ptr) KERNEL32.FindActCtxSectionGuid
@ stdcall FindActCtxSectionStringA(long ptr long str ptr) KERNEL32.FindActCtxSectionStringA
@ stdcall FindActCtxSectionStringW(long ptr long wstr ptr) KERNEL32.FindActCtxSectionStringW
@ stdcall FindAtomA(str) KERNEL32.FindAtomA
@ stdcall FindAtomW(wstr) KERNEL32.FindAtomW
@ stdcall FindClose(long) KERNEL32.FindClose
@ stdcall FindCloseChangeNotification(long) KERNEL32.FindCloseChangeNotification
@ stdcall FindFirstChangeNotificationA(str long long) KERNEL32.FindFirstChangeNotificationA
@ stdcall FindFirstChangeNotificationW(wstr long long) KERNEL32.FindFirstChangeNotificationW
@ stdcall FindFirstFileA(str ptr) KERNEL32.FindFirstFileA
@ stdcall FindFirstFileExA(str long ptr long ptr long) KERNEL32.FindFirstFileExA
@ stdcall FindFirstFileExW(wstr long ptr long ptr long) KERNEL32.FindFirstFileExW
@ stdcall FindFirstFileW(wstr ptr) KERNEL32.FindFirstFileW
@ stdcall FindFirstStreamW(wstr ptr ptr long) KERNEL32.FindFirstStreamW
@ stdcall FindFirstVolumeA(ptr long) KERNEL32.FindFirstVolumeA
@ stdcall FindFirstVolumeMountPointA(str ptr long) KERNEL32.FindFirstVolumeMountPointA
@ stdcall FindFirstVolumeMountPointW(wstr ptr long) KERNEL32.FindFirstVolumeMountPointW
@ stdcall FindFirstVolumeW(ptr long) KERNEL32.FindFirstVolumeW
@ stdcall FindNextChangeNotification(long) KERNEL32.FindNextChangeNotification
@ stdcall FindNextFileA(long ptr) KERNEL32.FindNextFileA
@ stdcall FindNextFileW(long ptr) KERNEL32.FindNextFileW
@ stdcall FindNextStreamW(ptr ptr) KERNEL32.FindNextStreamW
@ stdcall FindNextVolumeA(long ptr long) KERNEL32.FindNextVolumeA
@ stdcall FindNextVolumeMountPointA(long str long) KERNEL32.FindNextVolumeMountPointA
@ stdcall FindNextVolumeMountPointW(long wstr long) KERNEL32.FindNextVolumeMountPointW
@ stdcall FindNextVolumeW(long ptr long) KERNEL32.FindNextVolumeW
@ stdcall FindResourceA(long str str) KERNEL32.FindResourceA
@ stdcall FindResourceExA(long str str long) KERNEL32.FindResourceExA
@ stdcall FindResourceExW(long wstr wstr long) KERNEL32.FindResourceExW
@ stdcall FindResourceW(long wstr wstr) KERNEL32.FindResourceW
@ stdcall FindVolumeClose(ptr) KERNEL32.FindVolumeClose
@ stdcall FindVolumeMountPointClose(ptr) KERNEL32.FindVolumeMountPointClose
@ stdcall FlsAlloc(ptr) KERNEL32.FlsAlloc
@ stdcall FlsFree(long) KERNEL32.FlsFree
@ stdcall FlsGetValue(long) KERNEL32.FlsGetValue
@ stdcall FlsSetValue(long ptr) KERNEL32.FlsSetValue
@ stdcall FlushConsoleInputBuffer(long) KERNEL32.FlushConsoleInputBuffer
@ stdcall FlushFileBuffers(long) KERNEL32.FlushFileBuffers
@ stdcall FlushInstructionCache(long long long) KERNEL32.FlushInstructionCache
@ stdcall FlushViewOfFile(ptr long) KERNEL32.FlushViewOfFile
@ stdcall FoldStringA(long str long ptr long) KERNEL32.FoldStringA
@ stdcall FoldStringW(long wstr long ptr long) KERNEL32.FoldStringW
@ stdcall FormatMessageA(long ptr long long ptr long ptr) KERNEL32.FormatMessageA
@ stdcall FormatMessageW(long ptr long long ptr long ptr) KERNEL32.FormatMessageW
@ stdcall FreeConsole() KERNEL32.FreeConsole
@ stdcall FreeEnvironmentStringsA(ptr) KERNEL32.FreeEnvironmentStringsA
@ stdcall FreeEnvironmentStringsW(ptr) KERNEL32.FreeEnvironmentStringsW
@ stdcall FreeLibrary(long) KERNEL32.FreeLibrary
@ stdcall FreeLibraryAndExitThread(long long) KERNEL32.FreeLibraryAndExitThread
@ stdcall FreeResource(long) KERNEL32.FreeResource
@ stdcall FreeUserPhysicalPages(long long long) KERNEL32.FreeUserPhysicalPages
@ stdcall GenerateConsoleCtrlEvent(long long) KERNEL32.GenerateConsoleCtrlEvent
@ stdcall GetACP() KERNEL32.GetACP
@ stdcall GetAtomNameA(long ptr long) KERNEL32.GetAtomNameA
@ stdcall GetAtomNameW(long ptr long) KERNEL32.GetAtomNameW
@ stdcall GetBinaryType(str ptr)  KERNEL32.GetBinaryType
@ stdcall GetBinaryTypeA(str ptr) KERNEL32.GetBinaryTypeA
@ stdcall GetBinaryTypeW(wstr ptr) KERNEL32.GetBinaryTypeW
@ stdcall -version=0x501-0x600 GetCPFileNameFromRegistry(long wstr long) KERNEL32.GetCPFileNameFromRegistry
@ stdcall GetCPInfo(long ptr) KERNEL32.GetCPInfo
@ stdcall GetCPInfoExA(long long ptr) KERNEL32.GetCPInfoExA
@ stdcall GetCPInfoExW(long long ptr) KERNEL32.GetCPInfoExW
@ stdcall GetCalendarInfoA(long long long ptr long ptr) KERNEL32.GetCalendarInfoA
@ stdcall GetCalendarInfoW(long long long ptr long ptr) KERNEL32.GetCalendarInfoW
@ stdcall GetComPlusPackageInstallStatus() KERNEL32.GetComPlusPackageInstallStatus
@ stdcall GetCommConfig(long ptr long) KERNEL32.GetCommConfig
@ stdcall GetCommMask(long ptr) KERNEL32.GetCommMask
@ stdcall GetCommModemStatus(long ptr) KERNEL32.GetCommModemStatus
@ stdcall GetCommProperties(long ptr) KERNEL32.GetCommProperties
@ stdcall GetCommState(long ptr) KERNEL32.GetCommState
@ stdcall GetCommTimeouts(long ptr) KERNEL32.GetCommTimeouts
@ stdcall GetCommandLineA() KERNEL32.GetCommandLineA
@ stdcall GetCommandLineW() KERNEL32.GetCommandLineW
@ stdcall GetCompressedFileSizeA(long ptr) KERNEL32.GetCompressedFileSizeA
@ stdcall GetCompressedFileSizeW(long ptr) KERNEL32.GetCompressedFileSizeW
@ stdcall GetComputerNameA(ptr ptr) KERNEL32.GetComputerNameA
@ stdcall GetComputerNameExA(long ptr ptr) KERNEL32.GetComputerNameExA
@ stdcall GetComputerNameExW(long ptr ptr) KERNEL32.GetComputerNameExW
@ stdcall GetComputerNameW(ptr ptr) KERNEL32.GetComputerNameW
@ stdcall GetConsoleAliasA(str str long str) KERNEL32.GetConsoleAliasA
@ stdcall GetConsoleAliasExesA(str long) KERNEL32.GetConsoleAliasExesA
@ stdcall GetConsoleAliasExesLengthA() KERNEL32.GetConsoleAliasExesLengthA
@ stdcall GetConsoleAliasExesLengthW() KERNEL32.GetConsoleAliasExesLengthW
@ stdcall GetConsoleAliasExesW(wstr long) KERNEL32.GetConsoleAliasExesW
@ stdcall GetConsoleAliasW(wstr ptr long wstr) KERNEL32.GetConsoleAliasW
@ stdcall GetConsoleAliasesA(str long str) KERNEL32.GetConsoleAliasesA
@ stdcall GetConsoleAliasesLengthA(str) KERNEL32.GetConsoleAliasesLengthA
@ stdcall GetConsoleAliasesLengthW(wstr) KERNEL32.GetConsoleAliasesLengthW
@ stdcall GetConsoleAliasesW(wstr long wstr) KERNEL32.GetConsoleAliasesW
@ stdcall GetConsoleCP() KERNEL32.GetConsoleCP
@ stdcall GetConsoleCharType(long long ptr) KERNEL32.GetConsoleCharType
@ stdcall GetConsoleCommandHistoryA(long long long) KERNEL32.GetConsoleCommandHistoryA
@ stdcall GetConsoleCommandHistoryLengthA(long) KERNEL32.GetConsoleCommandHistoryLengthA
@ stdcall GetConsoleCommandHistoryLengthW(long) KERNEL32.GetConsoleCommandHistoryLengthW
@ stdcall GetConsoleCommandHistoryW(long long long) KERNEL32.GetConsoleCommandHistoryW
@ stdcall GetConsoleCursorInfo(long ptr) KERNEL32.GetConsoleCursorInfo
@ stdcall GetConsoleCursorMode(long ptr ptr) KERNEL32.GetConsoleCursorMode
@ stdcall GetConsoleDisplayMode(ptr) KERNEL32.GetConsoleDisplayMode
@ stdcall GetConsoleFontInfo(long long long ptr) KERNEL32.GetConsoleFontInfo
@ stdcall GetConsoleFontSize(long long) KERNEL32.GetConsoleFontSize
@ stdcall GetConsoleHardwareState(long long ptr) KERNEL32.GetConsoleHardwareState
@ stdcall GetConsoleInputExeNameA(long ptr) KERNEL32.GetConsoleInputExeNameA
@ stdcall GetConsoleInputExeNameW(long ptr) KERNEL32.GetConsoleInputExeNameW
@ stdcall GetConsoleInputWaitHandle() KERNEL32.GetConsoleInputWaitHandle
@ stdcall GetConsoleKeyboardLayoutNameA(ptr) KERNEL32.GetConsoleKeyboardLayoutNameA
@ stdcall GetConsoleKeyboardLayoutNameW(ptr) KERNEL32.GetConsoleKeyboardLayoutNameW
@ stdcall GetConsoleMode(long ptr) KERNEL32.GetConsoleMode
@ stdcall GetConsoleNlsMode(long ptr) KERNEL32.GetConsoleNlsMode
@ stdcall GetConsoleOutputCP() KERNEL32.GetConsoleOutputCP
@ stdcall GetConsoleProcessList(ptr long) KERNEL32.GetConsoleProcessList
@ stdcall GetConsoleScreenBufferInfo(long ptr) KERNEL32.GetConsoleScreenBufferInfo
@ stdcall GetConsoleSelectionInfo(ptr) KERNEL32.GetConsoleSelectionInfo
@ stdcall GetConsoleTitleA(ptr long) KERNEL32.GetConsoleTitleA
@ stdcall GetConsoleTitleW(ptr long) KERNEL32.GetConsoleTitleW
@ stdcall GetConsoleWindow() KERNEL32.GetConsoleWindow
@ stdcall GetCurrencyFormatA(long long str ptr str long) KERNEL32.GetCurrencyFormatA
@ stdcall GetCurrencyFormatW(long long str ptr str long) KERNEL32.GetCurrencyFormatW
@ stdcall GetCurrentActCtx(ptr) KERNEL32.GetCurrentActCtx
@ stdcall GetCurrentConsoleFont(long long ptr) KERNEL32.GetCurrentConsoleFont
@ stdcall GetCurrentDirectoryA(long ptr) KERNEL32.GetCurrentDirectoryA
@ stdcall GetCurrentDirectoryW(long ptr) KERNEL32.GetCurrentDirectoryW
@ stdcall -norelay GetCurrentProcess() KERNEL32.GetCurrentProcess
@ stdcall -norelay GetCurrentProcessId() KERNEL32.GetCurrentProcessId
@ stdcall GetCurrentProcessorNumber() ntdll.RtlGetCurrentProcessorNumber
@ stdcall -norelay GetCurrentThread() KERNEL32.GetCurrentThread
@ stdcall -norelay GetCurrentThreadId() KERNEL32.GetCurrentThreadId
@ stdcall GetDateFormatA(long long ptr str ptr long) KERNEL32.GetDateFormatA
@ stdcall GetDateFormatW(long long ptr wstr ptr long) KERNEL32.GetDateFormatW
@ stdcall GetDefaultCommConfigA(str ptr long) KERNEL32.GetDefaultCommConfigA
@ stdcall GetDefaultCommConfigW(wstr ptr long) KERNEL32.GetDefaultCommConfigW
@ stdcall -version=0x501-0x502 GetDefaultSortkeySize(ptr) KERNEL32.GetDefaultSortkeySize
@ stdcall GetDevicePowerState(long ptr) KERNEL32.GetDevicePowerState
@ stdcall GetDiskFreeSpaceA(str ptr ptr ptr ptr) KERNEL32.GetDiskFreeSpaceA
@ stdcall GetDiskFreeSpaceExA (str ptr ptr ptr) KERNEL32.GetDiskFreeSpaceExA
@ stdcall GetDiskFreeSpaceExW (wstr ptr ptr ptr) KERNEL32.GetDiskFreeSpaceExW
@ stdcall GetDiskFreeSpaceW(wstr ptr ptr ptr ptr) KERNEL32.GetDiskFreeSpaceW
@ stdcall GetDllDirectoryA(long ptr) KERNEL32.GetDllDirectoryA
@ stdcall GetDllDirectoryW(long ptr) KERNEL32.GetDllDirectoryW
@ stdcall GetDriveTypeA(str) KERNEL32.GetDriveTypeA
@ stdcall GetDriveTypeW(wstr) KERNEL32.GetDriveTypeW
@ stdcall GetEnvironmentStrings() KERNEL32.GetEnvironmentStrings
@ stdcall GetEnvironmentStringsA()  KERNEL32.GetEnvironmentStringsA
@ stdcall GetEnvironmentStringsW() KERNEL32.GetEnvironmentStringsW
@ stdcall GetEnvironmentVariableA(str ptr long) KERNEL32.GetEnvironmentVariableA
@ stdcall GetEnvironmentVariableW(wstr ptr long) KERNEL32.GetEnvironmentVariableW
@ stdcall GetExitCodeProcess(long ptr) KERNEL32.GetExitCodeProcess
@ stdcall GetExitCodeThread(long ptr) KERNEL32.GetExitCodeThread
@ stdcall GetExpandedNameA(str ptr) KERNEL32.GetExpandedNameA
@ stdcall GetExpandedNameW(wstr ptr) KERNEL32.GetExpandedNameW
@ stdcall GetFileAttributesA(str) KERNEL32.GetFileAttributesA
@ stdcall GetFileAttributesExA(str long ptr) KERNEL32.GetFileAttributesExA
@ stdcall GetFileAttributesExW(wstr long ptr) KERNEL32.GetFileAttributesExW
@ stdcall GetFileAttributesW(wstr) KERNEL32.GetFileAttributesW
@ stdcall GetFileInformationByHandle(long ptr) KERNEL32.GetFileInformationByHandle
@ stdcall GetFileSize(long ptr) KERNEL32.GetFileSize
@ stdcall GetFileSizeEx(long ptr) KERNEL32.GetFileSizeEx
@ stdcall GetFileTime(long ptr ptr ptr) KERNEL32.GetFileTime
@ stdcall GetFileType(long) KERNEL32.GetFileType
@ stdcall GetFirmwareEnvironmentVariableA(str str ptr long) KERNEL32.GetFirmwareEnvironmentVariableA
@ stdcall GetFirmwareEnvironmentVariableW(wstr wstr ptr long) KERNEL32.GetFirmwareEnvironmentVariableW
@ stdcall GetFullPathNameA(str long ptr ptr) KERNEL32.GetFullPathNameA
@ stdcall GetFullPathNameW(wstr long ptr ptr) KERNEL32.GetFullPathNameW
@ stdcall GetGeoInfoA(long long ptr long long) KERNEL32.GetGeoInfoA
@ stdcall GetGeoInfoW(long long ptr long long) KERNEL32.GetGeoInfoW
@ stdcall -i386 GetHandleContext(long) KERNEL32.GetHandleContext
@ stdcall GetHandleInformation(long ptr) KERNEL32.GetHandleInformation
@ stdcall GetLargePageMinimum() KERNEL32.GetLargePageMinimum
@ stdcall GetLargestConsoleWindowSize(long) KERNEL32.GetLargestConsoleWindowSize
@ stdcall GetLastError() ntdll.RtlGetLastWin32Error
@ stdcall -version=0x500-0x502 GetLinguistLangSize(ptr) KERNEL32.GetLinguistLangSize
@ stdcall GetLocalTime(ptr) KERNEL32.GetLocalTime
@ stdcall GetLocaleInfoA(long long ptr long) KERNEL32.GetLocaleInfoA
@ stdcall GetLocaleInfoW(long long ptr long) KERNEL32.GetLocaleInfoW
@ stdcall GetLogicalDriveStringsA(long ptr) KERNEL32.GetLogicalDriveStringsA
@ stdcall GetLogicalDriveStringsW(long ptr) KERNEL32.GetLogicalDriveStringsW
@ stdcall GetLogicalDrives() KERNEL32.GetLogicalDrives
@ stdcall GetLogicalProcessorInformation(ptr ptr) KERNEL32.GetLogicalProcessorInformation
@ stdcall GetLongPathNameA (str long long) KERNEL32.GetLongPathNameA
@ stdcall GetLongPathNameW (wstr long long) KERNEL32.GetLongPathNameW
@ stdcall GetMailslotInfo(long ptr ptr ptr ptr) KERNEL32.GetMailslotInfo
@ stdcall GetModuleFileNameA(long ptr long) KERNEL32.GetModuleFileNameA
@ stdcall GetModuleFileNameW(long ptr long) KERNEL32.GetModuleFileNameW
@ stdcall GetModuleHandleA(str) KERNEL32.GetModuleHandleA
@ stdcall GetModuleHandleExA(long ptr ptr) KERNEL32.GetModuleHandleExA
@ stdcall GetModuleHandleExW(long ptr ptr) KERNEL32.GetModuleHandleExW
@ stdcall GetModuleHandleW(wstr) KERNEL32.GetModuleHandleW
@ stdcall GetNLSVersion(long long ptr) KERNEL32.GetNLSVersion
@ stdcall GetNamedPipeHandleStateA(long ptr ptr ptr ptr str long) KERNEL32.GetNamedPipeHandleStateA
@ stdcall GetNamedPipeHandleStateW(long ptr ptr ptr ptr wstr long) KERNEL32.GetNamedPipeHandleStateW
@ stdcall GetNamedPipeInfo(long ptr ptr ptr ptr) KERNEL32.GetNamedPipeInfo
@ stdcall GetNativeSystemInfo(ptr) KERNEL32.GetNativeSystemInfo
@ stdcall GetNextVDMCommand(long) KERNEL32.GetNextVDMCommand
@ stdcall -version=0x500-0x502 GetNlsSectionName(long long long str str long) KERNEL32.GetNlsSectionName
@ stdcall GetNumaAvailableMemoryNode(long ptr) KERNEL32.GetNumaAvailableMemoryNode
@ stdcall GetNumaHighestNodeNumber(ptr) KERNEL32.GetNumaHighestNodeNumber
@ stdcall GetNumaNodeProcessorMask(long ptr) KERNEL32.GetNumaNodeProcessorMask
@ stdcall GetNumaProcessorNode(long ptr) KERNEL32.GetNumaProcessorNode
@ stdcall GetNumberFormatA(long long str ptr ptr long) KERNEL32.GetNumberFormatA
@ stdcall GetNumberFormatW(long long wstr ptr ptr long) KERNEL32.GetNumberFormatW
@ stdcall GetNumberOfConsoleFonts() KERNEL32.GetNumberOfConsoleFonts
@ stdcall GetNumberOfConsoleInputEvents(long ptr) KERNEL32.GetNumberOfConsoleInputEvents
@ stdcall GetNumberOfConsoleMouseButtons(ptr) KERNEL32.GetNumberOfConsoleMouseButtons
@ stdcall GetOEMCP() KERNEL32.GetOEMCP
@ stdcall GetOverlappedResult(long ptr ptr long) KERNEL32.GetOverlappedResult
@ stdcall GetPriorityClass(long) KERNEL32.GetPriorityClass
@ stdcall GetPrivateProfileIntA(str str long str) KERNEL32.GetPrivateProfileIntA
@ stdcall GetPrivateProfileIntW(wstr wstr long wstr) KERNEL32.GetPrivateProfileIntW
@ stdcall GetPrivateProfileSectionA(str ptr long str) KERNEL32.GetPrivateProfileSectionA
@ stdcall GetPrivateProfileSectionNamesA(ptr long str) KERNEL32.GetPrivateProfileSectionNamesA
@ stdcall GetPrivateProfileSectionNamesW(ptr long wstr) KERNEL32.GetPrivateProfileSectionNamesW
@ stdcall GetPrivateProfileSectionW(wstr ptr long wstr) KERNEL32.GetPrivateProfileSectionW
@ stdcall GetPrivateProfileStringA(str str str ptr long str) KERNEL32.GetPrivateProfileStringA
@ stdcall GetPrivateProfileStringW(wstr wstr wstr ptr long wstr) KERNEL32.GetPrivateProfileStringW
@ stdcall GetPrivateProfileStructA (str str ptr long str) KERNEL32.GetPrivateProfileStructA
@ stdcall GetPrivateProfileStructW(wstr wstr ptr long wstr) KERNEL32.GetPrivateProfileStructW
@ stdcall GetProcAddress(long str) KERNEL32.GetProcAddress
@ stdcall GetProcessAffinityMask(long ptr ptr) KERNEL32.GetProcessAffinityMask
@ stdcall GetProcessHandleCount(long ptr) KERNEL32.GetProcessHandleCount
@ stdcall -norelay GetProcessHeap() KERNEL32.GetProcessHeap
@ stdcall GetProcessHeaps(long ptr) KERNEL32.GetProcessHeaps
@ stdcall GetProcessId(long) KERNEL32.GetProcessId
@ stdcall GetProcessIdOfThread(ptr) KERNEL32.GetProcessIdOfThread
@ stdcall GetProcessIoCounters(long ptr) KERNEL32.GetProcessIoCounters
@ stdcall GetProcessPriorityBoost(long ptr) KERNEL32.GetProcessPriorityBoost
@ stdcall GetProcessShutdownParameters(ptr ptr) KERNEL32.GetProcessShutdownParameters
@ stdcall GetProcessTimes(long ptr ptr ptr ptr) KERNEL32.GetProcessTimes
@ stdcall GetProcessVersion(long) KERNEL32.GetProcessVersion
@ stdcall GetProcessWorkingSetSize(long ptr ptr) KERNEL32.GetProcessWorkingSetSize
@ stdcall GetProcessWorkingSetSizeEx(long ptr ptr long) KERNEL32.GetProcessWorkingSetSizeEx
@ stdcall GetProfileIntA(str str long) KERNEL32.GetProfileIntA
@ stdcall GetProfileIntW(wstr wstr long) KERNEL32.GetProfileIntW
@ stdcall GetProfileSectionA(str ptr long) KERNEL32.GetProfileSectionA
@ stdcall GetProfileSectionW(wstr ptr long) KERNEL32.GetProfileSectionW
@ stdcall GetProfileStringA(str str str ptr long) KERNEL32.GetProfileStringA
@ stdcall GetProfileStringW(wstr wstr wstr ptr long) KERNEL32.GetProfileStringW
@ stdcall GetQueuedCompletionStatus(long ptr ptr ptr long) KERNEL32.GetQueuedCompletionStatus
@ stdcall GetShortPathNameA(str ptr long) KERNEL32.GetShortPathNameA
@ stdcall GetShortPathNameW(wstr ptr long) KERNEL32.GetShortPathNameW
@ stdcall GetStartupInfoA(ptr) KERNEL32.GetStartupInfoA
@ stdcall GetStartupInfoW(ptr) KERNEL32.GetStartupInfoW
@ stdcall GetStdHandle(long) KERNEL32.GetStdHandle
@ stdcall GetStringTypeA(long long str long ptr) KERNEL32.GetStringTypeA
@ stdcall GetStringTypeExA(long long str long ptr) KERNEL32.GetStringTypeExA
@ stdcall GetStringTypeExW(long long wstr long ptr) KERNEL32.GetStringTypeExW
@ stdcall GetStringTypeW(long wstr long ptr) KERNEL32.GetStringTypeW
@ stdcall GetSystemDefaultLCID() KERNEL32.GetSystemDefaultLCID
@ stdcall GetSystemDefaultLangID() KERNEL32.GetSystemDefaultLangID
@ stdcall GetSystemDefaultUILanguage() KERNEL32.GetSystemDefaultUILanguage
@ stdcall GetSystemDirectoryA(ptr long) KERNEL32.GetSystemDirectoryA
@ stdcall GetSystemDirectoryW(ptr long) KERNEL32.GetSystemDirectoryW
@ stdcall GetSystemFileCacheSize(ptr ptr ptr) KERNEL32.GetSystemFileCacheSize
@ stdcall GetSystemFirmwareTable(long long ptr long) KERNEL32.GetSystemFirmwareTable
@ stdcall GetSystemInfo(ptr) KERNEL32.GetSystemInfo
@ stdcall GetSystemPowerStatus(ptr) KERNEL32.GetSystemPowerStatus
@ stdcall GetSystemRegistryQuota(ptr ptr) KERNEL32.GetSystemRegistryQuota
@ stdcall GetSystemTime(ptr) KERNEL32.GetSystemTime
@ stdcall GetSystemTimeAdjustment(ptr ptr ptr) KERNEL32.GetSystemTimeAdjustment
@ stdcall GetSystemTimeAsFileTime(ptr) KERNEL32.GetSystemTimeAsFileTime
@ stdcall GetSystemTimes(ptr ptr ptr) KERNEL32.GetSystemTimes
@ stdcall GetSystemWindowsDirectoryA(ptr long) KERNEL32.GetSystemWindowsDirectoryA
@ stdcall GetSystemWindowsDirectoryW(ptr long) KERNEL32.GetSystemWindowsDirectoryW
@ stdcall GetSystemWow64DirectoryA(ptr long) KERNEL32.GetSystemWow64DirectoryA
@ stdcall GetSystemWow64DirectoryW(ptr long) KERNEL32.GetSystemWow64DirectoryW
@ stdcall GetTapeParameters(ptr long ptr ptr) KERNEL32.GetTapeParameters
@ stdcall GetTapePosition(ptr long ptr ptr ptr) KERNEL32.GetTapePosition
@ stdcall GetTapeStatus(ptr) KERNEL32.GetTapeStatus
@ stdcall GetTempFileNameA(str str long ptr) KERNEL32.GetTempFileNameA
@ stdcall GetTempFileNameW(wstr wstr long ptr) KERNEL32.GetTempFileNameW
@ stdcall GetTempPathA(long ptr) KERNEL32.GetTempPathA
@ stdcall GetTempPathW(long ptr) KERNEL32.GetTempPathW
@ stdcall GetThreadContext(long ptr) KERNEL32.GetThreadContext
@ stdcall GetThreadIOPendingFlag(long ptr) KERNEL32.GetThreadIOPendingFlag
@ stdcall GetThreadId(ptr) KERNEL32.GetThreadId
@ stdcall GetThreadLocale() KERNEL32.GetThreadLocale
@ stdcall GetThreadPriority(long) KERNEL32.GetThreadPriority
@ stdcall GetThreadPriorityBoost(long ptr) KERNEL32.GetThreadPriorityBoost
@ stdcall GetThreadSelectorEntry(long long ptr) KERNEL32.GetThreadSelectorEntry
@ stdcall GetThreadTimes(long ptr ptr ptr ptr) KERNEL32.GetThreadTimes
@ stdcall GetTickCount() KERNEL32.GetTickCount
@ stdcall GetTimeFormatA(long long ptr str ptr long) KERNEL32.GetTimeFormatA
@ stdcall GetTimeFormatW(long long ptr wstr ptr long) KERNEL32.GetTimeFormatW
@ stdcall GetTimeZoneInformation(ptr) KERNEL32.GetTimeZoneInformation
@ stdcall GetUserDefaultLCID() KERNEL32.GetUserDefaultLCID
@ stdcall GetUserDefaultLangID() KERNEL32.GetUserDefaultLangID
@ stdcall GetUserDefaultUILanguage() KERNEL32.GetUserDefaultUILanguage
@ stdcall GetUserGeoID(long) KERNEL32.GetUserGeoID
@ stdcall GetVDMCurrentDirectories(long long) KERNEL32.GetVDMCurrentDirectories
@ stdcall GetVersion() KERNEL32.GetVersion
@ stdcall GetVersionExA(ptr) KERNEL32.GetVersionExA
@ stdcall GetVersionExW(ptr) KERNEL32.GetVersionExW
@ stdcall GetVolumeInformationA(str ptr long ptr ptr ptr ptr long) KERNEL32.GetVolumeInformationA
@ stdcall GetVolumeInformationW(wstr ptr long ptr ptr ptr ptr long) KERNEL32.GetVolumeInformationW
@ stdcall GetVolumeNameForVolumeMountPointA(str ptr long) KERNEL32.GetVolumeNameForVolumeMountPointA
@ stdcall GetVolumeNameForVolumeMountPointW(wstr ptr long) KERNEL32.GetVolumeNameForVolumeMountPointW
@ stdcall GetVolumePathNameA(str ptr long) KERNEL32.GetVolumePathNameA
@ stdcall GetVolumePathNameW(wstr ptr long) KERNEL32.GetVolumePathNameW
@ stdcall GetVolumePathNamesForVolumeNameA(str str long ptr) KERNEL32.GetVolumePathNamesForVolumeNameA
@ stdcall GetVolumePathNamesForVolumeNameW(wstr wstr long ptr) KERNEL32.GetVolumePathNamesForVolumeNameW
@ stdcall GetWindowsDirectoryA(ptr long) KERNEL32.GetWindowsDirectoryA
@ stdcall GetWindowsDirectoryW(ptr long) KERNEL32.GetWindowsDirectoryW
@ stdcall GetWriteWatch(long ptr long ptr ptr ptr) KERNEL32.GetWriteWatch
@ stdcall GlobalAddAtomA(str) KERNEL32.GlobalAddAtomA
@ stdcall GlobalAddAtomW(wstr) KERNEL32.GlobalAddAtomW
@ stdcall GlobalAlloc(long long) KERNEL32.GlobalAlloc
@ stdcall GlobalCompact(long) KERNEL32.GlobalCompact
@ stdcall GlobalDeleteAtom(long) KERNEL32.GlobalDeleteAtom
@ stdcall GlobalFindAtomA(str) KERNEL32.GlobalFindAtomA
@ stdcall GlobalFindAtomW(wstr) KERNEL32.GlobalFindAtomW
@ stdcall GlobalFix(long) KERNEL32.GlobalFix
@ stdcall GlobalFlags(long) KERNEL32.GlobalFlags
@ stdcall GlobalFree(long) KERNEL32.GlobalFree
@ stdcall GlobalGetAtomNameA(long ptr long) KERNEL32.GlobalGetAtomNameA
@ stdcall GlobalGetAtomNameW(long ptr long) KERNEL32.GlobalGetAtomNameW
@ stdcall GlobalHandle(ptr) KERNEL32.GlobalHandle
@ stdcall GlobalLock(long) KERNEL32.GlobalLock
@ stdcall GlobalMemoryStatus(ptr) KERNEL32.GlobalMemoryStatus
@ stdcall GlobalMemoryStatusEx(ptr) KERNEL32.GlobalMemoryStatusEx
@ stdcall GlobalReAlloc(long long long) KERNEL32.GlobalReAlloc
@ stdcall GlobalSize(long) KERNEL32.GlobalSize
@ stdcall GlobalUnWire(long) KERNEL32.GlobalUnWire
@ stdcall GlobalUnfix(long) KERNEL32.GlobalUnfix
@ stdcall GlobalUnlock(long) KERNEL32.GlobalUnlock
@ stdcall GlobalWire(long) KERNEL32.GlobalWire
@ stdcall Heap32First(ptr long long) KERNEL32.Heap32First
@ stdcall Heap32ListFirst(long ptr) KERNEL32.Heap32ListFirst
@ stdcall Heap32ListNext(long ptr) KERNEL32.Heap32ListNext
@ stdcall Heap32Next(ptr) KERNEL32.Heap32Next
@ stdcall HeapAlloc(long long long) ntdll.RtlAllocateHeap
@ stdcall HeapCompact(long long) KERNEL32.HeapCompact
@ stdcall HeapCreate(long long long) KERNEL32.HeapCreate
@ stdcall -version=0x351-0x502 HeapCreateTagsW(long long wstr wstr) KERNEL32.HeapCreateTagsW
@ stdcall HeapDestroy(long) KERNEL32.HeapDestroy
@ stdcall -version=0x351-0x502 HeapExtend(long long ptr long) KERNEL32.HeapExtend
@ stdcall HeapFree(long long long) ntdll.RtlFreeHeap
@ stdcall HeapLock(long) KERNEL32.HeapLock
@ stdcall HeapQueryInformation(long long ptr long ptr) KERNEL32.HeapQueryInformation
@ stdcall -version=0x351-0x502 HeapQueryTagW(long long long long ptr) KERNEL32.HeapQueryTagW
@ stdcall HeapReAlloc(long long ptr long) ntdll.RtlReAllocateHeap
@ stdcall HeapSetInformation(ptr long ptr long) KERNEL32.HeapSetInformation
@ stdcall HeapSize(long long ptr) ntdll.RtlSizeHeap
@ stdcall HeapSummary(long long ptr) KERNEL32.HeapSummary
@ stdcall HeapUnlock(long) KERNEL32.HeapUnlock
@ stdcall -version=0x351-0x502 HeapUsage(long long long long ptr) KERNEL32.HeapUsage
@ stdcall HeapValidate(long long ptr) KERNEL32.HeapValidate
@ stdcall HeapWalk(long ptr) KERNEL32.HeapWalk
@ stdcall InitAtomTable(long) KERNEL32.InitAtomTable
@ stdcall InitializeCriticalSection(ptr) KERNEL32.InitializeCriticalSection
@ stdcall InitializeCriticalSectionAndSpinCount(ptr long) KERNEL32.InitializeCriticalSectionAndSpinCount
@ stdcall InitializeSListHead(ptr) ntdll.RtlInitializeSListHead
@ stdcall -arch=i386 -ret64 InterlockedCompareExchange64(ptr double double) ntdll.RtlInterlockedCompareExchange64
@ stdcall -arch=i386 InterlockedCompareExchange (ptr long long) KERNEL32.InterlockedCompareExchange
@ stdcall -arch=i386 InterlockedDecrement(ptr) KERNEL32.InterlockedDecrement
@ stdcall -arch=i386 InterlockedExchange(ptr long) KERNEL32.InterlockedExchange
@ stdcall -arch=i386 InterlockedExchangeAdd(ptr long) KERNEL32.InterlockedExchangeAdd
@ stdcall InterlockedFlushSList(ptr) ntdll.RtlInterlockedFlushSList
@ stdcall -arch=i386 InterlockedIncrement(ptr) KERNEL32.InterlockedIncrement
@ stdcall InterlockedPopEntrySList(ptr) ntdll.RtlInterlockedPopEntrySList
@ stdcall InterlockedPushEntrySList(ptr ptr) ntdll.RtlInterlockedPushEntrySList
@ stdcall InvalidateConsoleDIBits(long long) KERNEL32.InvalidateConsoleDIBits
@ stdcall IsBadCodePtr(ptr) KERNEL32.IsBadCodePtr
@ stdcall IsBadHugeReadPtr(ptr long) KERNEL32.IsBadHugeReadPtr
@ stdcall IsBadHugeWritePtr(ptr long) KERNEL32.IsBadHugeWritePtr
@ stdcall IsBadReadPtr(ptr long) KERNEL32.IsBadReadPtr
@ stdcall IsBadStringPtrA(ptr long) KERNEL32.IsBadStringPtrA
@ stdcall IsBadStringPtrW(ptr long) KERNEL32.IsBadStringPtrW
@ stdcall IsBadWritePtr(ptr long) KERNEL32.IsBadWritePtr
@ stdcall IsDBCSLeadByte(long) KERNEL32.IsDBCSLeadByte
@ stdcall IsDBCSLeadByteEx(long long) KERNEL32.IsDBCSLeadByteEx
@ stdcall IsDebuggerPresent() KERNEL32.IsDebuggerPresent
@ stdcall IsNLSDefinedString(long long ptr long long) KERNEL32.IsNLSDefinedString
@ stdcall IsProcessInJob(long long ptr) KERNEL32.IsProcessInJob
@ stdcall IsProcessorFeaturePresent(long) KERNEL32.IsProcessorFeaturePresent
@ stdcall IsSystemResumeAutomatic() KERNEL32.IsSystemResumeAutomatic
@ stdcall IsTimeZoneRedirectionEnabled() KERNEL32.IsTimeZoneRedirectionEnabled
@ stdcall IsValidCodePage(long) KERNEL32.IsValidCodePage
@ stdcall IsValidLanguageGroup(long long) KERNEL32.IsValidLanguageGroup
@ stdcall IsValidLocale(long long) KERNEL32.IsValidLocale
@ stdcall -version=0x501-0x502 IsValidUILanguage(long) KERNEL32.IsValidUILanguage
@ stdcall IsWow64Process(ptr ptr) KERNEL32.IsWow64Process
@ stdcall LCMapStringA(long long str long ptr long) KERNEL32.LCMapStringA
@ stdcall LCMapStringW(long long wstr long ptr long) KERNEL32.LCMapStringW
@ stdcall LZClose(long) KERNEL32.LZClose
@ stdcall LZCloseFile(long) KERNEL32.LZCloseFile
@ stdcall LZCopy(long long) KERNEL32.LZCopy
@ stdcall LZCreateFileW(ptr long long long ptr) KERNEL32.LZCreateFileW
@ stdcall LZDone() KERNEL32.LZDone
@ stdcall LZInit(long) KERNEL32.LZInit
@ stdcall LZOpenFileA(str ptr long) KERNEL32.LZOpenFileA
@ stdcall LZOpenFileW(wstr ptr long) KERNEL32.LZOpenFileW
@ stdcall LZRead(long str long) KERNEL32.LZRead
@ stdcall LZSeek(long long long) KERNEL32.LZSeek
@ stdcall LZStart() KERNEL32.LZStart
@ stdcall LeaveCriticalSection(ptr) ntdll.RtlLeaveCriticalSection
@ stdcall LoadLibraryA(str) KERNEL32.LoadLibraryA
@ stdcall LoadLibraryExA( str long long) KERNEL32.LoadLibraryExA
@ stdcall LoadLibraryExW(wstr long long) KERNEL32.LoadLibraryExW
@ stdcall LoadLibraryW(wstr) KERNEL32.LoadLibraryW
@ stdcall LoadModule(str ptr) KERNEL32.LoadModule
@ stdcall LoadResource(long long) KERNEL32.LoadResource
@ stdcall LocalAlloc(long long) KERNEL32.LocalAlloc
@ stdcall LocalCompact(long) KERNEL32.LocalCompact
@ stdcall LocalFileTimeToFileTime(ptr ptr) KERNEL32.LocalFileTimeToFileTime
@ stdcall LocalFlags(long) KERNEL32.LocalFlags
@ stdcall LocalFree(long) KERNEL32.LocalFree
@ stdcall LocalHandle(ptr) KERNEL32.LocalHandle
@ stdcall LocalLock(long) KERNEL32.LocalLock
@ stdcall LocalReAlloc(long long long) KERNEL32.LocalReAlloc
@ stdcall LocalShrink(long long) KERNEL32.LocalShrink
@ stdcall LocalSize(long) KERNEL32.LocalSize
@ stdcall LocalUnlock(long) KERNEL32.LocalUnlock
@ stdcall LockFile(long long long long long) KERNEL32.LockFile
@ stdcall LockFileEx(long long long long long ptr) KERNEL32.LockFileEx
@ stdcall LockResource(long) KERNEL32.LockResource
@ stdcall MapUserPhysicalPages(ptr long ptr) KERNEL32.MapUserPhysicalPages
@ stdcall MapUserPhysicalPagesScatter(ptr long ptr) KERNEL32.MapUserPhysicalPagesScatter
@ stdcall MapViewOfFile(long long long long long) KERNEL32.MapViewOfFile
@ stdcall MapViewOfFileEx(long long long long long ptr) KERNEL32.MapViewOfFileEx
@ stdcall Module32First(long ptr) KERNEL32.Module32First
@ stdcall Module32FirstW(long ptr) KERNEL32.Module32FirstW
@ stdcall Module32Next(long ptr) KERNEL32.Module32Next
@ stdcall Module32NextW(long ptr) KERNEL32.Module32NextW
@ stdcall MoveFileA(str str) KERNEL32.MoveFileA
@ stdcall MoveFileExA(str str long) KERNEL32.MoveFileExA
@ stdcall MoveFileExW(wstr wstr long) KERNEL32.MoveFileExW
@ stdcall MoveFileW(wstr wstr) KERNEL32.MoveFileW
@ stdcall MoveFileWithProgressA(str str ptr ptr long) KERNEL32.MoveFileWithProgressA
@ stdcall MoveFileWithProgressW(wstr wstr ptr ptr long) KERNEL32.MoveFileWithProgressW
@ stdcall MulDiv(long long long) KERNEL32.MulDiv
@ stdcall MultiByteToWideChar(long long str long ptr long) KERNEL32.MultiByteToWideChar
@ stdcall NeedCurrentDirectoryForExePathA(str) KERNEL32.NeedCurrentDirectoryForExePathA
@ stdcall NeedCurrentDirectoryForExePathW(wstr) KERNEL32.NeedCurrentDirectoryForExePathW
@ stdcall -version=0x500-0x600 NlsConvertIntegerToString(long long long wstr long) KERNEL32.NlsConvertIntegerToString
@ stdcall NlsGetCacheUpdateCount() KERNEL32.NlsGetCacheUpdateCount
@ stdcall -version=0x500-0x502 NlsResetProcessLocale() KERNEL32.NlsResetProcessLocale
@ stdcall OpenConsoleW(wstr long long long) KERNEL32.OpenConsoleW
@ stdcall -version=0x500-0x502 OpenDataFile(long long) KERNEL32.OpenDataFile
@ stdcall OpenEventA(long long str) KERNEL32.OpenEventA
@ stdcall OpenEventW(long long wstr) KERNEL32.OpenEventW
@ stdcall OpenFile(str ptr long) KERNEL32.OpenFile
@ stdcall OpenFileMappingA(long long str) KERNEL32.OpenFileMappingA
@ stdcall OpenFileMappingW(long long wstr) KERNEL32.OpenFileMappingW
@ stdcall OpenJobObjectA(long long str) KERNEL32.OpenJobObjectA
@ stdcall OpenJobObjectW(long long wstr) KERNEL32.OpenJobObjectW
@ stdcall OpenMutexA(long long str) KERNEL32.OpenMutexA
@ stdcall OpenMutexW(long long wstr) KERNEL32.OpenMutexW
@ stdcall OpenProcess(long long long) KERNEL32.OpenProcess
@ stdcall OpenProfileUserMapping() KERNEL32.OpenProfileUserMapping
@ stdcall OpenSemaphoreA(long long str) KERNEL32.OpenSemaphoreA
@ stdcall OpenSemaphoreW(long long wstr) KERNEL32.OpenSemaphoreW
@ stdcall OpenThread(long long long) KERNEL32.OpenThread
@ stdcall OpenWaitableTimerA(long long str) KERNEL32.OpenWaitableTimerA
@ stdcall OpenWaitableTimerW(long long wstr) KERNEL32.OpenWaitableTimerW
@ stdcall OutputDebugStringA(str) KERNEL32.OutputDebugStringA
@ stdcall OutputDebugStringW(wstr) KERNEL32.OutputDebugStringW
@ stdcall PeekConsoleInputA(ptr ptr long ptr) KERNEL32.PeekConsoleInputA
@ stdcall PeekConsoleInputW(ptr ptr long ptr) KERNEL32.PeekConsoleInputW
@ stdcall PeekNamedPipe(long ptr long ptr ptr ptr) KERNEL32.PeekNamedPipe
@ stdcall PostQueuedCompletionStatus(long long ptr ptr) KERNEL32.PostQueuedCompletionStatus
@ stdcall PrepareTape(ptr long long) KERNEL32.PrepareTape
@ stdcall PrivCopyFileExW(wstr wstr ptr ptr long long) KERNEL32.PrivCopyFileExW
@ stdcall PrivMoveFileIdentityW(long long long) KERNEL32.PrivMoveFileIdentityW
@ stdcall Process32First (ptr ptr) KERNEL32.Process32First
@ stdcall Process32FirstW (ptr ptr) KERNEL32.Process32FirstW
@ stdcall Process32Next (ptr ptr) KERNEL32.Process32Next
@ stdcall Process32NextW (ptr ptr) KERNEL32.Process32NextW
@ stdcall ProcessIdToSessionId(long ptr) KERNEL32.ProcessIdToSessionId
@ stdcall PulseEvent(long) KERNEL32.PulseEvent
@ stdcall PurgeComm(long long) KERNEL32.PurgeComm
@ stdcall QueryActCtxW(long ptr ptr long ptr long ptr) KERNEL32.QueryActCtxW
@ stdcall QueryDepthSList(ptr) ntdll.RtlQueryDepthSList
@ stdcall QueryDosDeviceA(str ptr long) KERNEL32.QueryDosDeviceA
@ stdcall QueryDosDeviceW(wstr ptr long) KERNEL32.QueryDosDeviceW
@ stdcall QueryInformationJobObject(long long ptr long ptr) KERNEL32.QueryInformationJobObject
@ stdcall QueryMemoryResourceNotification(ptr ptr) KERNEL32.QueryMemoryResourceNotification
@ stdcall QueryPerformanceCounter(ptr) KERNEL32.QueryPerformanceCounter
@ stdcall QueryPerformanceFrequency(ptr) KERNEL32.QueryPerformanceFrequency
@ stdcall QueueUserAPC(ptr long long) KERNEL32.QueueUserAPC
@ stdcall QueueUserWorkItem(ptr ptr long) KERNEL32.QueueUserWorkItem
@ stdcall -norelay RaiseException(long long long ptr) KERNEL32.RaiseException
@ stdcall ReOpenFile(ptr long long long) KERNEL32.ReOpenFile
@ stdcall ReadConsoleA(long ptr long ptr ptr) KERNEL32.ReadConsoleA
@ stdcall ReadConsoleInputA(long ptr long ptr) KERNEL32.ReadConsoleInputA
@ stdcall ReadConsoleInputExA(long ptr long ptr long) KERNEL32.ReadConsoleInputExA
@ stdcall ReadConsoleInputExW(long ptr long ptr long) KERNEL32.ReadConsoleInputExW
@ stdcall ReadConsoleInputW(long ptr long ptr) KERNEL32.ReadConsoleInputW
@ stdcall ReadConsoleOutputA(long ptr long long ptr) KERNEL32.ReadConsoleOutputA
@ stdcall ReadConsoleOutputAttribute(long ptr long long ptr) KERNEL32.ReadConsoleOutputAttribute
@ stdcall ReadConsoleOutputCharacterA(long ptr long long ptr) KERNEL32.ReadConsoleOutputCharacterA
@ stdcall ReadConsoleOutputCharacterW(long ptr long long ptr) KERNEL32.ReadConsoleOutputCharacterW
@ stdcall ReadConsoleOutputW(long ptr long long ptr) KERNEL32.ReadConsoleOutputW
@ stdcall ReadConsoleW(long ptr long ptr ptr) KERNEL32.ReadConsoleW
@ stdcall ReadDirectoryChangesW(long ptr long long long ptr ptr ptr) KERNEL32.ReadDirectoryChangesW
@ stdcall ReadFile(long ptr long ptr ptr) KERNEL32.ReadFile
@ stdcall ReadFileEx(long ptr long ptr ptr) KERNEL32.ReadFileEx
@ stdcall ReadFileScatter(long ptr long ptr ptr) KERNEL32.ReadFileScatter
@ stdcall ReadProcessMemory(long ptr ptr long ptr) KERNEL32.ReadProcessMemory
@ stdcall RegisterConsoleIME(ptr ptr) KERNEL32.RegisterConsoleIME
@ stdcall RegisterConsoleOS2(long) KERNEL32.RegisterConsoleOS2
@ stdcall RegisterConsoleVDM(long long long long long long long long long long long) KERNEL32.RegisterConsoleVDM
@ stdcall RegisterWaitForInputIdle(ptr) KERNEL32.RegisterWaitForInputIdle
@ stdcall RegisterWaitForSingleObject(ptr long ptr ptr long long) KERNEL32.RegisterWaitForSingleObject
@ stdcall RegisterWaitForSingleObjectEx(long ptr ptr long long) KERNEL32.RegisterWaitForSingleObjectEx
@ stdcall RegisterWowBaseHandlers(long) KERNEL32.RegisterWowBaseHandlers
@ stdcall RegisterWowExec(long) KERNEL32.RegisterWowExec
@ stdcall ReleaseActCtx(ptr) KERNEL32.ReleaseActCtx
@ stdcall ReleaseMutex(long) KERNEL32.ReleaseMutex
@ stdcall ReleaseSemaphore(long long ptr) KERNEL32.ReleaseSemaphore
@ stdcall RemoveDirectoryA(str) KERNEL32.RemoveDirectoryA
@ stdcall RemoveDirectoryW(wstr) KERNEL32.RemoveDirectoryW
@ stdcall RemoveLocalAlternateComputerNameA(str long) KERNEL32.RemoveLocalAlternateComputerNameA
@ stdcall RemoveLocalAlternateComputerNameW(wstr long) KERNEL32.RemoveLocalAlternateComputerNameW
@ stdcall RemoveVectoredContinueHandler(ptr) ntdll.RtlRemoveVectoredContinueHandler
@ stdcall RemoveVectoredExceptionHandler(ptr) ntdll.RtlRemoveVectoredExceptionHandler
@ stdcall ReplaceFile(wstr wstr wstr long ptr ptr)  KERNEL32.ReplaceFile
@ stdcall ReplaceFileA(str str str long ptr ptr) KERNEL32.ReplaceFileA
@ stdcall ReplaceFileW(wstr wstr wstr long ptr ptr) KERNEL32.ReplaceFileW
@ stdcall RequestDeviceWakeup(long) KERNEL32.RequestDeviceWakeup
@ stdcall RequestWakeupLatency(long) KERNEL32.RequestWakeupLatency
@ stdcall ResetEvent(long) KERNEL32.ResetEvent
@ stdcall ResetWriteWatch(ptr long) KERNEL32.ResetWriteWatch
@ stdcall RestoreLastError(long) ntdll.RtlRestoreLastWin32Error
@ stdcall ResumeThread(long) KERNEL32.ResumeThread
@ stdcall -arch=x86_64 RtlAddFunctionTable(ptr long long) ntdll.RtlAddFunctionTable
@ stdcall -register RtlCaptureContext(ptr) ntdll.RtlCaptureContext
@ stdcall RtlCaptureStackBackTrace(long long ptr ptr) ntdll.RtlCaptureStackBackTrace
@ stdcall -arch=x86_64 RtlCompareMemory(ptr ptr ptr) ntdll.RtlCompareMemory
@ stdcall -arch=x86_64 RtlCopyMemory(ptr ptr ptr) ntdll.memcpy
@ stdcall -arch=x86_64 RtlDeleteFunctionTable(ptr) ntdll.RtlDeleteFunctionTable
@ stdcall RtlFillMemory(ptr long long) ntdll.RtlFillMemory
@ stdcall -arch=x86_64 RtlInstallFunctionTableCallback(double double long ptr ptr ptr) ntdll.RtlInstallFunctionTableCallback
@ stdcall -arch=x86_64 RtlLookupFunctionEntry(ptr ptr ptr) ntdll.RtlLookupFunctionEntry
@ stdcall RtlMoveMemory(ptr ptr long) ntdll.RtlMoveMemory
@ stdcall -arch=x86_64 RtlPcToFileHeader(ptr ptr) ntdll.RtlPcToFileHeader
@ stdcall -arch=x86_64 RtlRaiseException(ptr) ntdll.RtlRaiseException
@ stdcall -arch=x86_64 RtlRestoreContext(ptr ptr) ntdll.RtlRestoreContext
@ stdcall RtlUnwind(ptr ptr ptr ptr) ntdll.RtlUnwind
@ stdcall -arch=x86_64 RtlUnwindEx(ptr ptr ptr ptr ptr ptr) ntdll.RtlUnwindEx
@ stdcall -arch=x86_64 RtlVirtualUnwind(ptr ptr ptr long) ntdll.RtlVirtualUnwind
@ stdcall RtlZeroMemory(ptr long) ntdll.RtlZeroMemory
@ stdcall ScrollConsoleScreenBufferA(long ptr ptr ptr ptr) KERNEL32.ScrollConsoleScreenBufferA
@ stdcall ScrollConsoleScreenBufferW(long ptr ptr ptr ptr) KERNEL32.ScrollConsoleScreenBufferW
@ stdcall SearchPathA(str str str long ptr ptr) KERNEL32.SearchPathA
@ stdcall SearchPathW(wstr wstr wstr long ptr ptr) KERNEL32.SearchPathW
@ stdcall -version=0x500-0x502 SetCPGlobal(long) KERNEL32.SetCPGlobal
@ stdcall SetCalendarInfoA(long long long str) KERNEL32.SetCalendarInfoA
@ stdcall SetCalendarInfoW(long long long wstr) KERNEL32.SetCalendarInfoW
@ stdcall SetClientTimeZoneInformation(ptr) KERNEL32.SetClientTimeZoneInformation
@ stdcall SetComPlusPackageInstallStatus(ptr) KERNEL32.SetComPlusPackageInstallStatus
@ stdcall SetCommBreak(long) KERNEL32.SetCommBreak
@ stdcall SetCommConfig(long ptr long) KERNEL32.SetCommConfig
@ stdcall SetCommMask(long ptr) KERNEL32.SetCommMask
@ stdcall SetCommState(long ptr) KERNEL32.SetCommState
@ stdcall SetCommTimeouts(long ptr) KERNEL32.SetCommTimeouts
@ stdcall SetComputerNameA(str) KERNEL32.SetComputerNameA
@ stdcall SetComputerNameExA(long str) KERNEL32.SetComputerNameExA
@ stdcall SetComputerNameExW(long wstr) KERNEL32.SetComputerNameExW
@ stdcall SetComputerNameW(wstr) KERNEL32.SetComputerNameW
@ stdcall SetConsoleActiveScreenBuffer(long) KERNEL32.SetConsoleActiveScreenBuffer
@ stdcall SetConsoleCP(long) KERNEL32.SetConsoleCP
@ stdcall -version=0x351-0x502 SetConsoleCommandHistoryMode(long) KERNEL32.SetConsoleCommandHistoryMode
@ stdcall SetConsoleCtrlHandler(ptr long) KERNEL32.SetConsoleCtrlHandler
@ stdcall SetConsoleCursor(long long) KERNEL32.SetConsoleCursor
@ stdcall SetConsoleCursorInfo(long ptr) KERNEL32.SetConsoleCursorInfo
@ stdcall SetConsoleCursorMode(long long long) KERNEL32.SetConsoleCursorMode
@ stdcall SetConsoleCursorPosition(long long) KERNEL32.SetConsoleCursorPosition
@ stdcall SetConsoleDisplayMode(long long ptr) KERNEL32.SetConsoleDisplayMode
@ stdcall SetConsoleFont(long long) KERNEL32.SetConsoleFont
@ stdcall SetConsoleHardwareState(long long long) KERNEL32.SetConsoleHardwareState
@ stdcall SetConsoleIcon(ptr) KERNEL32.SetConsoleIcon
@ stdcall SetConsoleInputExeNameA(ptr) KERNEL32.SetConsoleInputExeNameA
@ stdcall SetConsoleInputExeNameW(ptr) KERNEL32.SetConsoleInputExeNameW
@ stdcall SetConsoleKeyShortcuts(long long long long) KERNEL32.SetConsoleKeyShortcuts
@ stdcall SetConsoleLocalEUDC(long long long long) KERNEL32.SetConsoleLocalEUDC
@ stdcall SetConsoleMaximumWindowSize(long long) KERNEL32.SetConsoleMaximumWindowSize
@ stdcall SetConsoleMenuClose(long) KERNEL32.SetConsoleMenuClose
@ stdcall SetConsoleMode(long long) KERNEL32.SetConsoleMode
@ stdcall SetConsoleNlsMode(long long) KERNEL32.SetConsoleNlsMode
@ stdcall SetConsoleNumberOfCommandsA(long long) KERNEL32.SetConsoleNumberOfCommandsA
@ stdcall SetConsoleNumberOfCommandsW(long long) KERNEL32.SetConsoleNumberOfCommandsW
@ stdcall SetConsoleOS2OemFormat(long) KERNEL32.SetConsoleOS2OemFormat
@ stdcall SetConsoleOutputCP(long) KERNEL32.SetConsoleOutputCP
@ stdcall SetConsolePalette(long long long) KERNEL32.SetConsolePalette
@ stdcall SetConsoleScreenBufferSize(long long) KERNEL32.SetConsoleScreenBufferSize
@ stdcall SetConsoleTextAttribute(long long) KERNEL32.SetConsoleTextAttribute
@ stdcall SetConsoleTitleA(str) KERNEL32.SetConsoleTitleA
@ stdcall SetConsoleTitleW(wstr) KERNEL32.SetConsoleTitleW
@ stdcall SetConsoleWindowInfo(long long ptr) KERNEL32.SetConsoleWindowInfo
@ stdcall SetCriticalSectionSpinCount(ptr long) ntdll.RtlSetCriticalSectionSpinCount
@ stdcall SetCurrentDirectoryA(str) KERNEL32.SetCurrentDirectoryA
@ stdcall SetCurrentDirectoryW(wstr) KERNEL32.SetCurrentDirectoryW
@ stdcall SetDefaultCommConfigA(str ptr long) KERNEL32.SetDefaultCommConfigA
@ stdcall SetDefaultCommConfigW(wstr ptr long) KERNEL32.SetDefaultCommConfigW
@ stdcall SetDllDirectoryA(str) KERNEL32.SetDllDirectoryA
@ stdcall SetDllDirectoryW(wstr) KERNEL32.SetDllDirectoryW
@ stdcall SetEndOfFile(long) KERNEL32.SetEndOfFile
@ stdcall SetEnvironmentStringsA(ptr) KERNEL32.SetEnvironmentStringsA
@ stdcall SetEnvironmentStringsW(ptr) KERNEL32.SetEnvironmentStringsW
@ stdcall SetEnvironmentVariableA(str str) KERNEL32.SetEnvironmentVariableA
@ stdcall SetEnvironmentVariableW(wstr wstr) KERNEL32.SetEnvironmentVariableW
@ stdcall SetErrorMode(long) KERNEL32.SetErrorMode
@ stdcall SetEvent(long) KERNEL32.SetEvent
@ stdcall SetFileApisToANSI() KERNEL32.SetFileApisToANSI
@ stdcall SetFileApisToOEM() KERNEL32.SetFileApisToOEM
@ stdcall SetFileAttributesA(str long) KERNEL32.SetFileAttributesA
@ stdcall SetFileAttributesW(wstr long) KERNEL32.SetFileAttributesW
@ stdcall SetFileCompletionNotificationModes(ptr long) KERNEL32.SetFileCompletionNotificationModes
@ stdcall SetFilePointer(long long ptr long) KERNEL32.SetFilePointer
@ stdcall SetFilePointerEx(long double ptr long) KERNEL32.SetFilePointerEx
@ stdcall SetFileShortNameA(long str) KERNEL32.SetFileShortNameA
@ stdcall SetFileShortNameW(long wstr) KERNEL32.SetFileShortNameW
@ stdcall SetFileTime(long ptr ptr ptr) KERNEL32.SetFileTime
@ stdcall SetFileValidData(long double) KERNEL32.SetFileValidData
@ stdcall SetFirmwareEnvironmentVariableA(str str ptr long) KERNEL32.SetFirmwareEnvironmentVariableA
@ stdcall SetFirmwareEnvironmentVariableW(wstr wstr ptr long) KERNEL32.SetFirmwareEnvironmentVariableW
@ stdcall -i386 SetHandleContext(long long) KERNEL32.SetHandleContext
@ stdcall SetHandleCount(long) KERNEL32.SetHandleCount
@ stdcall SetHandleInformation(long long long) KERNEL32.SetHandleInformation
@ stdcall SetInformationJobObject(long long ptr long) KERNEL32.SetInformationJobObject
@ stdcall SetLastConsoleEventActive() KERNEL32.SetLastConsoleEventActive
@ stdcall SetLastError(long) ntdll.RtlSetLastWin32Error
@ stdcall SetLocalPrimaryComputerNameA(long long) KERNEL32.SetLocalPrimaryComputerNameA
@ stdcall SetLocalPrimaryComputerNameW(long long) KERNEL32.SetLocalPrimaryComputerNameW
@ stdcall SetLocalTime(ptr) KERNEL32.SetLocalTime
@ stdcall SetLocaleInfoA(long long str) KERNEL32.SetLocaleInfoA
@ stdcall SetLocaleInfoW(long long wstr) KERNEL32.SetLocaleInfoW
@ stdcall SetMailslotInfo(long long) KERNEL32.SetMailslotInfo
@ stdcall SetMessageWaitingIndicator(ptr long) KERNEL32.SetMessageWaitingIndicator
@ stdcall SetNamedPipeHandleState(long ptr ptr ptr) KERNEL32.SetNamedPipeHandleState
@ stdcall SetPriorityClass(long long) KERNEL32.SetPriorityClass
@ stdcall SetProcessAffinityMask(long long) KERNEL32.SetProcessAffinityMask
@ stdcall SetProcessPriorityBoost(long long) KERNEL32.SetProcessPriorityBoost
@ stdcall SetProcessShutdownParameters(long long) KERNEL32.SetProcessShutdownParameters
@ stdcall SetProcessWorkingSetSize(long long long) KERNEL32.SetProcessWorkingSetSize
@ stdcall SetProcessWorkingSetSizeEx(long long long long) KERNEL32.SetProcessWorkingSetSizeEx
@ stdcall SetStdHandle(long long) KERNEL32.SetStdHandle
@ stdcall SetSystemFileCacheSize(long long long) KERNEL32.SetSystemFileCacheSize
@ stdcall SetSystemPowerState(long long) KERNEL32.SetSystemPowerState
@ stdcall SetSystemTime(ptr) KERNEL32.SetSystemTime
@ stdcall SetSystemTimeAdjustment(long long) KERNEL32.SetSystemTimeAdjustment
@ stdcall SetTapeParameters(ptr long ptr) KERNEL32.SetTapeParameters
@ stdcall SetTapePosition(ptr long long long long long) KERNEL32.SetTapePosition
@ stdcall SetTermsrvAppInstallMode(long) KERNEL32.SetTermsrvAppInstallMode
@ stdcall SetThreadAffinityMask(long long) KERNEL32.SetThreadAffinityMask
@ stdcall SetThreadContext(long ptr) KERNEL32.SetThreadContext
@ stdcall SetThreadExecutionState(long) KERNEL32.SetThreadExecutionState
@ stdcall SetThreadIdealProcessor(long long) KERNEL32.SetThreadIdealProcessor
@ stdcall SetThreadLocale(long) KERNEL32.SetThreadLocale
@ stdcall SetThreadPriority(long long) KERNEL32.SetThreadPriority
@ stdcall SetThreadPriorityBoost(long long) KERNEL32.SetThreadPriorityBoost
@ stdcall SetThreadStackGuarantee(ptr) KERNEL32.SetThreadStackGuarantee
@ stdcall SetThreadUILanguage(long) KERNEL32.SetThreadUILanguage
@ stdcall SetTimeZoneInformation(ptr) KERNEL32.SetTimeZoneInformation
@ stdcall SetTimerQueueTimer(long ptr ptr long long long) KERNEL32.SetTimerQueueTimer
@ stdcall SetUnhandledExceptionFilter(ptr) KERNEL32.SetUnhandledExceptionFilter
@ stdcall SetUserGeoID(long) KERNEL32.SetUserGeoID
@ stdcall SetVDMCurrentDirectories(long long) KERNEL32.SetVDMCurrentDirectories
@ stdcall SetVolumeLabelA(str str) KERNEL32.SetVolumeLabelA
@ stdcall SetVolumeLabelW(wstr wstr) KERNEL32.SetVolumeLabelW
@ stdcall SetVolumeMountPointA(str str) KERNEL32.SetVolumeMountPointA
@ stdcall SetVolumeMountPointW(wstr wstr) KERNEL32.SetVolumeMountPointW
@ stdcall SetWaitableTimer(long ptr long ptr ptr long) KERNEL32.SetWaitableTimer
@ stdcall SetupComm(long long long) KERNEL32.SetupComm
@ stdcall ShowConsoleCursor(long long) KERNEL32.ShowConsoleCursor
@ stdcall SignalObjectAndWait(long long long long) KERNEL32.SignalObjectAndWait
@ stdcall SizeofResource(long long) KERNEL32.SizeofResource
@ stdcall Sleep(long) KERNEL32.Sleep
@ stdcall SleepEx(long long) KERNEL32.SleepEx
@ stdcall SuspendThread(long) KERNEL32.SuspendThread
@ stdcall SwitchToFiber(ptr) KERNEL32.SwitchToFiber
@ stdcall SwitchToThread() KERNEL32.SwitchToThread
@ stdcall SystemTimeToFileTime(ptr ptr) KERNEL32.SystemTimeToFileTime
@ stdcall SystemTimeToTzSpecificLocalTime (ptr ptr ptr) KERNEL32.SystemTimeToTzSpecificLocalTime
@ stdcall TerminateJobObject(long long) KERNEL32.TerminateJobObject
@ stdcall TerminateProcess(long long) KERNEL32.TerminateProcess
@ stdcall TerminateThread(long long) KERNEL32.TerminateThread
@ stdcall TermsrvAppInstallMode() KERNEL32.TermsrvAppInstallMode
@ stdcall Thread32First(long ptr) KERNEL32.Thread32First
@ stdcall Thread32Next(long ptr) KERNEL32.Thread32Next
@ stdcall TlsAlloc() KERNEL32.TlsAlloc
@ stdcall TlsFree(long) KERNEL32.TlsFree
@ stdcall -norelay TlsGetValue(long) KERNEL32.TlsGetValue
@ stdcall -norelay TlsSetValue(long ptr) KERNEL32.TlsSetValue
@ stdcall Toolhelp32ReadProcessMemory(long ptr ptr long ptr) KERNEL32.Toolhelp32ReadProcessMemory
@ stdcall TransactNamedPipe(long ptr long ptr long ptr ptr) KERNEL32.TransactNamedPipe
@ stdcall TransmitCommChar(long long) KERNEL32.TransmitCommChar
@ stdcall TryEnterCriticalSection(ptr) ntdll.RtlTryEnterCriticalSection
@ stdcall TzSpecificLocalTimeToSystemTime(ptr ptr ptr) KERNEL32.TzSpecificLocalTimeToSystemTime
@ stdcall UTRegister(long str str str ptr ptr ptr) KERNEL32.UTRegister
@ stdcall UTUnRegister(long) KERNEL32.UTUnRegister
@ stdcall UnhandledExceptionFilter(ptr) KERNEL32.UnhandledExceptionFilter
@ stdcall UnlockFile(long long long long long) KERNEL32.UnlockFile
@ stdcall UnlockFileEx(long long long long ptr) KERNEL32.UnlockFileEx
@ stdcall UnmapViewOfFile(ptr) KERNEL32.UnmapViewOfFile
@ stdcall UnregisterConsoleIME() KERNEL32.UnregisterConsoleIME
@ stdcall UnregisterWait(long) KERNEL32.UnregisterWait
@ stdcall UnregisterWaitEx(long long) KERNEL32.UnregisterWaitEx
@ stdcall UpdateResourceA(long str str long ptr long) KERNEL32.UpdateResourceA
@ stdcall UpdateResourceW(long wstr wstr long ptr long) KERNEL32.UpdateResourceW
@ stdcall VDMConsoleOperation(long long) KERNEL32.VDMConsoleOperation
@ stdcall VDMOperationStarted(long) KERNEL32.VDMOperationStarted
@ stdcall -version=0x500-0x502 ValidateLCType(long long ptr ptr) KERNEL32.ValidateLCType
@ stdcall -version=0x500-0x502 ValidateLocale(long) KERNEL32.ValidateLocale
@ stdcall VerLanguageNameA(long str long) KERNEL32.VerLanguageNameA
@ stdcall VerLanguageNameW(long wstr long) KERNEL32.VerLanguageNameW
@ stdcall -ret64 VerSetConditionMask(long long long long) ntdll.VerSetConditionMask
@ stdcall VerifyConsoleIoHandle(long) KERNEL32.VerifyConsoleIoHandle
@ stdcall VerifyVersionInfoA(long long double) KERNEL32.VerifyVersionInfoA
@ stdcall VerifyVersionInfoW(long long double) KERNEL32.VerifyVersionInfoW
@ stdcall VirtualAlloc(ptr long long long) KERNEL32.VirtualAlloc
@ stdcall VirtualAllocEx(long ptr long long long) KERNEL32.VirtualAllocEx
@ stdcall VirtualFree(ptr long long) KERNEL32.VirtualFree
@ stdcall VirtualFreeEx(long ptr long long) KERNEL32.VirtualFreeEx
@ stdcall VirtualLock(ptr long) KERNEL32.VirtualLock
@ stdcall VirtualProtect(ptr long long ptr) KERNEL32.VirtualProtect
@ stdcall VirtualProtectEx(long ptr long long ptr) KERNEL32.VirtualProtectEx
@ stdcall VirtualQuery(ptr ptr long) KERNEL32.VirtualQuery
@ stdcall VirtualQueryEx(long ptr ptr long) KERNEL32.VirtualQueryEx
@ stdcall VirtualUnlock(ptr long) KERNEL32.VirtualUnlock
@ stdcall WTSGetActiveConsoleSessionId() KERNEL32.WTSGetActiveConsoleSessionId
@ stdcall WaitCommEvent(long ptr ptr) KERNEL32.WaitCommEvent
@ stdcall WaitForDebugEvent(ptr long) KERNEL32.WaitForDebugEvent
@ stdcall WaitForMultipleObjects(long ptr long long) KERNEL32.WaitForMultipleObjects
@ stdcall WaitForMultipleObjectsEx(long ptr long long long) KERNEL32.WaitForMultipleObjectsEx
@ stdcall WaitForSingleObject(long long) KERNEL32.WaitForSingleObject
@ stdcall WaitForSingleObjectEx(long long long) KERNEL32.WaitForSingleObjectEx
@ stdcall WaitNamedPipeA (str long) KERNEL32.WaitNamedPipeA
@ stdcall WaitNamedPipeW (wstr long) KERNEL32.WaitNamedPipeW
@ stdcall WideCharToMultiByte(long long wstr long ptr long ptr ptr) KERNEL32.WideCharToMultiByte
@ stdcall WinExec(str long) KERNEL32.WinExec
@ stdcall Wow64DisableWow64FsRedirection(ptr) KERNEL32.Wow64DisableWow64FsRedirection
@ stdcall Wow64EnableWow64FsRedirection(long) KERNEL32.Wow64EnableWow64FsRedirection
@ stdcall Wow64RevertWow64FsRedirection(ptr) KERNEL32.Wow64RevertWow64FsRedirection
@ stdcall WriteConsoleA(long ptr long ptr ptr) KERNEL32.WriteConsoleA
@ stdcall WriteConsoleInputA(long ptr long ptr) KERNEL32.WriteConsoleInputA
@ stdcall WriteConsoleInputVDMA(long long long long) KERNEL32.WriteConsoleInputVDMA
@ stdcall WriteConsoleInputVDMW(long long long long) KERNEL32.WriteConsoleInputVDMW
@ stdcall WriteConsoleInputW(long ptr long ptr) KERNEL32.WriteConsoleInputW
@ stdcall WriteConsoleOutputA(long ptr long long ptr) KERNEL32.WriteConsoleOutputA
@ stdcall WriteConsoleOutputAttribute(long ptr long long ptr) KERNEL32.WriteConsoleOutputAttribute
@ stdcall WriteConsoleOutputCharacterA(long ptr long long ptr) KERNEL32.WriteConsoleOutputCharacterA
@ stdcall WriteConsoleOutputCharacterW(long ptr long long ptr) KERNEL32.WriteConsoleOutputCharacterW
@ stdcall WriteConsoleOutputW(long ptr long long ptr) KERNEL32.WriteConsoleOutputW
@ stdcall WriteConsoleW(long ptr long ptr ptr) KERNEL32.WriteConsoleW
@ stdcall WriteFile(long ptr long ptr ptr) KERNEL32.WriteFile
@ stdcall WriteFileEx(long ptr long ptr ptr) KERNEL32.WriteFileEx
@ stdcall WriteFileGather(long ptr long ptr ptr) KERNEL32.WriteFileGather
@ stdcall WritePrivateProfileSectionA(str str str) KERNEL32.WritePrivateProfileSectionA
@ stdcall WritePrivateProfileSectionW(wstr wstr wstr) KERNEL32.WritePrivateProfileSectionW
@ stdcall WritePrivateProfileStringA(str str str str) KERNEL32.WritePrivateProfileStringA
@ stdcall WritePrivateProfileStringW(wstr wstr wstr wstr) KERNEL32.WritePrivateProfileStringW
@ stdcall WritePrivateProfileStructA (str str ptr long str) KERNEL32.WritePrivateProfileStructA
@ stdcall WritePrivateProfileStructW(wstr wstr ptr long wstr) KERNEL32.WritePrivateProfileStructW
@ stdcall WriteProcessMemory(long ptr ptr long ptr) KERNEL32.WriteProcessMemory
@ stdcall WriteProfileSectionA(str str) KERNEL32.WriteProfileSectionA
@ stdcall WriteProfileSectionW(str str) KERNEL32.WriteProfileSectionW
@ stdcall WriteProfileStringA(str str str) KERNEL32.WriteProfileStringA
@ stdcall WriteProfileStringW(wstr wstr wstr) KERNEL32.WriteProfileStringW
@ stdcall WriteTapemark(ptr long long long) KERNEL32.WriteTapemark
@ stdcall ZombifyActCtx(ptr) KERNEL32.ZombifyActCtx
@ stdcall -arch=x86_64 __C_specific_handler() ntdll.__C_specific_handler
@ stdcall -arch=x86_64 __chkstk() ntdll.__chkstk
@ stdcall _hread(long ptr long) KERNEL32._hread
@ stdcall _hwrite(long ptr long) KERNEL32._hwrite
@ stdcall _lclose(long) KERNEL32._lclose
@ stdcall _lcreat(str long) KERNEL32._lcreat
@ stdcall _llseek(long long long) KERNEL32._llseek
@ stdcall -arch=x86_64 _local_unwind() ntdll._local_unwind
@ stdcall _lopen(str long) KERNEL32._lopen
@ stdcall _lread(long ptr long)  KERNEL32._lread
@ stdcall _lwrite(long ptr long)  KERNEL32._lwrite
@ stdcall lstrcat(str str)  KERNEL32.lstrcat
@ stdcall lstrcatA(str str) KERNEL32.lstrcatA
@ stdcall lstrcatW(wstr wstr) KERNEL32.lstrcatW
@ stdcall lstrcmp(str str)  KERNEL32.lstrcmp
@ stdcall lstrcmpA(str str) KERNEL32.lstrcmpA
@ stdcall lstrcmpW(wstr wstr) KERNEL32.lstrcmpW
@ stdcall lstrcmpi(str str)  KERNEL32.lstrcmpi
@ stdcall lstrcmpiA(str str) KERNEL32.lstrcmpiA
@ stdcall lstrcmpiW(wstr wstr) KERNEL32.lstrcmpiW
@ stdcall lstrcpy(ptr str)  KERNEL32.lstrcpy
@ stdcall lstrcpyA(ptr str) KERNEL32.lstrcpyA
@ stdcall lstrcpyW(ptr wstr) KERNEL32.lstrcpyW
@ stdcall lstrcpyn(ptr str long)  KERNEL32.lstrcpyn
@ stdcall lstrcpynA(ptr str long) KERNEL32.lstrcpynA
@ stdcall lstrcpynW(ptr wstr long) KERNEL32.lstrcpynW
@ stdcall lstrlen(str)  KERNEL32.lstrlen
@ stdcall lstrlenA(str) KERNEL32.lstrlenA
@ stdcall lstrlenW(wstr) KERNEL32.lstrlenW
