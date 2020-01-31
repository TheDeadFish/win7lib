@ fastcall RtlActivateActivationContextUnsafeFast(ptr ptr) NTDLL.RtlActivateActivationContextUnsafeFast
@ fastcall RtlDeactivateActivationContextUnsafeFast(ptr) NTDLL.RtlDeactivateActivationContextUnsafeFast
@ fastcall RtlInterlockedPushListSList(ptr ptr ptr long) NTDLL.RtlInterlockedPushListSList
@ fastcall -arch=i386 RtlUlongByteSwap(long) NTDLL.RtlUlongByteSwap
@ fastcall -ret64 RtlUlonglongByteSwap(double) NTDLL.RtlUlonglongByteSwap
@ fastcall -arch=i386 RtlUshortByteSwap(long) NTDLL.RtlUshortByteSwap
@ stdcall -arch=i386,x86_64 ExpInterlockedPopEntrySListEnd() NTDLL.ExpInterlockedPopEntrySListEnd
@ stdcall -arch=i386,x86_64 ExpInterlockedPopEntrySListFault() NTDLL.ExpInterlockedPopEntrySListFault
@ stdcall -arch=i386,x86_64 ExpInterlockedPopEntrySListResume() NTDLL.ExpInterlockedPopEntrySListResume
@ stdcall CsrAllocateCaptureBuffer(long long) NTDLL.CsrAllocateCaptureBuffer
@ stdcall CsrAllocateMessagePointer(ptr long ptr) NTDLL.CsrAllocateMessagePointer
@ stdcall CsrCaptureMessageBuffer(ptr ptr long ptr) NTDLL.CsrCaptureMessageBuffer
@ stdcall CsrCaptureMessageMultiUnicodeStringsInPlace(ptr long ptr) NTDLL.CsrCaptureMessageMultiUnicodeStringsInPlace
@ stdcall CsrCaptureMessageString(ptr str long long ptr) NTDLL.CsrCaptureMessageString
@ stdcall CsrCaptureTimeout(long ptr) NTDLL.CsrCaptureTimeout
@ stdcall CsrClientCallServer(ptr ptr long long) NTDLL.CsrClientCallServer
@ stdcall CsrClientConnectToServer(str long ptr ptr ptr) NTDLL.CsrClientConnectToServer
@ stdcall CsrFreeCaptureBuffer(ptr) NTDLL.CsrFreeCaptureBuffer
@ stdcall CsrGetProcessId() NTDLL.CsrGetProcessId
@ stdcall CsrIdentifyAlertableThread() NTDLL.CsrIdentifyAlertableThread
@ stdcall CsrNewThread() NTDLL.CsrNewThread
@ stdcall CsrProbeForRead(ptr long long) NTDLL.CsrProbeForRead
@ stdcall CsrProbeForWrite(ptr long long) NTDLL.CsrProbeForWrite
@ stdcall CsrSetPriorityClass(ptr ptr) NTDLL.CsrSetPriorityClass
@ stdcall DbgBreakPoint() NTDLL.DbgBreakPoint
@ varargs DbgPrint(str) NTDLL.DbgPrint
@ varargs DbgPrintEx(long long str) NTDLL.DbgPrintEx
@ varargs DbgPrintReturnControlC(str) NTDLL.DbgPrintReturnControlC
@ stdcall DbgPrompt(ptr ptr long) NTDLL.DbgPrompt
@ stdcall DbgQueryDebugFilterState(long long) NTDLL.DbgQueryDebugFilterState
@ stdcall DbgSetDebugFilterState(long long long) NTDLL.DbgSetDebugFilterState
@ stdcall DbgUiConnectToDbg() NTDLL.DbgUiConnectToDbg
@ stdcall DbgUiContinue(ptr long) NTDLL.DbgUiContinue
@ stdcall DbgUiConvertStateChangeStructure(ptr ptr) NTDLL.DbgUiConvertStateChangeStructure
@ stdcall DbgUiDebugActiveProcess(ptr) NTDLL.DbgUiDebugActiveProcess
@ stdcall DbgUiGetThreadDebugObject() NTDLL.DbgUiGetThreadDebugObject
@ stdcall DbgUiIssueRemoteBreakin(ptr) NTDLL.DbgUiIssueRemoteBreakin
@ stdcall DbgUiRemoteBreakin() NTDLL.DbgUiRemoteBreakin
@ stdcall DbgUiSetThreadDebugObject(ptr) NTDLL.DbgUiSetThreadDebugObject
@ stdcall DbgUiStopDebugging(ptr) NTDLL.DbgUiStopDebugging
@ stdcall DbgUiWaitStateChange(ptr ptr) NTDLL.DbgUiWaitStateChange
@ stdcall DbgUserBreakPoint() NTDLL.DbgUserBreakPoint
@ stdcall EtwControlTraceA(double str ptr long) NTDLL.EtwControlTraceA
@ stdcall EtwControlTraceW(double wstr ptr long) NTDLL.EtwControlTraceW
@ stdcall  EtwCreateTraceInstanceId(ptr ptr) NTDLL.EtwCreateTraceInstanceId
@ stdcall EtwEnableTrace(long long long ptr double) NTDLL.EtwEnableTrace
@ stdcall  EtwEnumerateTraceGuids(ptr long ptr) NTDLL.EtwEnumerateTraceGuids
@ stdcall EtwFlushTraceA(double str ptr) NTDLL.EtwFlushTraceA
@ stdcall EtwFlushTraceW(double wstr ptr) NTDLL.EtwFlushTraceW
@ stdcall EtwGetTraceEnableFlags(double) NTDLL.EtwGetTraceEnableFlags
@ stdcall EtwGetTraceEnableLevel(double) NTDLL.EtwGetTraceEnableLevel
@ stdcall EtwGetTraceLoggerHandle(ptr) NTDLL.EtwGetTraceLoggerHandle
@ stdcall  EtwNotificationRegistrationA(ptr long ptr long long) NTDLL.EtwNotificationRegistrationA
@ stdcall  EtwNotificationRegistrationW(ptr long ptr long long) NTDLL.EtwNotificationRegistrationW
@ stdcall EtwQueryAllTracesA(ptr long ptr) NTDLL.EtwQueryAllTracesA
@ stdcall EtwQueryAllTracesW(ptr long ptr) NTDLL.EtwQueryAllTracesW
@ stdcall EtwQueryTraceA(double str ptr) NTDLL.EtwQueryTraceA
@ stdcall EtwQueryTraceW(double wstr ptr) NTDLL.EtwQueryTraceW
@ stdcall  EtwReceiveNotificationsA(long long long long) NTDLL.EtwReceiveNotificationsA
@ stdcall  EtwReceiveNotificationsW(long long long long) NTDLL.EtwReceiveNotificationsW
@ stdcall EtwRegisterTraceGuidsA(ptr ptr ptr long ptr str str ptr) NTDLL.EtwRegisterTraceGuidsA
@ stdcall EtwRegisterTraceGuidsW(ptr ptr ptr long ptr wstr wstr ptr) NTDLL.EtwRegisterTraceGuidsW
@ stdcall EtwStartTraceA(ptr str ptr) NTDLL.EtwStartTraceA
@ stdcall EtwStartTraceW(ptr wstr ptr) NTDLL.EtwStartTraceW
@ stdcall EtwStopTraceA(double str ptr) NTDLL.EtwStopTraceA
@ stdcall EtwStopTraceW(double wstr ptr) NTDLL.EtwStopTraceW
@ stdcall EtwTraceEvent(double ptr) NTDLL.EtwTraceEvent
@ stdcall  EtwTraceEventInstance(double ptr ptr ptr) NTDLL.EtwTraceEventInstance
@ varargs EtwTraceMessage(ptr long ptr long) NTDLL.EtwTraceMessage
@ stdcall  EtwTraceMessageVa(double long ptr long ptr) NTDLL.EtwTraceMessageVa
@ stdcall EtwUnregisterTraceGuids(double) NTDLL.EtwUnregisterTraceGuids
@ stdcall EtwUpdateTraceA(double str ptr) NTDLL.EtwUpdateTraceA
@ stdcall EtwUpdateTraceW(double wstr ptr) NTDLL.EtwUpdateTraceW
@ stdcall  EtwpGetTraceBuffer(long long long long) NTDLL.EtwpGetTraceBuffer
@ stdcall  EtwpSetHWConfigFunction(ptr long) NTDLL.EtwpSetHWConfigFunction
@ stdcall -arch=i386 KiFastSystemCall() NTDLL.KiFastSystemCall
@ stdcall -arch=i386 KiFastSystemCallRet() NTDLL.KiFastSystemCallRet
@ stdcall -arch=i386 KiIntSystemCall() NTDLL.KiIntSystemCall
@ stdcall KiRaiseUserExceptionDispatcher() NTDLL.KiRaiseUserExceptionDispatcher
@ stdcall KiUserApcDispatcher(ptr ptr ptr ptr) NTDLL.KiUserApcDispatcher
@ stdcall KiUserCallbackDispatcher(ptr ptr long) ; CHECKME NTDLL.KiUserCallbackDispatcher
@ stdcall KiUserExceptionDispatcher(ptr ptr) NTDLL.KiUserExceptionDispatcher
@ stdcall LdrAccessOutOfProcessResource(ptr ptr ptr ptr ptr) NTDLL.LdrAccessOutOfProcessResource
@ stdcall LdrAccessResource(long ptr ptr ptr) NTDLL.LdrAccessResource
@ stdcall LdrAddRefDll(long ptr) NTDLL.LdrAddRefDll
@ stdcall LdrCreateOutOfProcessImage(long ptr ptr ptr) NTDLL.LdrCreateOutOfProcessImage
@ stdcall LdrDestroyOutOfProcessImage(ptr) NTDLL.LdrDestroyOutOfProcessImage
@ stdcall LdrDisableThreadCalloutsForDll(long) NTDLL.LdrDisableThreadCalloutsForDll
@ stdcall LdrEnumResources(ptr ptr long ptr ptr) NTDLL.LdrEnumResources
@ stdcall LdrEnumerateLoadedModules(long ptr long) NTDLL.LdrEnumerateLoadedModules
@ stdcall LdrFindCreateProcessManifest(long ptr ptr long ptr) NTDLL.LdrFindCreateProcessManifest
@ stdcall LdrFindEntryForAddress(ptr ptr) NTDLL.LdrFindEntryForAddress
@ stdcall LdrFindResourceDirectory_U(long ptr long ptr) NTDLL.LdrFindResourceDirectory_U
@ stdcall LdrFindResource_U(long ptr long ptr) NTDLL.LdrFindResource_U
@ stdcall LdrFlushAlternateResourceModules() NTDLL.LdrFlushAlternateResourceModules
@ stdcall LdrGetDllHandle(wstr long ptr ptr) NTDLL.LdrGetDllHandle
@ stdcall LdrGetDllHandleEx(long wstr long ptr ptr) NTDLL.LdrGetDllHandleEx
@ stdcall LdrGetProcedureAddress(ptr ptr long ptr) NTDLL.LdrGetProcedureAddress
@ stdcall LdrInitializeThunk(long long long long) NTDLL.LdrInitializeThunk
@ stdcall LdrLoadAlternateResourceModule(ptr ptr) NTDLL.LdrLoadAlternateResourceModule
@ stdcall LdrLoadDll(wstr long ptr ptr) NTDLL.LdrLoadDll
@ stdcall LdrLockLoaderLock(long ptr ptr) NTDLL.LdrLockLoaderLock
@ stdcall LdrOpenImageFileOptionsKey(ptr long ptr) ; 5.2 SP1 and higher NTDLL.LdrOpenImageFileOptionsKey
@ stdcall LdrProcessRelocationBlock(ptr long ptr long) NTDLL.LdrProcessRelocationBlock
@ stdcall LdrQueryImageFileExecutionOptions(ptr str long ptr long ptr) NTDLL.LdrQueryImageFileExecutionOptions
@ stdcall LdrQueryImageFileKeyOption(ptr ptr long ptr long ptr) NTDLL.LdrQueryImageFileKeyOption
@ stdcall LdrQueryProcessModuleInformation(ptr long ptr) NTDLL.LdrQueryProcessModuleInformation
@ stdcall LdrSetDllManifestProber(ptr) NTDLL.LdrSetDllManifestProber
@ stdcall LdrShutdownProcess() NTDLL.LdrShutdownProcess
@ stdcall LdrShutdownThread() NTDLL.LdrShutdownThread
@ stdcall LdrUnloadAlternateResourceModule(ptr) NTDLL.LdrUnloadAlternateResourceModule
@ stdcall LdrUnloadDll(ptr) NTDLL.LdrUnloadDll
@ stdcall LdrUnlockLoaderLock(long long) NTDLL.LdrUnlockLoaderLock
@ stdcall LdrVerifyImageMatchesChecksum(ptr long long long) NTDLL.LdrVerifyImageMatchesChecksum
@ extern NlsAnsiCodePage NTDLL.NlsAnsiCodePage
@ extern NlsMbCodePageTag NTDLL.NlsMbCodePageTag
@ extern NlsMbOemCodePageTag NTDLL.NlsMbOemCodePageTag
@ stdcall NtAcceptConnectPort(ptr long ptr long long ptr) NTDLL.NtAcceptConnectPort
@ stdcall NtAccessCheck(ptr long long ptr ptr ptr ptr ptr) NTDLL.NtAccessCheck
@ stdcall NtAccessCheckAndAuditAlarm(ptr long ptr ptr ptr long ptr long ptr ptr ptr) NTDLL.NtAccessCheckAndAuditAlarm
@ stdcall NtAccessCheckByType(ptr ptr ptr long ptr long ptr ptr long ptr ptr) NTDLL.NtAccessCheckByType
@ stdcall NtAccessCheckByTypeAndAuditAlarm(ptr ptr ptr ptr ptr ptr long long long ptr long ptr long ptr ptr ptr) NTDLL.NtAccessCheckByTypeAndAuditAlarm
@ stdcall NtAccessCheckByTypeResultList(ptr ptr ptr long ptr long ptr ptr long ptr ptr) NTDLL.NtAccessCheckByTypeResultList
@ stdcall NtAccessCheckByTypeResultListAndAuditAlarm(ptr ptr ptr ptr ptr ptr long long long ptr long ptr long ptr ptr ptr) NTDLL.NtAccessCheckByTypeResultListAndAuditAlarm
@ stdcall NtAccessCheckByTypeResultListAndAuditAlarmByHandle(ptr ptr ptr ptr ptr ptr ptr long long long ptr long ptr long ptr ptr ptr) NTDLL.NtAccessCheckByTypeResultListAndAuditAlarmByHandle
@ stdcall NtAddAtom(ptr long ptr) NTDLL.NtAddAtom
@ stdcall NtAddBootEntry(ptr long) NTDLL.NtAddBootEntry
@ stdcall NtAddDriverEntry(ptr long) ; 5.2 and higher NTDLL.NtAddDriverEntry
@ stdcall NtAdjustGroupsToken(long long ptr long ptr ptr) NTDLL.NtAdjustGroupsToken
@ stdcall NtAdjustPrivilegesToken(long long long long long long) NTDLL.NtAdjustPrivilegesToken
@ stdcall NtAlertResumeThread(long ptr) NTDLL.NtAlertResumeThread
@ stdcall NtAlertThread(long) NTDLL.NtAlertThread
@ stdcall NtAllocateLocallyUniqueId(ptr) NTDLL.NtAllocateLocallyUniqueId
@ stdcall NtAllocateUserPhysicalPages(ptr ptr ptr) NTDLL.NtAllocateUserPhysicalPages
@ stdcall NtAllocateUuids(ptr ptr ptr ptr) NTDLL.NtAllocateUuids
@ stdcall NtAllocateVirtualMemory(long ptr ptr ptr long long) NTDLL.NtAllocateVirtualMemory
@ stdcall NtApphelpCacheControl(long ptr) NTDLL.NtApphelpCacheControl
@ stdcall NtAreMappedFilesTheSame(ptr ptr) NTDLL.NtAreMappedFilesTheSame
@ stdcall NtAssignProcessToJobObject(long long) NTDLL.NtAssignProcessToJobObject
@ stdcall NtCallbackReturn(ptr long long) NTDLL.NtCallbackReturn
@ stdcall NtCancelDeviceWakeupRequest(ptr) NTDLL.NtCancelDeviceWakeupRequest
@ stdcall NtCancelIoFile(long ptr) NTDLL.NtCancelIoFile
@ stdcall NtCancelTimer(long ptr) NTDLL.NtCancelTimer
@ stdcall NtClearEvent(long) NTDLL.NtClearEvent
@ stdcall NtClose(long) NTDLL.NtClose
@ stdcall NtCloseObjectAuditAlarm(ptr ptr long) NTDLL.NtCloseObjectAuditAlarm
@ stdcall NtCompactKeys(long ptr) NTDLL.NtCompactKeys
@ stdcall NtCompareTokens(ptr ptr ptr) NTDLL.NtCompareTokens
@ stdcall NtCompleteConnectPort(ptr) NTDLL.NtCompleteConnectPort
@ stdcall NtCompressKey(ptr) NTDLL.NtCompressKey
@ stdcall NtConnectPort(ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.NtConnectPort
@ stdcall NtContinue(ptr long) NTDLL.NtContinue
@ stdcall NtCreateDebugObject(ptr long ptr long) NTDLL.NtCreateDebugObject
@ stdcall NtCreateDirectoryObject(long long long) NTDLL.NtCreateDirectoryObject
@ stdcall NtCreateEvent(long long long long long) NTDLL.NtCreateEvent
@ stdcall NtCreateEventPair(ptr long ptr) NTDLL.NtCreateEventPair
@ stdcall NtCreateFile(ptr long ptr ptr long long long ptr long long ptr) NTDLL.NtCreateFile
@ stdcall NtCreateIoCompletion(ptr long ptr long) NTDLL.NtCreateIoCompletion
@ stdcall NtCreateJobObject(ptr long ptr) NTDLL.NtCreateJobObject
@ stdcall NtCreateJobSet(long ptr long) NTDLL.NtCreateJobSet
@ stdcall NtCreateKey(ptr long ptr long ptr long long) NTDLL.NtCreateKey
@ stdcall NtCreateKeyedEvent(ptr long ptr long) NTDLL.NtCreateKeyedEvent
@ stdcall NtCreateMailslotFile(long long long long long long long long) NTDLL.NtCreateMailslotFile
@ stdcall NtCreateMutant(ptr long ptr long) NTDLL.NtCreateMutant
@ stdcall NtCreateNamedPipeFile(ptr long ptr ptr long long long long long long long long long ptr) NTDLL.NtCreateNamedPipeFile
@ stdcall NtCreatePagingFile(long long long long) NTDLL.NtCreatePagingFile
@ stdcall NtCreatePort(ptr ptr long long ptr) NTDLL.NtCreatePort
@ stdcall NtCreateProcess(ptr long ptr ptr long ptr ptr ptr) NTDLL.NtCreateProcess
@ stdcall NtCreateProcessEx(ptr long ptr ptr long ptr ptr ptr long) NTDLL.NtCreateProcessEx
@ stdcall NtCreateProfile(ptr ptr ptr long long ptr long long long) ; CHECKME NTDLL.NtCreateProfile
@ stdcall NtCreateSection(ptr long ptr ptr long long long) NTDLL.NtCreateSection
@ stdcall NtCreateSemaphore(ptr long ptr long long) NTDLL.NtCreateSemaphore
@ stdcall NtCreateSymbolicLinkObject(ptr long ptr ptr) NTDLL.NtCreateSymbolicLinkObject
@ stdcall NtCreateThread(ptr long ptr ptr ptr ptr ptr long) NTDLL.NtCreateThread
@ stdcall NtCreateTimer(ptr long ptr long) NTDLL.NtCreateTimer
@ stdcall NtCreateToken(ptr long ptr long ptr ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.NtCreateToken
@ stdcall NtCreateWaitablePort(ptr ptr long long long) NTDLL.NtCreateWaitablePort
@ stdcall -arch=win32 NtCurrentTeb()  NTDLL.NtCurrentTeb
@ stdcall NtDebugActiveProcess(ptr ptr) NTDLL.NtDebugActiveProcess
@ stdcall NtDebugContinue(ptr ptr long) NTDLL.NtDebugContinue
@ stdcall NtDelayExecution(long ptr) NTDLL.NtDelayExecution
@ stdcall NtDeleteAtom(long) NTDLL.NtDeleteAtom
@ stdcall NtDeleteBootEntry(long) NTDLL.NtDeleteBootEntry
@ stdcall NtDeleteDriverEntry(long) NTDLL.NtDeleteDriverEntry
@ stdcall NtDeleteFile(ptr) NTDLL.NtDeleteFile
@ stdcall NtDeleteKey(long) NTDLL.NtDeleteKey
@ stdcall NtDeleteObjectAuditAlarm(ptr ptr long) NTDLL.NtDeleteObjectAuditAlarm
@ stdcall NtDeleteValueKey(long ptr) NTDLL.NtDeleteValueKey
@ stdcall NtDeviceIoControlFile(long long long long long long long long long long) NTDLL.NtDeviceIoControlFile
@ stdcall NtDisplayString(ptr) NTDLL.NtDisplayString
@ stdcall NtDuplicateObject(long long long ptr long long long) NTDLL.NtDuplicateObject
@ stdcall NtDuplicateToken(long long long long long long) NTDLL.NtDuplicateToken
@ stdcall NtEnumerateBootEntries(ptr ptr) NTDLL.NtEnumerateBootEntries
@ stdcall NtEnumerateDriverEntries(ptr ptr) NTDLL.NtEnumerateDriverEntries
@ stdcall NtEnumerateKey (long long long long long long) NTDLL.NtEnumerateKey
@ stdcall NtEnumerateSystemEnvironmentValuesEx(long ptr long) NTDLL.NtEnumerateSystemEnvironmentValuesEx
@ stdcall NtEnumerateValueKey(long long long long long long) NTDLL.NtEnumerateValueKey
@ stdcall NtExtendSection(ptr ptr) NTDLL.NtExtendSection
@ stdcall NtFilterToken(ptr long ptr ptr ptr ptr) NTDLL.NtFilterToken
@ stdcall NtFindAtom(ptr long ptr) NTDLL.NtFindAtom
@ stdcall NtFlushBuffersFile(long ptr) NTDLL.NtFlushBuffersFile
@ stdcall NtFlushInstructionCache(long ptr long) NTDLL.NtFlushInstructionCache
@ stdcall NtFlushKey(long) NTDLL.NtFlushKey
@ stdcall NtFlushVirtualMemory(long ptr ptr long) NTDLL.NtFlushVirtualMemory
@ stdcall NtFlushWriteBuffer() NTDLL.NtFlushWriteBuffer
@ stdcall NtFreeUserPhysicalPages(ptr ptr ptr) NTDLL.NtFreeUserPhysicalPages
@ stdcall NtFreeVirtualMemory(long ptr ptr long) NTDLL.NtFreeVirtualMemory
@ stdcall NtFsControlFile(long long long long long long long long long long) NTDLL.NtFsControlFile
@ stdcall NtGetContextThread(long ptr) NTDLL.NtGetContextThread
@ stdcall NtGetCurrentProcessorNumber() ; 5.2 and higher NTDLL.NtGetCurrentProcessorNumber
@ stdcall NtGetDevicePowerState(ptr ptr) NTDLL.NtGetDevicePowerState
@ stdcall NtGetPlugPlayEvent(long long ptr long) NTDLL.NtGetPlugPlayEvent
@ stdcall NtGetTickCount()  NTDLL.NtGetTickCount
@ stdcall NtGetWriteWatch(long long ptr long ptr ptr ptr) NTDLL.NtGetWriteWatch
@ stdcall NtImpersonateAnonymousToken(ptr) NTDLL.NtImpersonateAnonymousToken
@ stdcall NtImpersonateClientOfPort(ptr ptr) NTDLL.NtImpersonateClientOfPort
@ stdcall NtImpersonateThread(ptr ptr ptr) NTDLL.NtImpersonateThread
@ stdcall NtInitializeRegistry(long) NTDLL.NtInitializeRegistry
@ stdcall NtInitiatePowerAction (long long long long) NTDLL.NtInitiatePowerAction
@ stdcall NtIsProcessInJob(long long) NTDLL.NtIsProcessInJob
@ stdcall NtIsSystemResumeAutomatic() NTDLL.NtIsSystemResumeAutomatic
@ stdcall NtListenPort(ptr ptr) NTDLL.NtListenPort
@ stdcall NtLoadDriver(ptr) NTDLL.NtLoadDriver
@ stdcall NtLoadKey2(ptr ptr long) NTDLL.NtLoadKey2
@ stdcall NtLoadKey(ptr ptr) NTDLL.NtLoadKey
@ stdcall NtLoadKeyEx(ptr ptr long ptr) NTDLL.NtLoadKeyEx
@ stdcall NtLockFile(long long ptr ptr ptr ptr ptr ptr long long) NTDLL.NtLockFile
@ stdcall NtLockProductActivationKeys(ptr ptr) NTDLL.NtLockProductActivationKeys
@ stdcall NtLockRegistryKey(ptr) NTDLL.NtLockRegistryKey
@ stdcall NtLockVirtualMemory(long ptr ptr long) NTDLL.NtLockVirtualMemory
@ stdcall NtMakePermanentObject(ptr) NTDLL.NtMakePermanentObject
@ stdcall NtMakeTemporaryObject(long) NTDLL.NtMakeTemporaryObject
@ stdcall NtMapUserPhysicalPages(ptr ptr ptr) NTDLL.NtMapUserPhysicalPages
@ stdcall NtMapUserPhysicalPagesScatter(ptr ptr ptr) NTDLL.NtMapUserPhysicalPagesScatter
@ stdcall NtMapViewOfSection(long long ptr long long ptr ptr long long long) NTDLL.NtMapViewOfSection
@ stdcall NtModifyBootEntry(ptr) NTDLL.NtModifyBootEntry
@ stdcall NtModifyDriverEntry(ptr) NTDLL.NtModifyDriverEntry
@ stdcall NtNotifyChangeDirectoryFile(long long ptr ptr ptr ptr long long long) NTDLL.NtNotifyChangeDirectoryFile
@ stdcall NtNotifyChangeKey(long long ptr ptr ptr long long ptr long long) NTDLL.NtNotifyChangeKey
@ stdcall NtNotifyChangeMultipleKeys(ptr long ptr ptr ptr ptr ptr long long ptr long long) NTDLL.NtNotifyChangeMultipleKeys
@ stdcall NtOpenDirectoryObject(long long long) NTDLL.NtOpenDirectoryObject
@ stdcall NtOpenEvent(long long long) NTDLL.NtOpenEvent
@ stdcall NtOpenEventPair(ptr long ptr) NTDLL.NtOpenEventPair
@ stdcall NtOpenFile(ptr long ptr ptr long long) NTDLL.NtOpenFile
@ stdcall NtOpenIoCompletion(ptr long ptr) NTDLL.NtOpenIoCompletion
@ stdcall NtOpenJobObject(ptr long ptr) NTDLL.NtOpenJobObject
@ stdcall NtOpenKey(ptr long ptr) NTDLL.NtOpenKey
@ stdcall NtOpenKeyedEvent(ptr long ptr) NTDLL.NtOpenKeyedEvent
@ stdcall NtOpenMutant(ptr long ptr) NTDLL.NtOpenMutant
@ stdcall NtOpenObjectAuditAlarm(ptr ptr ptr ptr ptr ptr long long ptr long long ptr) NTDLL.NtOpenObjectAuditAlarm
@ stdcall NtOpenProcess(ptr long ptr ptr) NTDLL.NtOpenProcess
@ stdcall NtOpenProcessToken(long long ptr) NTDLL.NtOpenProcessToken
@ stdcall NtOpenProcessTokenEx(long long long ptr) NTDLL.NtOpenProcessTokenEx
@ stdcall NtOpenSection(ptr long ptr) NTDLL.NtOpenSection
@ stdcall NtOpenSemaphore(long long ptr) NTDLL.NtOpenSemaphore
@ stdcall NtOpenSymbolicLinkObject (ptr long ptr) NTDLL.NtOpenSymbolicLinkObject
@ stdcall NtOpenThread(ptr long ptr ptr) NTDLL.NtOpenThread
@ stdcall NtOpenThreadToken(long long long ptr) NTDLL.NtOpenThreadToken
@ stdcall NtOpenThreadTokenEx(long long long long ptr) NTDLL.NtOpenThreadTokenEx
@ stdcall NtOpenTimer(ptr long ptr) NTDLL.NtOpenTimer
@ stdcall NtPlugPlayControl(ptr ptr long) NTDLL.NtPlugPlayControl
@ stdcall NtPowerInformation(long ptr long ptr long) NTDLL.NtPowerInformation
@ stdcall NtPrivilegeCheck(ptr ptr ptr) NTDLL.NtPrivilegeCheck
@ stdcall NtPrivilegeObjectAuditAlarm(ptr ptr ptr long ptr long) NTDLL.NtPrivilegeObjectAuditAlarm
@ stdcall NtPrivilegedServiceAuditAlarm(ptr ptr ptr ptr long) NTDLL.NtPrivilegedServiceAuditAlarm
@ stdcall NtProtectVirtualMemory(long ptr ptr long ptr) NTDLL.NtProtectVirtualMemory
@ stdcall NtPulseEvent(long ptr) NTDLL.NtPulseEvent
@ stdcall NtQueryAttributesFile(ptr ptr) NTDLL.NtQueryAttributesFile
@ stdcall NtQueryBootEntryOrder(ptr ptr) NTDLL.NtQueryBootEntryOrder
@ stdcall NtQueryBootOptions(ptr ptr) NTDLL.NtQueryBootOptions
@ stdcall NtQueryDebugFilterState(long long) NTDLL.NtQueryDebugFilterState
@ stdcall NtQueryDefaultLocale(long ptr) NTDLL.NtQueryDefaultLocale
@ stdcall NtQueryDefaultUILanguage(ptr) NTDLL.NtQueryDefaultUILanguage
@ stdcall NtQueryDirectoryFile(long long ptr ptr ptr ptr long long long ptr long) NTDLL.NtQueryDirectoryFile
@ stdcall NtQueryDirectoryObject(long ptr long long long ptr ptr) NTDLL.NtQueryDirectoryObject
@ stdcall NtQueryDriverEntryOrder(ptr ptr) NTDLL.NtQueryDriverEntryOrder
@ stdcall NtQueryEaFile(long ptr ptr long long ptr long ptr long) NTDLL.NtQueryEaFile
@ stdcall NtQueryEvent(long long ptr long ptr) NTDLL.NtQueryEvent
@ stdcall NtQueryFullAttributesFile(ptr ptr) NTDLL.NtQueryFullAttributesFile
@ stdcall NtQueryInformationAtom(long long ptr long ptr) NTDLL.NtQueryInformationAtom
@ stdcall NtQueryInformationFile(long ptr ptr long long) NTDLL.NtQueryInformationFile
@ stdcall NtQueryInformationJobObject(long long ptr long ptr) NTDLL.NtQueryInformationJobObject
@ stdcall NtQueryInformationPort(ptr long ptr long ptr) NTDLL.NtQueryInformationPort
@ stdcall NtQueryInformationProcess(long long ptr long ptr) NTDLL.NtQueryInformationProcess
@ stdcall NtQueryInformationThread(long long ptr long ptr) NTDLL.NtQueryInformationThread
@ stdcall NtQueryInformationToken(long long ptr long ptr) NTDLL.NtQueryInformationToken
@ stdcall NtQueryInstallUILanguage(ptr) NTDLL.NtQueryInstallUILanguage
@ stdcall NtQueryIntervalProfile(long ptr) NTDLL.NtQueryIntervalProfile
@ stdcall NtQueryIoCompletion(long long ptr long ptr) NTDLL.NtQueryIoCompletion
@ stdcall NtQueryKey (long long ptr long ptr) NTDLL.NtQueryKey
@ stdcall NtQueryMultipleValueKey(long ptr long ptr long ptr) NTDLL.NtQueryMultipleValueKey
@ stdcall NtQueryMutant(long long ptr long ptr) NTDLL.NtQueryMutant
@ stdcall NtQueryObject(long long long long long) NTDLL.NtQueryObject
@ stdcall NtQueryOpenSubKeys(ptr ptr) NTDLL.NtQueryOpenSubKeys
@ stdcall NtQueryOpenSubKeysEx(ptr long ptr ptr) NTDLL.NtQueryOpenSubKeysEx
@ stdcall NtQueryPerformanceCounter(ptr ptr) NTDLL.NtQueryPerformanceCounter
@ stdcall NtQueryPortInformationProcess() NTDLL.NtQueryPortInformationProcess
@ stdcall NtQueryQuotaInformationFile(ptr ptr ptr long long ptr long ptr long) NTDLL.NtQueryQuotaInformationFile
@ stdcall NtQuerySection (long long long long long) NTDLL.NtQuerySection
@ stdcall NtQuerySecurityObject (long long long long long) NTDLL.NtQuerySecurityObject
@ stdcall NtQuerySemaphore (long long ptr long ptr) NTDLL.NtQuerySemaphore
@ stdcall NtQuerySymbolicLinkObject(long ptr ptr) NTDLL.NtQuerySymbolicLinkObject
@ stdcall NtQuerySystemEnvironmentValue(ptr ptr long ptr) NTDLL.NtQuerySystemEnvironmentValue
@ stdcall NtQuerySystemEnvironmentValueEx(ptr ptr ptr ptr ptr) NTDLL.NtQuerySystemEnvironmentValueEx
@ stdcall NtQuerySystemInformation(long long long long) NTDLL.NtQuerySystemInformation
@ stdcall NtQuerySystemTime(ptr) NTDLL.NtQuerySystemTime
@ stdcall NtQueryTimer(ptr long ptr long ptr) NTDLL.NtQueryTimer
@ stdcall NtQueryTimerResolution(long long long) NTDLL.NtQueryTimerResolution
@ stdcall NtQueryValueKey(long long long long long long) NTDLL.NtQueryValueKey
@ stdcall NtQueryVirtualMemory(long ptr long ptr long ptr) NTDLL.NtQueryVirtualMemory
@ stdcall NtQueryVolumeInformationFile(long ptr ptr long long) NTDLL.NtQueryVolumeInformationFile
@ stdcall NtQueueApcThread(long ptr long long long) NTDLL.NtQueueApcThread
@ stdcall NtRaiseException(ptr ptr long) NTDLL.NtRaiseException
@ stdcall NtRaiseHardError(long long long ptr long ptr) NTDLL.NtRaiseHardError
@ stdcall NtReadFile(long long ptr ptr ptr ptr long ptr ptr) NTDLL.NtReadFile
@ stdcall NtReadFileScatter(long long ptr ptr ptr ptr long ptr ptr) NTDLL.NtReadFileScatter
@ stdcall NtReadRequestData(ptr ptr long ptr long ptr) NTDLL.NtReadRequestData
@ stdcall NtReadVirtualMemory(long ptr ptr long ptr) NTDLL.NtReadVirtualMemory
@ stdcall NtRegisterThreadTerminatePort(ptr) NTDLL.NtRegisterThreadTerminatePort
@ stdcall NtReleaseKeyedEvent(ptr ptr long ptr) NTDLL.NtReleaseKeyedEvent
@ stdcall NtReleaseMutant(long ptr) NTDLL.NtReleaseMutant
@ stdcall NtReleaseSemaphore(long long ptr) NTDLL.NtReleaseSemaphore
@ stdcall NtRemoveIoCompletion(ptr ptr ptr ptr ptr) NTDLL.NtRemoveIoCompletion
@ stdcall NtRemoveProcessDebug(ptr ptr) NTDLL.NtRemoveProcessDebug
@ stdcall NtRenameKey(ptr ptr) NTDLL.NtRenameKey
@ stdcall NtReplaceKey(ptr long ptr) NTDLL.NtReplaceKey
@ stdcall NtReplyPort(ptr ptr) NTDLL.NtReplyPort
@ stdcall NtReplyWaitReceivePort(ptr ptr ptr ptr) NTDLL.NtReplyWaitReceivePort
@ stdcall NtReplyWaitReceivePortEx(ptr ptr ptr ptr ptr) NTDLL.NtReplyWaitReceivePortEx
@ stdcall NtReplyWaitReplyPort(ptr ptr) NTDLL.NtReplyWaitReplyPort
@ stdcall NtRequestDeviceWakeup(ptr) NTDLL.NtRequestDeviceWakeup
@ stdcall NtRequestPort(ptr ptr) NTDLL.NtRequestPort
@ stdcall NtRequestWaitReplyPort(ptr ptr ptr) NTDLL.NtRequestWaitReplyPort
@ stdcall NtRequestWakeupLatency(long) NTDLL.NtRequestWakeupLatency
@ stdcall NtResetEvent(long ptr) NTDLL.NtResetEvent
@ stdcall NtResetWriteWatch(long ptr long) NTDLL.NtResetWriteWatch
@ stdcall NtRestoreKey(long long long) NTDLL.NtRestoreKey
@ stdcall NtResumeProcess(ptr) NTDLL.NtResumeProcess
@ stdcall NtResumeThread(long long) NTDLL.NtResumeThread
@ stdcall NtSaveKey(long long) NTDLL.NtSaveKey
@ stdcall NtSaveKeyEx(ptr ptr long) NTDLL.NtSaveKeyEx
@ stdcall NtSaveMergedKeys(ptr ptr ptr) NTDLL.NtSaveMergedKeys
@ stdcall NtSecureConnectPort(ptr ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.NtSecureConnectPort
@ stdcall NtSetBootEntryOrder(ptr ptr) NTDLL.NtSetBootEntryOrder
@ stdcall NtSetBootOptions(ptr long) NTDLL.NtSetBootOptions
@ stdcall NtSetContextThread(long ptr) NTDLL.NtSetContextThread
@ stdcall NtSetDebugFilterState(long long long) NTDLL.NtSetDebugFilterState
@ stdcall NtSetDefaultHardErrorPort(ptr) NTDLL.NtSetDefaultHardErrorPort
@ stdcall NtSetDefaultLocale(long long) NTDLL.NtSetDefaultLocale
@ stdcall NtSetDefaultUILanguage(long) NTDLL.NtSetDefaultUILanguage
@ stdcall NtSetDriverEntryOrder(ptr ptr) NTDLL.NtSetDriverEntryOrder
@ stdcall NtSetEaFile(long ptr ptr long) NTDLL.NtSetEaFile
@ stdcall NtSetEvent(long long) NTDLL.NtSetEvent
@ stdcall NtSetEventBoostPriority(ptr) NTDLL.NtSetEventBoostPriority
@ stdcall NtSetHighEventPair(ptr) NTDLL.NtSetHighEventPair
@ stdcall NtSetHighWaitLowEventPair(ptr) NTDLL.NtSetHighWaitLowEventPair
@ stdcall NtSetInformationDebugObject(ptr long ptr long ptr) NTDLL.NtSetInformationDebugObject
@ stdcall NtSetInformationFile(long long long long long) NTDLL.NtSetInformationFile
@ stdcall NtSetInformationJobObject(long long ptr long) NTDLL.NtSetInformationJobObject
@ stdcall NtSetInformationKey(long long ptr long) NTDLL.NtSetInformationKey
@ stdcall NtSetInformationObject(long long ptr long) NTDLL.NtSetInformationObject
@ stdcall NtSetInformationProcess(long long long long) NTDLL.NtSetInformationProcess
@ stdcall NtSetInformationThread(long long ptr long) NTDLL.NtSetInformationThread
@ stdcall NtSetInformationToken(long long ptr long) NTDLL.NtSetInformationToken
@ stdcall NtSetIntervalProfile(long long) NTDLL.NtSetIntervalProfile
@ stdcall NtSetIoCompletion(ptr long ptr long long) NTDLL.NtSetIoCompletion
@ stdcall NtSetLdtEntries(long int64 long int64) NTDLL.NtSetLdtEntries
@ stdcall NtSetLowEventPair(ptr) NTDLL.NtSetLowEventPair
@ stdcall NtSetLowWaitHighEventPair(ptr) NTDLL.NtSetLowWaitHighEventPair
@ stdcall NtSetQuotaInformationFile(ptr ptr ptr long) NTDLL.NtSetQuotaInformationFile
@ stdcall NtSetSecurityObject(long long ptr) NTDLL.NtSetSecurityObject
@ stdcall NtSetSystemEnvironmentValue(ptr ptr) NTDLL.NtSetSystemEnvironmentValue
@ stdcall NtSetSystemEnvironmentValueEx(ptr ptr ptr ptr ptr) NTDLL.NtSetSystemEnvironmentValueEx
@ stdcall NtSetSystemInformation(long ptr long) NTDLL.NtSetSystemInformation
@ stdcall NtSetSystemPowerState(long long long) NTDLL.NtSetSystemPowerState
@ stdcall NtSetSystemTime(ptr ptr) NTDLL.NtSetSystemTime
@ stdcall NtSetThreadExecutionState(long ptr) NTDLL.NtSetThreadExecutionState
@ stdcall NtSetTimer(long ptr ptr ptr long long ptr) NTDLL.NtSetTimer
@ stdcall NtSetTimerResolution(long long ptr) NTDLL.NtSetTimerResolution
@ stdcall NtSetUuidSeed(ptr) NTDLL.NtSetUuidSeed
@ stdcall NtSetValueKey(long long long long long long) NTDLL.NtSetValueKey
@ stdcall NtSetVolumeInformationFile(long ptr ptr long long) NTDLL.NtSetVolumeInformationFile
@ stdcall NtShutdownSystem(long) NTDLL.NtShutdownSystem
@ stdcall NtSignalAndWaitForSingleObject(long long long ptr) NTDLL.NtSignalAndWaitForSingleObject
@ stdcall NtStartProfile(ptr) NTDLL.NtStartProfile
@ stdcall NtStopProfile(ptr) NTDLL.NtStopProfile
@ stdcall NtSuspendProcess(ptr) NTDLL.NtSuspendProcess
@ stdcall NtSuspendThread(long ptr) NTDLL.NtSuspendThread
@ stdcall NtSystemDebugControl(long ptr long ptr long ptr) NTDLL.NtSystemDebugControl
@ stdcall NtTerminateJobObject(long long) NTDLL.NtTerminateJobObject
@ stdcall NtTerminateProcess(long long) NTDLL.NtTerminateProcess
@ stdcall NtTerminateThread(long long) NTDLL.NtTerminateThread
@ stdcall NtTestAlert() NTDLL.NtTestAlert
@ stdcall NtTraceEvent(long long long ptr) NTDLL.NtTraceEvent
@ stdcall NtTranslateFilePath(ptr long ptr long) NTDLL.NtTranslateFilePath
@ stdcall NtUnloadDriver(ptr) NTDLL.NtUnloadDriver
@ stdcall NtUnloadKey2(ptr long) NTDLL.NtUnloadKey2
@ stdcall NtUnloadKey(long) NTDLL.NtUnloadKey
@ stdcall NtUnloadKeyEx(ptr ptr) NTDLL.NtUnloadKeyEx
@ stdcall NtUnlockFile(long ptr ptr ptr ptr) NTDLL.NtUnlockFile
@ stdcall NtUnlockVirtualMemory(long ptr ptr long) NTDLL.NtUnlockVirtualMemory
@ stdcall NtUnmapViewOfSection(long ptr) NTDLL.NtUnmapViewOfSection
@ stdcall NtVdmControl(long ptr) NTDLL.NtVdmControl
@ stdcall NtWaitForDebugEvent(ptr long ptr ptr) NTDLL.NtWaitForDebugEvent
@ stdcall NtWaitForKeyedEvent(ptr ptr long ptr) NTDLL.NtWaitForKeyedEvent
@ stdcall NtWaitForMultipleObjects32(long ptr long long ptr) NTDLL.NtWaitForMultipleObjects32
@ stdcall NtWaitForMultipleObjects(long ptr long long ptr) NTDLL.NtWaitForMultipleObjects
@ stdcall NtWaitForSingleObject(long long long) NTDLL.NtWaitForSingleObject
@ stdcall NtWaitHighEventPair(ptr) NTDLL.NtWaitHighEventPair
@ stdcall NtWaitLowEventPair(ptr) NTDLL.NtWaitLowEventPair
@ stdcall NtWriteFile(long long ptr ptr ptr ptr long ptr ptr) NTDLL.NtWriteFile
@ stdcall NtWriteFileGather(long long ptr ptr ptr ptr long ptr ptr) NTDLL.NtWriteFileGather
@ stdcall NtWriteRequestData(ptr ptr long ptr long ptr) NTDLL.NtWriteRequestData
@ stdcall NtWriteVirtualMemory(long ptr ptr long ptr) NTDLL.NtWriteVirtualMemory
@ stdcall NtYieldExecution() NTDLL.NtYieldExecution
@ stdcall RtlAbortRXact(ptr) NTDLL.RtlAbortRXact
@ stdcall RtlAbsoluteToSelfRelativeSD(ptr ptr ptr) NTDLL.RtlAbsoluteToSelfRelativeSD
@ stdcall RtlAcquirePebLock() NTDLL.RtlAcquirePebLock
@ stdcall RtlAcquirePrivilege(ptr long long ptr) NTDLL.RtlAcquirePrivilege
@ stdcall RtlAcquireResourceExclusive(ptr long) NTDLL.RtlAcquireResourceExclusive
@ stdcall RtlAcquireResourceShared(ptr long) NTDLL.RtlAcquireResourceShared
@ stdcall RtlActivateActivationContext(long ptr ptr) NTDLL.RtlActivateActivationContext
@ stdcall RtlActivateActivationContextEx(long ptr ptr ptr) NTDLL.RtlActivateActivationContextEx
@ stdcall RtlAddAccessAllowedAce(ptr long long ptr) NTDLL.RtlAddAccessAllowedAce
@ stdcall RtlAddAccessAllowedAceEx(ptr long long long ptr) NTDLL.RtlAddAccessAllowedAceEx
@ stdcall RtlAddAccessAllowedObjectAce(ptr long long long ptr ptr ptr) NTDLL.RtlAddAccessAllowedObjectAce
@ stdcall RtlAddAccessDeniedAce(ptr long long ptr) NTDLL.RtlAddAccessDeniedAce
@ stdcall RtlAddAccessDeniedAceEx(ptr long long long ptr) NTDLL.RtlAddAccessDeniedAceEx
@ stdcall RtlAddAccessDeniedObjectAce(ptr long long long ptr ptr ptr) NTDLL.RtlAddAccessDeniedObjectAce
@ stdcall RtlAddAce(ptr long long ptr long) NTDLL.RtlAddAce
@ stdcall RtlAddActionToRXact(ptr long ptr long ptr long) NTDLL.RtlAddActionToRXact
@ stdcall RtlAddAtomToAtomTable(ptr wstr ptr) NTDLL.RtlAddAtomToAtomTable
@ stdcall RtlAddAttributeActionToRXact(ptr long ptr ptr ptr long ptr long) NTDLL.RtlAddAttributeActionToRXact
@ stdcall RtlAddAuditAccessAce(ptr long long ptr long long) NTDLL.RtlAddAuditAccessAce
@ stdcall RtlAddAuditAccessAceEx(ptr long long long ptr long long) NTDLL.RtlAddAuditAccessAceEx
@ stdcall RtlAddAuditAccessObjectAce(ptr long long long ptr ptr ptr long long) NTDLL.RtlAddAuditAccessObjectAce
@ stdcall -arch=x86_64 RtlAddFunctionTable(ptr long long) NTDLL.RtlAddFunctionTable
@ stdcall RtlAddRefActivationContext(ptr) NTDLL.RtlAddRefActivationContext
@ stdcall RtlAddRefMemoryStream(ptr) NTDLL.RtlAddRefMemoryStream
@ stdcall RtlAddVectoredContinueHandler(long ptr) NTDLL.RtlAddVectoredContinueHandler
@ stdcall RtlAddVectoredExceptionHandler(long ptr) NTDLL.RtlAddVectoredExceptionHandler
@ stdcall RtlAdjustPrivilege(long long long ptr) NTDLL.RtlAdjustPrivilege
@ stdcall RtlAllocateActivationContextStack(ptr) ; CHECKME NTDLL.RtlAllocateActivationContextStack
@ stdcall RtlAllocateAndInitializeSid(ptr long long long long long long long long long ptr) NTDLL.RtlAllocateAndInitializeSid
@ stdcall RtlAllocateHandle(ptr ptr) NTDLL.RtlAllocateHandle
@ stdcall RtlAllocateHeap(ptr long ptr) NTDLL.RtlAllocateHeap
@ stdcall RtlAnsiCharToUnicodeChar(ptr) NTDLL.RtlAnsiCharToUnicodeChar
@ stdcall RtlAnsiStringToUnicodeSize(ptr)  NTDLL.RtlAnsiStringToUnicodeSize
@ stdcall RtlAnsiStringToUnicodeString(ptr ptr long) NTDLL.RtlAnsiStringToUnicodeString
@ stdcall RtlAppendAsciizToString(ptr str) NTDLL.RtlAppendAsciizToString
@ stdcall RtlAppendStringToString(ptr ptr) NTDLL.RtlAppendStringToString
@ stdcall RtlAppendUnicodeStringToString(ptr ptr) NTDLL.RtlAppendUnicodeStringToString
@ stdcall RtlAppendUnicodeToString(ptr wstr) NTDLL.RtlAppendUnicodeToString
@ stdcall RtlApplicationVerifierStop(ptr str ptr str ptr str ptr str ptr str) NTDLL.RtlApplicationVerifierStop
@ stdcall RtlApplyRXact(ptr) NTDLL.RtlApplyRXact
@ stdcall RtlApplyRXactNoFlush(ptr) NTDLL.RtlApplyRXactNoFlush
@ stdcall RtlAreAllAccessesGranted(long long) NTDLL.RtlAreAllAccessesGranted
@ stdcall RtlAreAnyAccessesGranted(long long) NTDLL.RtlAreAnyAccessesGranted
@ stdcall RtlAreBitsClear(ptr long long) NTDLL.RtlAreBitsClear
@ stdcall RtlAreBitsSet(ptr long long) NTDLL.RtlAreBitsSet
@ stdcall RtlAssert(ptr ptr long ptr) NTDLL.RtlAssert
@ stdcall -register RtlCaptureContext(ptr) NTDLL.RtlCaptureContext
@ stdcall RtlCaptureStackBackTrace(long long ptr ptr) NTDLL.RtlCaptureStackBackTrace
@ stdcall RtlCharToInteger(ptr long ptr) NTDLL.RtlCharToInteger
@ stdcall RtlCheckForOrphanedCriticalSections(ptr) NTDLL.RtlCheckForOrphanedCriticalSections
@ stdcall RtlCheckRegistryKey(long ptr) NTDLL.RtlCheckRegistryKey
@ stdcall RtlClearAllBits(ptr) NTDLL.RtlClearAllBits
@ stdcall RtlClearBits(ptr long long) NTDLL.RtlClearBits
@ stdcall RtlCloneMemoryStream(ptr ptr) NTDLL.RtlCloneMemoryStream
@ stdcall RtlCommitMemoryStream(ptr long) NTDLL.RtlCommitMemoryStream
@ stdcall RtlCompactHeap(long long) NTDLL.RtlCompactHeap
@ stdcall RtlCompareMemory(ptr ptr long) NTDLL.RtlCompareMemory
@ stdcall RtlCompareMemoryUlong(ptr long long) NTDLL.RtlCompareMemoryUlong
@ stdcall RtlCompareString(ptr ptr long) NTDLL.RtlCompareString
@ stdcall RtlCompareUnicodeString (ptr ptr long) NTDLL.RtlCompareUnicodeString
@ stdcall RtlCompressBuffer(long ptr long ptr long long ptr ptr) NTDLL.RtlCompressBuffer
@ stdcall RtlComputeCrc32(long ptr long) NTDLL.RtlComputeCrc32
@ stdcall RtlComputeImportTableHash(ptr ptr long) NTDLL.RtlComputeImportTableHash
@ stdcall RtlComputePrivatizedDllName_U(ptr ptr ptr) NTDLL.RtlComputePrivatizedDllName_U
@ stdcall RtlConsoleMultiByteToUnicodeN(ptr long ptr ptr long ptr) NTDLL.RtlConsoleMultiByteToUnicodeN
@ stdcall RtlConvertExclusiveToShared(ptr) NTDLL.RtlConvertExclusiveToShared
@ stdcall -arch=win32 -ret64 RtlConvertLongToLargeInteger(long) NTDLL.RtlConvertLongToLargeInteger
@ stdcall RtlConvertSharedToExclusive(ptr) NTDLL.RtlConvertSharedToExclusive
@ stdcall RtlConvertSidToUnicodeString(ptr ptr long) NTDLL.RtlConvertSidToUnicodeString
@ stdcall RtlConvertToAutoInheritSecurityObject(ptr ptr ptr ptr long ptr) NTDLL.RtlConvertToAutoInheritSecurityObject
@ stdcall RtlConvertUiListToApiList(ptr ptr long) NTDLL.RtlConvertUiListToApiList
@ stdcall -arch=win32 -ret64 RtlConvertUlongToLargeInteger(long) NTDLL.RtlConvertUlongToLargeInteger
@ stdcall RtlCopyLuid(ptr ptr) NTDLL.RtlCopyLuid
@ stdcall RtlCopyLuidAndAttributesArray(long ptr ptr) NTDLL.RtlCopyLuidAndAttributesArray
@ stdcall RtlCopyMappedMemory(ptr ptr long) NTDLL.RtlCopyMappedMemory
@ stdcall RtlCopyMemoryStreamTo(ptr ptr int64 ptr ptr) NTDLL.RtlCopyMemoryStreamTo
@ stdcall RtlCopyOutOfProcessMemoryStreamTo(ptr ptr int64 ptr ptr)  NTDLL.RtlCopyOutOfProcessMemoryStreamTo
@ stdcall RtlCopySecurityDescriptor(ptr ptr) NTDLL.RtlCopySecurityDescriptor
@ stdcall RtlCopySid(long ptr ptr) NTDLL.RtlCopySid
@ stdcall RtlCopySidAndAttributesArray(long ptr long ptr ptr ptr ptr) NTDLL.RtlCopySidAndAttributesArray
@ stdcall RtlCopyString(ptr ptr) NTDLL.RtlCopyString
@ stdcall RtlCopyUnicodeString(ptr ptr) NTDLL.RtlCopyUnicodeString
@ stdcall RtlCreateAcl(ptr long long) NTDLL.RtlCreateAcl
@ stdcall RtlCreateActivationContext(long ptr long ptr ptr ptr) NTDLL.RtlCreateActivationContext
@ stdcall RtlCreateAndSetSD(ptr long ptr ptr ptr) NTDLL.RtlCreateAndSetSD
@ stdcall RtlCreateAtomTable(long ptr) NTDLL.RtlCreateAtomTable
@ stdcall RtlCreateBootStatusDataFile() NTDLL.RtlCreateBootStatusDataFile
@ stdcall RtlCreateEnvironment(long ptr) NTDLL.RtlCreateEnvironment
@ stdcall RtlCreateHeap(long ptr long long ptr ptr) NTDLL.RtlCreateHeap
@ stdcall RtlCreateProcessParameters(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.RtlCreateProcessParameters
@ stdcall RtlCreateQueryDebugBuffer(long long) NTDLL.RtlCreateQueryDebugBuffer
@ stdcall RtlCreateRegistryKey(long wstr) NTDLL.RtlCreateRegistryKey
@ stdcall RtlCreateSecurityDescriptor(ptr long) NTDLL.RtlCreateSecurityDescriptor
@ stdcall RtlCreateSystemVolumeInformationFolder(ptr) NTDLL.RtlCreateSystemVolumeInformationFolder
@ stdcall RtlCreateTagHeap(ptr long str str) NTDLL.RtlCreateTagHeap
@ stdcall RtlCreateTimer(ptr ptr ptr ptr long long long) NTDLL.RtlCreateTimer
@ stdcall RtlCreateTimerQueue(ptr) NTDLL.RtlCreateTimerQueue
@ stdcall RtlCreateUnicodeString(ptr wstr) NTDLL.RtlCreateUnicodeString
@ stdcall RtlCreateUnicodeStringFromAsciiz(ptr str) NTDLL.RtlCreateUnicodeStringFromAsciiz
@ stdcall RtlCreateUserProcess(ptr long ptr ptr ptr ptr long ptr ptr ptr) NTDLL.RtlCreateUserProcess
@ stdcall RtlCreateUserSecurityObject(ptr long ptr ptr long ptr ptr) NTDLL.RtlCreateUserSecurityObject
@ stdcall RtlCreateUserThread(long ptr long ptr long long ptr ptr ptr ptr) NTDLL.RtlCreateUserThread
@ stdcall RtlCustomCPToUnicodeN(ptr wstr long ptr str long) NTDLL.RtlCustomCPToUnicodeN
@ stdcall RtlCutoverTimeToSystemTime(ptr ptr ptr long) NTDLL.RtlCutoverTimeToSystemTime
@ stdcall RtlDeNormalizeProcessParams(ptr) NTDLL.RtlDeNormalizeProcessParams
@ stdcall RtlDeactivateActivationContext(long long) NTDLL.RtlDeactivateActivationContext
@ stdcall RtlDecodePointer(ptr) NTDLL.RtlDecodePointer
@ stdcall RtlDecodeSystemPointer(ptr) NTDLL.RtlDecodeSystemPointer
@ stdcall RtlDecompressBuffer(long ptr long ptr long ptr) NTDLL.RtlDecompressBuffer
@ stdcall RtlDecompressFragment(long ptr long ptr long long ptr ptr) NTDLL.RtlDecompressFragment
@ stdcall RtlDefaultNpAcl(ptr) NTDLL.RtlDefaultNpAcl
@ stdcall RtlDelete(ptr) NTDLL.RtlDelete
@ stdcall RtlDeleteAce(ptr long) NTDLL.RtlDeleteAce
@ stdcall RtlDeleteAtomFromAtomTable(ptr long) NTDLL.RtlDeleteAtomFromAtomTable
@ stdcall RtlDeleteCriticalSection(ptr) NTDLL.RtlDeleteCriticalSection
@ stdcall RtlDeleteElementGenericTable(ptr ptr) NTDLL.RtlDeleteElementGenericTable
@ stdcall RtlDeleteElementGenericTableAvl(ptr ptr) NTDLL.RtlDeleteElementGenericTableAvl
@ cdecl -arch=x86_64 RtlDeleteFunctionTable(ptr) NTDLL.RtlDeleteFunctionTable
@ stdcall RtlDeleteNoSplay(ptr ptr) NTDLL.RtlDeleteNoSplay
@ stdcall RtlDeleteRegistryValue(long ptr ptr) NTDLL.RtlDeleteRegistryValue
@ stdcall RtlDeleteResource(ptr) NTDLL.RtlDeleteResource
@ stdcall RtlDeleteSecurityObject(ptr) NTDLL.RtlDeleteSecurityObject
@ stdcall RtlDeleteTimer(ptr ptr ptr) NTDLL.RtlDeleteTimer
@ stdcall RtlDeleteTimerQueue(ptr) NTDLL.RtlDeleteTimerQueue
@ stdcall RtlDeleteTimerQueueEx(ptr ptr) NTDLL.RtlDeleteTimerQueueEx
@ stdcall RtlDeregisterWait(ptr) NTDLL.RtlDeregisterWait
@ stdcall RtlDeregisterWaitEx(ptr ptr) NTDLL.RtlDeregisterWaitEx
@ stdcall RtlDestroyAtomTable(ptr) NTDLL.RtlDestroyAtomTable
@ stdcall RtlDestroyEnvironment(ptr) NTDLL.RtlDestroyEnvironment
@ stdcall RtlDestroyHandleTable(ptr) NTDLL.RtlDestroyHandleTable
@ stdcall RtlDestroyHeap(long) NTDLL.RtlDestroyHeap
@ stdcall RtlDestroyProcessParameters(ptr) NTDLL.RtlDestroyProcessParameters
@ stdcall RtlDestroyQueryDebugBuffer(ptr) NTDLL.RtlDestroyQueryDebugBuffer
@ stdcall RtlDetermineDosPathNameType_U(wstr) NTDLL.RtlDetermineDosPathNameType_U
@ stdcall RtlDllShutdownInProgress() NTDLL.RtlDllShutdownInProgress
@ stdcall RtlDnsHostNameToComputerName(ptr ptr long) NTDLL.RtlDnsHostNameToComputerName
@ stdcall RtlDoesFileExists_U(wstr) NTDLL.RtlDoesFileExists_U
@ stdcall RtlDosApplyFileIsolationRedirection_Ustr(long ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.RtlDosApplyFileIsolationRedirection_Ustr
@ stdcall RtlDosPathNameToNtPathName_U(wstr ptr ptr ptr) NTDLL.RtlDosPathNameToNtPathName_U
@ stdcall RtlDosPathNameToNtPathName_U_WithStatus(wstr ptr ptr ptr) ; 5.2 SP1, and higher NTDLL.RtlDosPathNameToNtPathName_U_WithStatus
@ stdcall RtlDosPathNameToRelativeNtPathName_U(ptr ptr ptr ptr) NTDLL.RtlDosPathNameToRelativeNtPathName_U
@ stdcall RtlDosPathNameToRelativeNtPathName_U_WithStatus(wstr ptr ptr ptr) NTDLL.RtlDosPathNameToRelativeNtPathName_U_WithStatus
@ stdcall RtlDosSearchPath_U(wstr wstr wstr long ptr ptr) NTDLL.RtlDosSearchPath_U
@ stdcall RtlDosSearchPath_Ustr(long ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.RtlDosSearchPath_Ustr
@ stdcall RtlDowncaseUnicodeChar(long) NTDLL.RtlDowncaseUnicodeChar
@ stdcall RtlDowncaseUnicodeString(ptr ptr long) NTDLL.RtlDowncaseUnicodeString
@ stdcall RtlDumpResource(ptr) NTDLL.RtlDumpResource
@ stdcall RtlDuplicateUnicodeString(long ptr ptr) NTDLL.RtlDuplicateUnicodeString
@ stdcall RtlEmptyAtomTable(ptr long) NTDLL.RtlEmptyAtomTable
@ stdcall RtlEncodePointer(ptr) NTDLL.RtlEncodePointer
@ stdcall RtlEncodeSystemPointer(ptr) NTDLL.RtlEncodeSystemPointer
@ stdcall -arch=win32 -ret64 RtlEnlargedIntegerMultiply(long long) NTDLL.RtlEnlargedIntegerMultiply
@ stdcall -arch=win32 RtlEnlargedUnsignedDivide(double long ptr) NTDLL.RtlEnlargedUnsignedDivide
@ stdcall -arch=win32 -ret64 RtlEnlargedUnsignedMultiply(long long) NTDLL.RtlEnlargedUnsignedMultiply
@ stdcall RtlEnterCriticalSection(ptr) NTDLL.RtlEnterCriticalSection
@ stdcall RtlEnumProcessHeaps(ptr ptr) NTDLL.RtlEnumProcessHeaps
@ stdcall RtlEnumerateGenericTable(ptr long) NTDLL.RtlEnumerateGenericTable
@ stdcall RtlEnumerateGenericTableAvl(ptr long) NTDLL.RtlEnumerateGenericTableAvl
@ stdcall RtlEnumerateGenericTableLikeADirectory(ptr ptr ptr long ptr ptr ptr) NTDLL.RtlEnumerateGenericTableLikeADirectory
@ stdcall RtlEnumerateGenericTableWithoutSplaying(ptr ptr) NTDLL.RtlEnumerateGenericTableWithoutSplaying
@ stdcall RtlEnumerateGenericTableWithoutSplayingAvl(ptr ptr) NTDLL.RtlEnumerateGenericTableWithoutSplayingAvl
@ stdcall RtlEqualComputerName(ptr ptr) NTDLL.RtlEqualComputerName
@ stdcall RtlEqualDomainName(ptr ptr) NTDLL.RtlEqualDomainName
@ stdcall RtlEqualLuid(ptr ptr) NTDLL.RtlEqualLuid
@ stdcall RtlEqualPrefixSid(ptr ptr) NTDLL.RtlEqualPrefixSid
@ stdcall RtlEqualSid(long long) NTDLL.RtlEqualSid
@ stdcall RtlEqualString(ptr ptr long) NTDLL.RtlEqualString
@ stdcall RtlEqualUnicodeString(ptr ptr long) NTDLL.RtlEqualUnicodeString
@ stdcall RtlEraseUnicodeString(ptr) NTDLL.RtlEraseUnicodeString
@ stdcall RtlExitUserThread(long) NTDLL.RtlExitUserThread
@ stdcall RtlExpandEnvironmentStrings_U(ptr ptr ptr ptr) NTDLL.RtlExpandEnvironmentStrings_U
@ stdcall RtlExtendHeap(ptr long ptr ptr) NTDLL.RtlExtendHeap
@ stdcall -arch=win32 -ret64 RtlExtendedIntegerMultiply(double long) NTDLL.RtlExtendedIntegerMultiply
@ stdcall -arch=win32 -ret64 RtlExtendedLargeIntegerDivide(double long ptr) NTDLL.RtlExtendedLargeIntegerDivide
@ stdcall -arch=win32 -ret64 RtlExtendedMagicDivide(double double long) NTDLL.RtlExtendedMagicDivide
@ stdcall RtlFillMemory(ptr long long) NTDLL.RtlFillMemory
@ stdcall RtlFillMemoryUlong(ptr long long) NTDLL.RtlFillMemoryUlong
@ stdcall RtlFinalReleaseOutOfProcessMemoryStream(ptr) NTDLL.RtlFinalReleaseOutOfProcessMemoryStream
@ stdcall RtlFindActivationContextSectionGuid(long ptr long ptr ptr) NTDLL.RtlFindActivationContextSectionGuid
@ stdcall RtlFindActivationContextSectionString(long ptr long ptr ptr) NTDLL.RtlFindActivationContextSectionString
@ stdcall RtlFindCharInUnicodeString(long ptr ptr ptr) NTDLL.RtlFindCharInUnicodeString
@ stdcall RtlFindClearBits(ptr long long) NTDLL.RtlFindClearBits
@ stdcall RtlFindClearBitsAndSet(ptr long long) NTDLL.RtlFindClearBitsAndSet
@ stdcall RtlFindClearRuns(ptr ptr long long) NTDLL.RtlFindClearRuns
@ stdcall RtlFindLastBackwardRunClear(ptr long ptr) NTDLL.RtlFindLastBackwardRunClear
@ stdcall RtlFindLeastSignificantBit(double) NTDLL.RtlFindLeastSignificantBit
@ stdcall RtlFindLongestRunClear(ptr long) NTDLL.RtlFindLongestRunClear
@ stdcall RtlFindMessage(long long long long ptr) NTDLL.RtlFindMessage
@ stdcall RtlFindMostSignificantBit(double) NTDLL.RtlFindMostSignificantBit
@ stdcall RtlFindNextForwardRunClear(ptr long ptr) NTDLL.RtlFindNextForwardRunClear
@ stdcall RtlFindSetBits(ptr long long) NTDLL.RtlFindSetBits
@ stdcall RtlFindSetBitsAndClear(ptr long long) NTDLL.RtlFindSetBitsAndClear
@ stdcall RtlFirstEntrySList(ptr) NTDLL.RtlFirstEntrySList
@ stdcall RtlFirstFreeAce(ptr ptr) NTDLL.RtlFirstFreeAce
@ stdcall RtlFlushSecureMemoryCache(ptr ptr) NTDLL.RtlFlushSecureMemoryCache
@ stdcall RtlFormatCurrentUserKeyPath(ptr) NTDLL.RtlFormatCurrentUserKeyPath
@ stdcall RtlFormatMessage(ptr long long long long ptr ptr long ptr) NTDLL.RtlFormatMessage
@ stdcall RtlFormatMessageEx(ptr long long long long ptr ptr long ptr long) NTDLL.RtlFormatMessageEx
@ stdcall RtlFreeActivationContextStack(ptr) NTDLL.RtlFreeActivationContextStack
@ stdcall RtlFreeAnsiString(long) NTDLL.RtlFreeAnsiString
@ stdcall RtlFreeHandle(ptr ptr) NTDLL.RtlFreeHandle
@ stdcall RtlFreeHeap(long long long) NTDLL.RtlFreeHeap
@ stdcall RtlFreeOemString(ptr) NTDLL.RtlFreeOemString
@ stdcall RtlFreeSid(long) NTDLL.RtlFreeSid
@ stdcall RtlFreeThreadActivationContextStack() NTDLL.RtlFreeThreadActivationContextStack
@ stdcall RtlFreeUnicodeString(ptr) NTDLL.RtlFreeUnicodeString
@ stdcall RtlFreeUserThreadStack(ptr ptr) ; 4.0 to 5.2 only NTDLL.RtlFreeUserThreadStack
@ stdcall RtlGUIDFromString(ptr ptr) NTDLL.RtlGUIDFromString
@ stdcall RtlGenerate8dot3Name(ptr ptr long ptr) NTDLL.RtlGenerate8dot3Name
@ stdcall RtlGetAce(ptr long ptr) NTDLL.RtlGetAce
@ stdcall RtlGetActiveActivationContext(ptr) NTDLL.RtlGetActiveActivationContext
@ stdcall RtlGetCallersAddress(ptr ptr) NTDLL.RtlGetCallersAddress
@ stdcall RtlGetCompressionWorkSpaceSize(long ptr ptr) NTDLL.RtlGetCompressionWorkSpaceSize
@ stdcall RtlGetControlSecurityDescriptor(ptr ptr ptr) NTDLL.RtlGetControlSecurityDescriptor
@ stdcall RtlGetCriticalSectionRecursionCount(ptr) NTDLL.RtlGetCriticalSectionRecursionCount
@ stdcall RtlGetCurrentDirectory_U(long ptr) NTDLL.RtlGetCurrentDirectory_U
@ stdcall RtlGetCurrentPeb() NTDLL.RtlGetCurrentPeb
@ stdcall RtlGetCurrentProcessorNumber() ; 5.2 SP1 and higher NTDLL.RtlGetCurrentProcessorNumber
@ stdcall RtlGetDaclSecurityDescriptor(ptr ptr ptr ptr) NTDLL.RtlGetDaclSecurityDescriptor
@ stdcall RtlGetElementGenericTable(ptr long) NTDLL.RtlGetElementGenericTable
@ stdcall RtlGetElementGenericTableAvl(ptr long) NTDLL.RtlGetElementGenericTableAvl
@ stdcall RtlGetFrame() NTDLL.RtlGetFrame
@ stdcall RtlGetFullPathName_U(wstr long ptr ptr) NTDLL.RtlGetFullPathName_U
@ stdcall RtlGetFullPathName_UstrEx(ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.RtlGetFullPathName_UstrEx
@ stdcall RtlGetGroupSecurityDescriptor(ptr ptr ptr) NTDLL.RtlGetGroupSecurityDescriptor
@ stdcall RtlGetLastNtStatus() NTDLL.RtlGetLastNtStatus
@ stdcall RtlGetLastWin32Error() NTDLL.RtlGetLastWin32Error
@ stdcall RtlGetLengthWithoutLastFullDosOrNtPathElement(long ptr ptr) NTDLL.RtlGetLengthWithoutLastFullDosOrNtPathElement
@ stdcall RtlGetLengthWithoutTrailingPathSeperators(long ptr ptr)  NTDLL.RtlGetLengthWithoutTrailingPathSeperators
@ stdcall RtlGetLongestNtPathLength() NTDLL.RtlGetLongestNtPathLength
@ stdcall RtlGetNativeSystemInformation(long long long long)  NTDLL.RtlGetNativeSystemInformation
@ stdcall RtlGetNtGlobalFlags() NTDLL.RtlGetNtGlobalFlags
@ stdcall RtlGetNtProductType(ptr) NTDLL.RtlGetNtProductType
@ stdcall RtlGetNtVersionNumbers(ptr ptr ptr) NTDLL.RtlGetNtVersionNumbers
@ stdcall RtlGetOwnerSecurityDescriptor(ptr ptr ptr) NTDLL.RtlGetOwnerSecurityDescriptor
@ stdcall RtlGetProcessHeaps(long ptr) NTDLL.RtlGetProcessHeaps
@ stdcall RtlGetSaclSecurityDescriptor(ptr ptr ptr ptr) NTDLL.RtlGetSaclSecurityDescriptor
@ stdcall RtlGetSecurityDescriptorRMControl(ptr ptr) NTDLL.RtlGetSecurityDescriptorRMControl
@ stdcall RtlGetSetBootStatusData(ptr long long ptr long long) NTDLL.RtlGetSetBootStatusData
@ stdcall RtlGetThreadErrorMode() NTDLL.RtlGetThreadErrorMode
@ stdcall RtlGetUserInfoHeap(ptr long ptr ptr ptr) NTDLL.RtlGetUserInfoHeap
@ stdcall RtlGetVersion(ptr) NTDLL.RtlGetVersion
@ stdcall RtlHashUnicodeString(ptr long long ptr) NTDLL.RtlHashUnicodeString
@ stdcall RtlIdentifierAuthoritySid(ptr) NTDLL.RtlIdentifierAuthoritySid
@ stdcall RtlImageDirectoryEntryToData(long long long ptr) NTDLL.RtlImageDirectoryEntryToData
@ stdcall RtlImageNtHeader(long) NTDLL.RtlImageNtHeader
@ stdcall RtlImageNtHeaderEx(long ptr double ptr) NTDLL.RtlImageNtHeaderEx
@ stdcall RtlImageRvaToSection(ptr long long) NTDLL.RtlImageRvaToSection
@ stdcall RtlImageRvaToVa(ptr long long ptr) NTDLL.RtlImageRvaToVa
@ stdcall RtlImpersonateSelf(long) NTDLL.RtlImpersonateSelf
@ stdcall RtlInitAnsiString(ptr str) NTDLL.RtlInitAnsiString
@ stdcall RtlInitAnsiStringEx(ptr str) NTDLL.RtlInitAnsiStringEx
@ stdcall RtlInitCodePageTable(ptr ptr) NTDLL.RtlInitCodePageTable
@ stdcall RtlInitMemoryStream(ptr) NTDLL.RtlInitMemoryStream
@ stdcall RtlInitNlsTables(ptr ptr ptr ptr) NTDLL.RtlInitNlsTables
@ stdcall RtlInitOutOfProcessMemoryStream(ptr) NTDLL.RtlInitOutOfProcessMemoryStream
@ stdcall RtlInitString(ptr str) NTDLL.RtlInitString
@ stdcall RtlInitUnicodeString(ptr wstr) NTDLL.RtlInitUnicodeString
@ stdcall RtlInitUnicodeStringEx(ptr wstr) NTDLL.RtlInitUnicodeStringEx
@ stdcall RtlInitializeBitMap(ptr long long) NTDLL.RtlInitializeBitMap
@ stdcall RtlInitializeContext(ptr ptr ptr ptr ptr) NTDLL.RtlInitializeContext
@ stdcall RtlInitializeCriticalSection(ptr) NTDLL.RtlInitializeCriticalSection
@ stdcall RtlInitializeCriticalSectionAndSpinCount(ptr long) NTDLL.RtlInitializeCriticalSectionAndSpinCount
@ stdcall RtlInitializeGenericTable(ptr ptr ptr ptr ptr) NTDLL.RtlInitializeGenericTable
@ stdcall RtlInitializeGenericTableAvl(ptr ptr ptr ptr ptr) NTDLL.RtlInitializeGenericTableAvl
@ stdcall RtlInitializeHandleTable(long long ptr) NTDLL.RtlInitializeHandleTable
@ stdcall RtlInitializeRXact(ptr long ptr) NTDLL.RtlInitializeRXact
@ stdcall RtlInitializeResource(ptr) NTDLL.RtlInitializeResource
@ stdcall RtlInitializeSListHead(ptr) NTDLL.RtlInitializeSListHead
@ stdcall RtlInitializeSid(ptr ptr long) NTDLL.RtlInitializeSid
@ stdcall RtlInsertElementGenericTable(ptr ptr long ptr) NTDLL.RtlInsertElementGenericTable
@ stdcall RtlInsertElementGenericTableAvl(ptr ptr long ptr) NTDLL.RtlInsertElementGenericTableAvl
@ stdcall -arch=x86_64 RtlInstallFunctionTableCallback(double double long ptr ptr ptr) NTDLL.RtlInstallFunctionTableCallback
@ stdcall RtlInt64ToUnicodeString(double long ptr) NTDLL.RtlInt64ToUnicodeString
@ stdcall RtlIntegerToChar(long long long ptr) NTDLL.RtlIntegerToChar
@ stdcall RtlIntegerToUnicodeString(long long ptr) NTDLL.RtlIntegerToUnicodeString
@ stdcall -arch=win32 -ret64 RtlInterlockedCompareExchange64(ptr double double) NTDLL.RtlInterlockedCompareExchange64
@ stdcall RtlInterlockedFlushSList(ptr) NTDLL.RtlInterlockedFlushSList
@ stdcall RtlInterlockedPopEntrySList(ptr) NTDLL.RtlInterlockedPopEntrySList
@ stdcall RtlInterlockedPushEntrySList(ptr ptr) NTDLL.RtlInterlockedPushEntrySList
@ stdcall RtlIpv4AddressToStringA(ptr ptr) NTDLL.RtlIpv4AddressToStringA
@ stdcall RtlIpv4AddressToStringExA(ptr long ptr ptr) NTDLL.RtlIpv4AddressToStringExA
@ stdcall RtlIpv4AddressToStringExW(ptr long ptr ptr) NTDLL.RtlIpv4AddressToStringExW
@ stdcall RtlIpv4AddressToStringW(ptr ptr) NTDLL.RtlIpv4AddressToStringW
@ stdcall RtlIpv4StringToAddressA(str long ptr ptr) NTDLL.RtlIpv4StringToAddressA
@ stdcall RtlIpv4StringToAddressExA(str long ptr ptr) NTDLL.RtlIpv4StringToAddressExA
@ stdcall RtlIpv4StringToAddressExW(wstr long ptr ptr) NTDLL.RtlIpv4StringToAddressExW
@ stdcall RtlIpv4StringToAddressW(wstr long ptr ptr) NTDLL.RtlIpv4StringToAddressW
@ stdcall RtlIpv6AddressToStringA(ptr ptr) NTDLL.RtlIpv6AddressToStringA
@ stdcall RtlIpv6AddressToStringExA(ptr long long ptr ptr) NTDLL.RtlIpv6AddressToStringExA
@ stdcall RtlIpv6AddressToStringExW(ptr long long ptr ptr) NTDLL.RtlIpv6AddressToStringExW
@ stdcall RtlIpv6AddressToStringW(ptr ptr) NTDLL.RtlIpv6AddressToStringW
@ stdcall RtlIpv6StringToAddressA(str ptr ptr) NTDLL.RtlIpv6StringToAddressA
@ stdcall RtlIpv6StringToAddressExA(str ptr ptr ptr) NTDLL.RtlIpv6StringToAddressExA
@ stdcall RtlIpv6StringToAddressExW(wstr ptr ptr ptr) NTDLL.RtlIpv6StringToAddressExW
@ stdcall RtlIpv6StringToAddressW(wstr ptr ptr) NTDLL.RtlIpv6StringToAddressW
@ stdcall RtlIsActivationContextActive(ptr) NTDLL.RtlIsActivationContextActive
@ stdcall RtlIsCriticalSectionLocked(ptr) NTDLL.RtlIsCriticalSectionLocked
@ stdcall RtlIsCriticalSectionLockedByThread(ptr) NTDLL.RtlIsCriticalSectionLockedByThread
@ stdcall RtlIsDosDeviceName_U(wstr) NTDLL.RtlIsDosDeviceName_U
@ stdcall RtlIsGenericTableEmpty(ptr) NTDLL.RtlIsGenericTableEmpty
@ stdcall RtlIsGenericTableEmptyAvl(ptr) NTDLL.RtlIsGenericTableEmptyAvl
@ stdcall RtlIsNameLegalDOS8Dot3(ptr ptr ptr) NTDLL.RtlIsNameLegalDOS8Dot3
@ stdcall RtlIsTextUnicode(ptr long ptr) NTDLL.RtlIsTextUnicode
@ stdcall RtlIsThreadWithinLoaderCallout() NTDLL.RtlIsThreadWithinLoaderCallout
@ stdcall RtlIsValidHandle(ptr ptr) NTDLL.RtlIsValidHandle
@ stdcall RtlIsValidIndexHandle(ptr long ptr) NTDLL.RtlIsValidIndexHandle
@ stdcall -arch=win32 -ret64 RtlLargeIntegerAdd(double double) NTDLL.RtlLargeIntegerAdd
@ stdcall -arch=win32 -ret64 RtlLargeIntegerArithmeticShift(double long) NTDLL.RtlLargeIntegerArithmeticShift
@ stdcall -arch=win32 -ret64 RtlLargeIntegerDivide(double double ptr) NTDLL.RtlLargeIntegerDivide
@ stdcall -arch=win32 -ret64 RtlLargeIntegerNegate(double) NTDLL.RtlLargeIntegerNegate
@ stdcall -arch=win32 -ret64 RtlLargeIntegerShiftLeft(double long) NTDLL.RtlLargeIntegerShiftLeft
@ stdcall -arch=win32 -ret64 RtlLargeIntegerShiftRight(double long) NTDLL.RtlLargeIntegerShiftRight
@ stdcall -arch=win32 -ret64 RtlLargeIntegerSubtract(double double) NTDLL.RtlLargeIntegerSubtract
@ stdcall RtlLargeIntegerToChar(ptr long long ptr) NTDLL.RtlLargeIntegerToChar
@ stdcall RtlLeaveCriticalSection(ptr) NTDLL.RtlLeaveCriticalSection
@ stdcall RtlLengthRequiredSid(long) NTDLL.RtlLengthRequiredSid
@ stdcall RtlLengthSecurityDescriptor(ptr) NTDLL.RtlLengthSecurityDescriptor
@ stdcall RtlLengthSid(ptr) NTDLL.RtlLengthSid
@ stdcall RtlLocalTimeToSystemTime(ptr ptr) NTDLL.RtlLocalTimeToSystemTime
@ stdcall RtlLockBootStatusData(ptr) NTDLL.RtlLockBootStatusData
@ stdcall RtlLockHeap(long) NTDLL.RtlLockHeap
@ stdcall RtlLockMemoryStreamRegion(ptr int64 int64 long) NTDLL.RtlLockMemoryStreamRegion
@ stdcall RtlLookupAtomInAtomTable(ptr wstr ptr) NTDLL.RtlLookupAtomInAtomTable
@ stdcall RtlLookupElementGenericTable(ptr ptr) NTDLL.RtlLookupElementGenericTable
@ stdcall RtlLookupElementGenericTableAvl(ptr ptr) NTDLL.RtlLookupElementGenericTableAvl
@ stdcall -arch=x86_64 RtlLookupFunctionEntry(long ptr ptr) NTDLL.RtlLookupFunctionEntry
@ stdcall RtlMakeSelfRelativeSD(ptr ptr ptr) NTDLL.RtlMakeSelfRelativeSD
@ stdcall RtlMapGenericMask(long ptr) NTDLL.RtlMapGenericMask
@ stdcall RtlMapSecurityErrorToNtStatus(long) NTDLL.RtlMapSecurityErrorToNtStatus
@ stdcall RtlMoveMemory(ptr ptr long) NTDLL.RtlMoveMemory
@ stdcall RtlMultiAppendUnicodeStringBuffer(ptr long ptr) NTDLL.RtlMultiAppendUnicodeStringBuffer
@ stdcall RtlMultiByteToUnicodeN(ptr long ptr ptr long) NTDLL.RtlMultiByteToUnicodeN
@ stdcall RtlMultiByteToUnicodeSize(ptr str long) NTDLL.RtlMultiByteToUnicodeSize
@ stdcall RtlNewInstanceSecurityObject(long long ptr ptr ptr ptr ptr long ptr ptr) NTDLL.RtlNewInstanceSecurityObject
@ stdcall RtlNewSecurityGrantedAccess(long ptr ptr ptr ptr ptr) NTDLL.RtlNewSecurityGrantedAccess
@ stdcall RtlNewSecurityObject(ptr ptr ptr long ptr ptr) NTDLL.RtlNewSecurityObject
@ stdcall RtlNewSecurityObjectEx(ptr ptr ptr ptr long long ptr ptr) NTDLL.RtlNewSecurityObjectEx
@ stdcall RtlNewSecurityObjectWithMultipleInheritance(ptr ptr ptr ptr long long long ptr ptr) NTDLL.RtlNewSecurityObjectWithMultipleInheritance
@ stdcall RtlNormalizeProcessParams(ptr) NTDLL.RtlNormalizeProcessParams
@ stdcall RtlNtPathNameToDosPathName(long ptr ptr ptr) ; CHECKME (last arg) NTDLL.RtlNtPathNameToDosPathName
@ stdcall RtlNtStatusToDosError(long) NTDLL.RtlNtStatusToDosError
@ stdcall RtlNtStatusToDosErrorNoTeb(long) NTDLL.RtlNtStatusToDosErrorNoTeb
@ stdcall RtlNumberGenericTableElements(ptr) NTDLL.RtlNumberGenericTableElements
@ stdcall RtlNumberGenericTableElementsAvl(ptr) NTDLL.RtlNumberGenericTableElementsAvl
@ stdcall RtlNumberOfClearBits(ptr) NTDLL.RtlNumberOfClearBits
@ stdcall RtlNumberOfSetBits(ptr) NTDLL.RtlNumberOfSetBits
@ stdcall RtlOemStringToUnicodeSize(ptr)  NTDLL.RtlOemStringToUnicodeSize
@ stdcall RtlOemStringToUnicodeString(ptr ptr long) NTDLL.RtlOemStringToUnicodeString
@ stdcall RtlOemToUnicodeN(ptr long ptr ptr long) NTDLL.RtlOemToUnicodeN
@ stdcall RtlOpenCurrentUser(long ptr) NTDLL.RtlOpenCurrentUser
@ stdcall RtlPcToFileHeader(ptr ptr) NTDLL.RtlPcToFileHeader
@ stdcall RtlPinAtomInAtomTable(ptr long) NTDLL.RtlPinAtomInAtomTable
@ stdcall RtlPopFrame(ptr) NTDLL.RtlPopFrame
@ stdcall RtlPrefixString(ptr ptr long) NTDLL.RtlPrefixString
@ stdcall RtlPrefixUnicodeString(ptr ptr long) NTDLL.RtlPrefixUnicodeString
@ stdcall RtlProtectHeap(ptr long) NTDLL.RtlProtectHeap
@ stdcall RtlPushFrame(ptr) NTDLL.RtlPushFrame
@ stdcall RtlQueryAtomInAtomTable(ptr long ptr ptr ptr ptr) NTDLL.RtlQueryAtomInAtomTable
@ stdcall RtlQueryDepthSList(ptr) NTDLL.RtlQueryDepthSList
@ stdcall RtlQueryEnvironmentVariable_U(ptr ptr ptr) NTDLL.RtlQueryEnvironmentVariable_U
@ stdcall RtlQueryHeapInformation(long long ptr long ptr) NTDLL.RtlQueryHeapInformation
@ stdcall RtlQueryInformationAcl(ptr ptr long long) NTDLL.RtlQueryInformationAcl
@ stdcall RtlQueryInformationActivationContext(long long ptr long ptr long ptr) NTDLL.RtlQueryInformationActivationContext
@ stdcall RtlQueryInformationActiveActivationContext(long ptr long ptr) NTDLL.RtlQueryInformationActiveActivationContext
@ stdcall RtlQueryInterfaceMemoryStream(ptr ptr ptr) NTDLL.RtlQueryInterfaceMemoryStream
@ stdcall RtlQueryProcessDebugInformation(long long ptr) NTDLL.RtlQueryProcessDebugInformation
@ stdcall RtlQueryRegistryValues(long ptr ptr ptr ptr) NTDLL.RtlQueryRegistryValues
@ stdcall RtlQuerySecurityObject(ptr long ptr long ptr) NTDLL.RtlQuerySecurityObject
@ stdcall RtlQueryTagHeap(ptr long long long ptr) NTDLL.RtlQueryTagHeap
@ stdcall RtlQueryTimeZoneInformation(ptr) NTDLL.RtlQueryTimeZoneInformation
@ stdcall RtlQueueWorkItem(ptr ptr long) NTDLL.RtlQueueWorkItem
@ stdcall -register RtlRaiseException(ptr) NTDLL.RtlRaiseException
@ stdcall RtlRaiseStatus(long) NTDLL.RtlRaiseStatus
@ stdcall RtlRandom(ptr) NTDLL.RtlRandom
@ stdcall RtlRandomEx(ptr) NTDLL.RtlRandomEx
@ stdcall RtlReAllocateHeap(long long ptr long) NTDLL.RtlReAllocateHeap
@ stdcall RtlReadMemoryStream(ptr ptr long ptr) NTDLL.RtlReadMemoryStream
@ stdcall RtlReadOutOfProcessMemoryStream(ptr ptr long ptr) NTDLL.RtlReadOutOfProcessMemoryStream
@ stdcall RtlRealPredecessor(ptr) NTDLL.RtlRealPredecessor
@ stdcall RtlRealSuccessor(ptr) NTDLL.RtlRealSuccessor
@ stdcall RtlRegisterSecureMemoryCacheCallback(ptr) NTDLL.RtlRegisterSecureMemoryCacheCallback
@ stdcall RtlRegisterWait(ptr ptr ptr ptr long long) NTDLL.RtlRegisterWait
@ stdcall RtlReleaseActivationContext(ptr) NTDLL.RtlReleaseActivationContext
@ stdcall RtlReleaseMemoryStream(ptr) NTDLL.RtlReleaseMemoryStream
@ stdcall RtlReleasePebLock() NTDLL.RtlReleasePebLock
@ stdcall RtlReleasePrivilege(ptr) NTDLL.RtlReleasePrivilege
@ stdcall RtlReleaseRelativeName(ptr) NTDLL.RtlReleaseRelativeName
@ stdcall RtlReleaseResource(ptr) NTDLL.RtlReleaseResource
@ stdcall RtlRemoteCall(ptr ptr ptr long ptr long long) NTDLL.RtlRemoteCall
@ stdcall RtlRemoveVectoredContinueHandler(ptr) NTDLL.RtlRemoveVectoredContinueHandler
@ stdcall RtlRemoveVectoredExceptionHandler(ptr) NTDLL.RtlRemoveVectoredExceptionHandler
@ stdcall RtlResetRtlTranslations(ptr) NTDLL.RtlResetRtlTranslations
@ stdcall -arch=x86_64 RtlRestoreContext(ptr ptr) NTDLL.RtlRestoreContext
@ stdcall RtlRestoreLastWin32Error(long)  NTDLL.RtlRestoreLastWin32Error
@ stdcall RtlRevertMemoryStream(ptr) NTDLL.RtlRevertMemoryStream
@ stdcall RtlRunDecodeUnicodeString(long ptr) NTDLL.RtlRunDecodeUnicodeString
@ stdcall RtlRunEncodeUnicodeString(long ptr) NTDLL.RtlRunEncodeUnicodeString
@ stdcall RtlSecondsSince1970ToTime(long ptr) NTDLL.RtlSecondsSince1970ToTime
@ stdcall RtlSecondsSince1980ToTime(long ptr) NTDLL.RtlSecondsSince1980ToTime
@ stdcall RtlSeekMemoryStream(ptr int64 long ptr) NTDLL.RtlSeekMemoryStream
@ stdcall RtlSelfRelativeToAbsoluteSD2(ptr ptr) NTDLL.RtlSelfRelativeToAbsoluteSD2
@ stdcall RtlSelfRelativeToAbsoluteSD(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.RtlSelfRelativeToAbsoluteSD
@ stdcall RtlSetAllBits(ptr) NTDLL.RtlSetAllBits
@ stdcall RtlSetAttributesSecurityDescriptor(ptr long ptr) NTDLL.RtlSetAttributesSecurityDescriptor
@ stdcall RtlSetBits(ptr long long) NTDLL.RtlSetBits
@ stdcall RtlSetControlSecurityDescriptor(ptr long long) NTDLL.RtlSetControlSecurityDescriptor
@ stdcall RtlSetCriticalSectionSpinCount(ptr long) NTDLL.RtlSetCriticalSectionSpinCount
@ stdcall RtlSetCurrentDirectory_U(ptr) NTDLL.RtlSetCurrentDirectory_U
@ stdcall RtlSetCurrentEnvironment(wstr ptr) NTDLL.RtlSetCurrentEnvironment
@ stdcall RtlSetDaclSecurityDescriptor(ptr long ptr long) NTDLL.RtlSetDaclSecurityDescriptor
@ stdcall RtlSetEnvironmentStrings(wstr long) NTDLL.RtlSetEnvironmentStrings
@ stdcall RtlSetEnvironmentVariable(ptr ptr ptr) NTDLL.RtlSetEnvironmentVariable
@ stdcall RtlSetGroupSecurityDescriptor(ptr ptr long) NTDLL.RtlSetGroupSecurityDescriptor
@ stdcall RtlSetHeapInformation(ptr long ptr ptr) NTDLL.RtlSetHeapInformation
@ stdcall RtlSetInformationAcl(ptr ptr long long) NTDLL.RtlSetInformationAcl
@ stdcall RtlSetIoCompletionCallback(long ptr long) NTDLL.RtlSetIoCompletionCallback
@ stdcall RtlSetLastWin32Error(long) NTDLL.RtlSetLastWin32Error
@ stdcall RtlSetLastWin32ErrorAndNtStatusFromNtStatus(long) NTDLL.RtlSetLastWin32ErrorAndNtStatusFromNtStatus
@ stdcall RtlSetMemoryStreamSize(ptr int64) NTDLL.RtlSetMemoryStreamSize
@ stdcall RtlSetOwnerSecurityDescriptor(ptr ptr long) NTDLL.RtlSetOwnerSecurityDescriptor
@ cdecl RtlSetProcessIsCritical(long ptr long) NTDLL.RtlSetProcessIsCritical
@ stdcall RtlSetSaclSecurityDescriptor(ptr long ptr long) NTDLL.RtlSetSaclSecurityDescriptor
@ stdcall RtlSetSecurityDescriptorRMControl(ptr ptr) NTDLL.RtlSetSecurityDescriptorRMControl
@ stdcall RtlSetSecurityObject(long ptr ptr ptr ptr) NTDLL.RtlSetSecurityObject
@ stdcall RtlSetSecurityObjectEx(long ptr ptr long ptr ptr) NTDLL.RtlSetSecurityObjectEx
@ stdcall RtlSetThreadErrorMode(long ptr) NTDLL.RtlSetThreadErrorMode
@ cdecl RtlSetThreadIsCritical(long ptr long) NTDLL.RtlSetThreadIsCritical
@ stdcall RtlSetThreadPoolStartFunc(ptr ptr) NTDLL.RtlSetThreadPoolStartFunc
@ stdcall RtlSetTimeZoneInformation(ptr) NTDLL.RtlSetTimeZoneInformation
@ stdcall RtlSetUnhandledExceptionFilter(ptr) NTDLL.RtlSetUnhandledExceptionFilter
@ stdcall RtlSetUserFlagsHeap(ptr long ptr long long) NTDLL.RtlSetUserFlagsHeap
@ stdcall RtlSetUserValueHeap(ptr long ptr ptr) NTDLL.RtlSetUserValueHeap
@ stdcall RtlSizeHeap(long long ptr) NTDLL.RtlSizeHeap
@ stdcall RtlSplay(ptr) NTDLL.RtlSplay
@ stdcall RtlStartRXact(ptr) NTDLL.RtlStartRXact
@ stdcall RtlStatMemoryStream(ptr ptr long) NTDLL.RtlStatMemoryStream
@ stdcall RtlStringFromGUID(ptr ptr) NTDLL.RtlStringFromGUID
@ stdcall RtlSubAuthorityCountSid(ptr) NTDLL.RtlSubAuthorityCountSid
@ stdcall RtlSubAuthoritySid(ptr long) NTDLL.RtlSubAuthoritySid
@ stdcall RtlSubtreePredecessor(ptr) NTDLL.RtlSubtreePredecessor
@ stdcall RtlSubtreeSuccessor(ptr) NTDLL.RtlSubtreeSuccessor
@ stdcall RtlSystemTimeToLocalTime(ptr ptr) NTDLL.RtlSystemTimeToLocalTime
@ stdcall RtlTimeFieldsToTime(ptr ptr) NTDLL.RtlTimeFieldsToTime
@ stdcall RtlTimeToElapsedTimeFields(long long) NTDLL.RtlTimeToElapsedTimeFields
@ stdcall RtlTimeToSecondsSince1970(ptr ptr) NTDLL.RtlTimeToSecondsSince1970
@ stdcall RtlTimeToSecondsSince1980(ptr ptr) NTDLL.RtlTimeToSecondsSince1980
@ stdcall RtlTimeToTimeFields (long long) NTDLL.RtlTimeToTimeFields
@ stdcall RtlTryEnterCriticalSection(ptr) NTDLL.RtlTryEnterCriticalSection
@ stdcall RtlUnhandledExceptionFilter(ptr) NTDLL.RtlUnhandledExceptionFilter
@ stdcall RtlUnicodeStringToAnsiSize(ptr)  NTDLL.RtlUnicodeStringToAnsiSize
@ stdcall RtlUnicodeStringToAnsiString(ptr ptr long) NTDLL.RtlUnicodeStringToAnsiString
@ stdcall RtlUnicodeStringToCountedOemString(ptr ptr long) NTDLL.RtlUnicodeStringToCountedOemString
@ stdcall RtlUnicodeStringToInteger(ptr long ptr) NTDLL.RtlUnicodeStringToInteger
@ stdcall RtlUnicodeStringToOemSize(ptr)  NTDLL.RtlUnicodeStringToOemSize
@ stdcall RtlUnicodeStringToOemString(ptr ptr long) NTDLL.RtlUnicodeStringToOemString
@ stdcall RtlUnicodeToCustomCPN(ptr ptr long ptr wstr long) NTDLL.RtlUnicodeToCustomCPN
@ stdcall RtlUnicodeToMultiByteN(ptr long ptr ptr long) NTDLL.RtlUnicodeToMultiByteN
@ stdcall RtlUnicodeToMultiByteSize(ptr ptr long) NTDLL.RtlUnicodeToMultiByteSize
@ stdcall RtlUnicodeToOemN(ptr long ptr ptr long) NTDLL.RtlUnicodeToOemN
@ stdcall RtlUniform(ptr) NTDLL.RtlUniform
@ stdcall RtlUnlockBootStatusData(ptr) NTDLL.RtlUnlockBootStatusData
@ stdcall RtlUnlockHeap(long) NTDLL.RtlUnlockHeap
@ stdcall RtlUnlockMemoryStreamRegion(ptr int64 int64 long) NTDLL.RtlUnlockMemoryStreamRegion
@ stdcall -register RtlUnwind(ptr ptr ptr ptr) NTDLL.RtlUnwind
@ stdcall -arch=x86_64 RtlUnwindEx(long long ptr long ptr) NTDLL.RtlUnwindEx
@ stdcall RtlUpcaseUnicodeChar(long) NTDLL.RtlUpcaseUnicodeChar
@ stdcall RtlUpcaseUnicodeString(ptr ptr long) NTDLL.RtlUpcaseUnicodeString
@ stdcall RtlUpcaseUnicodeStringToAnsiString(ptr ptr long) NTDLL.RtlUpcaseUnicodeStringToAnsiString
@ stdcall RtlUpcaseUnicodeStringToCountedOemString(ptr ptr long) NTDLL.RtlUpcaseUnicodeStringToCountedOemString
@ stdcall RtlUpcaseUnicodeStringToOemString(ptr ptr long) NTDLL.RtlUpcaseUnicodeStringToOemString
@ stdcall RtlUpcaseUnicodeToCustomCPN(ptr ptr long ptr wstr long) NTDLL.RtlUpcaseUnicodeToCustomCPN
@ stdcall RtlUpcaseUnicodeToMultiByteN(ptr long ptr ptr long) NTDLL.RtlUpcaseUnicodeToMultiByteN
@ stdcall RtlUpcaseUnicodeToOemN(ptr long ptr ptr long) NTDLL.RtlUpcaseUnicodeToOemN
@ stdcall RtlUpdateTimer(ptr ptr long long) NTDLL.RtlUpdateTimer
@ stdcall RtlUpperChar(long) NTDLL.RtlUpperChar
@ stdcall RtlUpperString(ptr ptr) NTDLL.RtlUpperString
@ stdcall RtlUsageHeap(ptr long ptr) NTDLL.RtlUsageHeap
@ stdcall RtlValidAcl(ptr) NTDLL.RtlValidAcl
@ stdcall RtlValidRelativeSecurityDescriptor(ptr long long) NTDLL.RtlValidRelativeSecurityDescriptor
@ stdcall RtlValidSecurityDescriptor(ptr) NTDLL.RtlValidSecurityDescriptor
@ stdcall RtlValidSid(ptr) NTDLL.RtlValidSid
@ stdcall RtlValidateHeap(long long ptr) NTDLL.RtlValidateHeap
@ stdcall RtlValidateProcessHeaps() NTDLL.RtlValidateProcessHeaps
@ stdcall RtlValidateUnicodeString(long ptr) NTDLL.RtlValidateUnicodeString
@ stdcall RtlVerifyVersionInfo(ptr long double) NTDLL.RtlVerifyVersionInfo
@ stdcall -arch=x86_64 RtlVirtualUnwind(long long long ptr ptr ptr ptr ptr) NTDLL.RtlVirtualUnwind
@ stdcall RtlWalkFrameChain(ptr long long) NTDLL.RtlWalkFrameChain
@ stdcall RtlWalkHeap(long ptr) NTDLL.RtlWalkHeap
@ stdcall RtlWow64EnableFsRedirection(long) NTDLL.RtlWow64EnableFsRedirection
@ stdcall RtlWow64EnableFsRedirectionEx(long ptr) NTDLL.RtlWow64EnableFsRedirectionEx
@ stdcall RtlWriteMemoryStream(ptr ptr long ptr) NTDLL.RtlWriteMemoryStream
@ stdcall RtlWriteRegistryValue(long ptr ptr long ptr long) NTDLL.RtlWriteRegistryValue
@ stdcall RtlZeroHeap(ptr long) NTDLL.RtlZeroHeap
@ stdcall RtlZeroMemory(ptr long) NTDLL.RtlZeroMemory
@ stdcall RtlZombifyActivationContext(ptr) NTDLL.RtlZombifyActivationContext
@ stdcall RtlpApplyLengthFunction(long long ptr ptr) NTDLL.RtlpApplyLengthFunction
@ stdcall RtlpEnsureBufferSize(long ptr long) NTDLL.RtlpEnsureBufferSize
@ stdcall RtlpNtCreateKey(ptr long ptr long ptr ptr) NTDLL.RtlpNtCreateKey
@ stdcall RtlpNtEnumerateSubKey(ptr ptr long long) NTDLL.RtlpNtEnumerateSubKey
@ stdcall RtlpNtMakeTemporaryKey(ptr) NTDLL.RtlpNtMakeTemporaryKey
@ stdcall RtlpNtOpenKey(ptr long ptr long) NTDLL.RtlpNtOpenKey
@ stdcall RtlpNtQueryValueKey(ptr ptr ptr ptr long) NTDLL.RtlpNtQueryValueKey
@ stdcall RtlpNtSetValueKey(ptr long ptr long) NTDLL.RtlpNtSetValueKey
@ stdcall RtlpUnWaitCriticalSection(ptr) NTDLL.RtlpUnWaitCriticalSection
@ stdcall RtlpWaitForCriticalSection(ptr) NTDLL.RtlpWaitForCriticalSection
@ stdcall RtlxAnsiStringToUnicodeSize(ptr) NTDLL.RtlxAnsiStringToUnicodeSize
@ stdcall RtlxOemStringToUnicodeSize(ptr) NTDLL.RtlxOemStringToUnicodeSize
@ stdcall RtlxUnicodeStringToAnsiSize(ptr) NTDLL.RtlxUnicodeStringToAnsiSize
@ stdcall RtlxUnicodeStringToOemSize(ptr) NTDLL.RtlxUnicodeStringToOemSize
@ stdcall -ret64 VerSetConditionMask(double long long) NTDLL.VerSetConditionMask
@ stdcall ZwAcceptConnectPort(ptr long ptr long long ptr)  NTDLL.ZwAcceptConnectPort
@ stdcall ZwAccessCheck(ptr long long ptr ptr ptr ptr ptr)  NTDLL.ZwAccessCheck
@ stdcall ZwAccessCheckAndAuditAlarm(ptr long ptr ptr ptr long ptr long ptr ptr ptr)  NTDLL.ZwAccessCheckAndAuditAlarm
@ stdcall ZwAccessCheckByType(ptr ptr ptr long ptr long ptr ptr long ptr ptr)  NTDLL.ZwAccessCheckByType
@ stdcall ZwAccessCheckByTypeAndAuditAlarm(ptr ptr ptr ptr ptr ptr long long long ptr long ptr long ptr ptr ptr)  NTDLL.ZwAccessCheckByTypeAndAuditAlarm
@ stdcall ZwAccessCheckByTypeResultList(ptr ptr ptr long ptr long ptr ptr long ptr ptr)  NTDLL.ZwAccessCheckByTypeResultList
@ stdcall ZwAccessCheckByTypeResultListAndAuditAlarm(ptr ptr ptr ptr ptr ptr long long long ptr long ptr long ptr ptr ptr)  NTDLL.ZwAccessCheckByTypeResultListAndAuditAlarm
@ stdcall ZwAccessCheckByTypeResultListAndAuditAlarmByHandle(ptr ptr ptr ptr ptr ptr ptr long long long ptr long ptr long ptr ptr ptr)  NTDLL.ZwAccessCheckByTypeResultListAndAuditAlarmByHandle
@ stdcall ZwAddAtom(ptr long ptr)  NTDLL.ZwAddAtom
@ stdcall ZwAddBootEntry(ptr long) NTDLL.ZwAddBootEntry
@ stdcall ZwAddDriverEntry(ptr long) NTDLL.ZwAddDriverEntry
@ stdcall ZwAdjustGroupsToken(long long long long long long)  NTDLL.ZwAdjustGroupsToken
@ stdcall ZwAdjustPrivilegesToken(long long long long long long)  NTDLL.ZwAdjustPrivilegesToken
@ stdcall ZwAlertResumeThread(long ptr)  NTDLL.ZwAlertResumeThread
@ stdcall ZwAlertThread(long)  NTDLL.ZwAlertThread
@ stdcall ZwAllocateLocallyUniqueId(ptr)  NTDLL.ZwAllocateLocallyUniqueId
@ stdcall ZwAllocateUserPhysicalPages(ptr ptr ptr) NTDLL.ZwAllocateUserPhysicalPages
@ stdcall ZwAllocateUuids(ptr ptr ptr ptr)  NTDLL.ZwAllocateUuids
@ stdcall ZwAllocateVirtualMemory(long ptr ptr ptr long long)  NTDLL.ZwAllocateVirtualMemory
@ stdcall ZwApphelpCacheControl(long ptr) NTDLL.ZwApphelpCacheControl
@ stdcall ZwAreMappedFilesTheSame(ptr ptr)  NTDLL.ZwAreMappedFilesTheSame
@ stdcall ZwAssignProcessToJobObject(long long)  NTDLL.ZwAssignProcessToJobObject
@ stdcall ZwCallbackReturn(ptr long long) NTDLL.ZwCallbackReturn
@ stdcall ZwCancelDeviceWakeupRequest(ptr) NTDLL.ZwCancelDeviceWakeupRequest
@ stdcall ZwCancelIoFile(long ptr)  NTDLL.ZwCancelIoFile
@ stdcall ZwCancelTimer(long ptr)  NTDLL.ZwCancelTimer
@ stdcall ZwClearEvent(long)  NTDLL.ZwClearEvent
@ stdcall ZwClose(long)  NTDLL.ZwClose
@ stdcall ZwCloseObjectAuditAlarm(ptr ptr long) NTDLL.ZwCloseObjectAuditAlarm
@ stdcall ZwCompactKeys(long ptr)  NTDLL.ZwCompactKeys
@ stdcall ZwCompareTokens(ptr ptr ptr)  NTDLL.ZwCompareTokens
@ stdcall ZwCompleteConnectPort(ptr)  NTDLL.ZwCompleteConnectPort
@ stdcall ZwCompressKey(ptr)  NTDLL.ZwCompressKey
@ stdcall ZwConnectPort(ptr ptr ptr ptr ptr ptr ptr ptr)  NTDLL.ZwConnectPort
@ stdcall ZwContinue(ptr long)  NTDLL.ZwContinue
@ stdcall ZwCreateDebugObject(ptr long ptr long)  NTDLL.ZwCreateDebugObject
@ stdcall ZwCreateDirectoryObject(long long long)  NTDLL.ZwCreateDirectoryObject
@ stdcall ZwCreateEvent(long long long long long)  NTDLL.ZwCreateEvent
@ stdcall ZwCreateEventPair(ptr long ptr)  NTDLL.ZwCreateEventPair
@ stdcall ZwCreateFile(ptr long ptr ptr long long long ptr long long ptr)  NTDLL.ZwCreateFile
@ stdcall ZwCreateIoCompletion(ptr long ptr long)  NTDLL.ZwCreateIoCompletion
@ stdcall ZwCreateJobObject(ptr long ptr)  NTDLL.ZwCreateJobObject
@ stdcall ZwCreateJobSet(long ptr long)  NTDLL.ZwCreateJobSet
@ stdcall ZwCreateKey(ptr long ptr long ptr long long)  NTDLL.ZwCreateKey
@ stdcall ZwCreateKeyedEvent(ptr long ptr long)  NTDLL.ZwCreateKeyedEvent
@ stdcall ZwCreateMailslotFile(long long long long long long long long)  NTDLL.ZwCreateMailslotFile
@ stdcall ZwCreateMutant(ptr long ptr long)  NTDLL.ZwCreateMutant
@ stdcall ZwCreateNamedPipeFile(ptr long ptr ptr long long long long long long long long long ptr)  NTDLL.ZwCreateNamedPipeFile
@ stdcall ZwCreatePagingFile(long long long long)  NTDLL.ZwCreatePagingFile
@ stdcall ZwCreatePort(ptr ptr long long long)  NTDLL.ZwCreatePort
@ stdcall ZwCreateProcess(ptr long ptr ptr long ptr ptr ptr) NTDLL.ZwCreateProcess
@ stdcall ZwCreateProcessEx(ptr long ptr ptr long ptr ptr ptr long)  NTDLL.ZwCreateProcessEx
@ stdcall ZwCreateProfile(ptr ptr ptr long long ptr long long long)  NTDLL.ZwCreateProfile
@ stdcall ZwCreateSection(ptr long ptr ptr long long long)  NTDLL.ZwCreateSection
@ stdcall ZwCreateSemaphore(ptr long ptr long long)  NTDLL.ZwCreateSemaphore
@ stdcall ZwCreateSymbolicLinkObject(ptr long ptr ptr)  NTDLL.ZwCreateSymbolicLinkObject
@ stdcall ZwCreateThread(ptr long ptr ptr ptr ptr ptr long) NTDLL.ZwCreateThread
@ stdcall ZwCreateTimer(ptr long ptr long)  NTDLL.ZwCreateTimer
@ stdcall ZwCreateToken(ptr long ptr long ptr ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.ZwCreateToken
@ stdcall ZwCreateWaitablePort(ptr ptr long long long)  NTDLL.ZwCreateWaitablePort
@ stdcall ZwDebugActiveProcess(ptr ptr)  NTDLL.ZwDebugActiveProcess
@ stdcall ZwDebugContinue(ptr ptr long)  NTDLL.ZwDebugContinue
@ stdcall ZwDelayExecution(long ptr)  NTDLL.ZwDelayExecution
@ stdcall ZwDeleteAtom(long)  NTDLL.ZwDeleteAtom
@ stdcall ZwDeleteBootEntry(long)  NTDLL.ZwDeleteBootEntry
@ stdcall ZwDeleteDriverEntry(long) NTDLL.ZwDeleteDriverEntry
@ stdcall ZwDeleteFile(ptr)  NTDLL.ZwDeleteFile
@ stdcall ZwDeleteKey(long)  NTDLL.ZwDeleteKey
@ stdcall ZwDeleteObjectAuditAlarm(ptr ptr long) NTDLL.ZwDeleteObjectAuditAlarm
@ stdcall ZwDeleteValueKey(long ptr)  NTDLL.ZwDeleteValueKey
@ stdcall ZwDeviceIoControlFile(long long long long long long long long long long)  NTDLL.ZwDeviceIoControlFile
@ stdcall ZwDisplayString(ptr)  NTDLL.ZwDisplayString
@ stdcall ZwDuplicateObject(long long long ptr long long long)  NTDLL.ZwDuplicateObject
@ stdcall ZwDuplicateToken(long long long long long long)  NTDLL.ZwDuplicateToken
@ stdcall ZwEnumerateBootEntries(ptr ptr) NTDLL.ZwEnumerateBootEntries
@ stdcall ZwEnumerateDriverEntries(ptr ptr) NTDLL.ZwEnumerateDriverEntries
@ stdcall ZwEnumerateKey(long long long ptr long ptr)  NTDLL.ZwEnumerateKey
@ stdcall ZwEnumerateSystemEnvironmentValuesEx(long ptr long)  NTDLL.ZwEnumerateSystemEnvironmentValuesEx
@ stdcall ZwEnumerateValueKey(long long long ptr long ptr)  NTDLL.ZwEnumerateValueKey
@ stdcall ZwExtendSection(ptr ptr)  NTDLL.ZwExtendSection
@ stdcall ZwFilterToken(ptr long ptr ptr ptr ptr)  NTDLL.ZwFilterToken
@ stdcall ZwFindAtom(ptr long ptr)  NTDLL.ZwFindAtom
@ stdcall ZwFlushBuffersFile(long ptr)  NTDLL.ZwFlushBuffersFile
@ stdcall ZwFlushInstructionCache(long ptr long)  NTDLL.ZwFlushInstructionCache
@ stdcall ZwFlushKey(long)  NTDLL.ZwFlushKey
@ stdcall ZwFlushVirtualMemory(long ptr ptr long)  NTDLL.ZwFlushVirtualMemory
@ stdcall ZwFlushWriteBuffer() NTDLL.ZwFlushWriteBuffer
@ stdcall ZwFreeUserPhysicalPages(ptr ptr ptr) NTDLL.ZwFreeUserPhysicalPages
@ stdcall ZwFreeVirtualMemory(long ptr ptr long)  NTDLL.ZwFreeVirtualMemory
@ stdcall ZwFsControlFile(long long long long long long long long long long)  NTDLL.ZwFsControlFile
@ stdcall ZwGetContextThread(long ptr)  NTDLL.ZwGetContextThread
@ stdcall ZwGetCurrentProcessorNumber() NTDLL.ZwGetCurrentProcessorNumber
@ stdcall ZwGetDevicePowerState(ptr ptr) NTDLL.ZwGetDevicePowerState
@ stdcall ZwGetPlugPlayEvent(long long ptr long) NTDLL.ZwGetPlugPlayEvent
@ stdcall ZwGetWriteWatch(long long ptr long ptr ptr ptr)  NTDLL.ZwGetWriteWatch
@ stdcall ZwImpersonateAnonymousToken(ptr) NTDLL.ZwImpersonateAnonymousToken
@ stdcall ZwImpersonateClientOfPort(ptr ptr)  NTDLL.ZwImpersonateClientOfPort
@ stdcall ZwImpersonateThread(ptr ptr ptr)  NTDLL.ZwImpersonateThread
@ stdcall ZwInitializeRegistry(long) NTDLL.ZwInitializeRegistry
@ stdcall ZwInitiatePowerAction(long long long long)  NTDLL.ZwInitiatePowerAction
@ stdcall ZwIsProcessInJob(long long)  NTDLL.ZwIsProcessInJob
@ stdcall ZwIsSystemResumeAutomatic() NTDLL.ZwIsSystemResumeAutomatic
@ stdcall ZwListenPort(ptr ptr)  NTDLL.ZwListenPort
@ stdcall ZwLoadDriver(ptr)  NTDLL.ZwLoadDriver
@ stdcall ZwLoadKey2(ptr ptr long)  NTDLL.ZwLoadKey2
@ stdcall ZwLoadKey(ptr ptr)  NTDLL.ZwLoadKey
@ stdcall ZwLoadKeyEx(ptr ptr long ptr) NTDLL.ZwLoadKeyEx
@ stdcall ZwLockFile(long long ptr ptr ptr ptr ptr ptr long long)  NTDLL.ZwLockFile
@ stdcall ZwLockProductActivationKeys(ptr ptr)  NTDLL.ZwLockProductActivationKeys
@ stdcall ZwLockRegistryKey(ptr)  NTDLL.ZwLockRegistryKey
@ stdcall ZwLockVirtualMemory(long ptr ptr long)  NTDLL.ZwLockVirtualMemory
@ stdcall ZwMakePermanentObject(ptr)  NTDLL.ZwMakePermanentObject
@ stdcall ZwMakeTemporaryObject(long)  NTDLL.ZwMakeTemporaryObject
@ stdcall ZwMapUserPhysicalPages(ptr ptr ptr) NTDLL.ZwMapUserPhysicalPages
@ stdcall ZwMapUserPhysicalPagesScatter(ptr ptr ptr) NTDLL.ZwMapUserPhysicalPagesScatter
@ stdcall ZwMapViewOfSection(long long ptr long long ptr ptr long long long)  NTDLL.ZwMapViewOfSection
@ stdcall ZwModifyBootEntry(ptr)  NTDLL.ZwModifyBootEntry
@ stdcall ZwModifyDriverEntry(ptr) NTDLL.ZwModifyDriverEntry
@ stdcall ZwNotifyChangeDirectoryFile(long long ptr ptr ptr ptr long long long)  NTDLL.ZwNotifyChangeDirectoryFile
@ stdcall ZwNotifyChangeKey(long long ptr ptr ptr long long ptr long long)  NTDLL.ZwNotifyChangeKey
@ stdcall ZwNotifyChangeMultipleKeys(ptr long ptr ptr ptr ptr ptr long long ptr long long)  NTDLL.ZwNotifyChangeMultipleKeys
@ stdcall ZwOpenDirectoryObject(long long long)  NTDLL.ZwOpenDirectoryObject
@ stdcall ZwOpenEvent(long long long)  NTDLL.ZwOpenEvent
@ stdcall ZwOpenEventPair(ptr long ptr)  NTDLL.ZwOpenEventPair
@ stdcall ZwOpenFile(ptr long ptr ptr long long)  NTDLL.ZwOpenFile
@ stdcall ZwOpenIoCompletion(ptr long ptr)  NTDLL.ZwOpenIoCompletion
@ stdcall ZwOpenJobObject(ptr long ptr)  NTDLL.ZwOpenJobObject
@ stdcall ZwOpenKey(ptr long ptr)  NTDLL.ZwOpenKey
@ stdcall ZwOpenKeyedEvent(ptr long ptr)  NTDLL.ZwOpenKeyedEvent
@ stdcall ZwOpenMutant(ptr long ptr)  NTDLL.ZwOpenMutant
@ stdcall ZwOpenObjectAuditAlarm(ptr ptr ptr ptr ptr ptr long long ptr long long ptr) NTDLL.ZwOpenObjectAuditAlarm
@ stdcall ZwOpenProcess(ptr long ptr ptr)  NTDLL.ZwOpenProcess
@ stdcall ZwOpenProcessToken(long long ptr)  NTDLL.ZwOpenProcessToken
@ stdcall ZwOpenProcessTokenEx(long long long ptr)  NTDLL.ZwOpenProcessTokenEx
@ stdcall ZwOpenSection(ptr long ptr)  NTDLL.ZwOpenSection
@ stdcall ZwOpenSemaphore(long long ptr)  NTDLL.ZwOpenSemaphore
@ stdcall ZwOpenSymbolicLinkObject (ptr long ptr)  NTDLL.ZwOpenSymbolicLinkObject
@ stdcall ZwOpenThread(ptr long ptr ptr)  NTDLL.ZwOpenThread
@ stdcall ZwOpenThreadToken(long long long ptr)  NTDLL.ZwOpenThreadToken
@ stdcall ZwOpenThreadTokenEx(long long long long ptr)  NTDLL.ZwOpenThreadTokenEx
@ stdcall ZwOpenTimer(ptr long ptr)  NTDLL.ZwOpenTimer
@ stdcall ZwPlugPlayControl(ptr ptr long) NTDLL.ZwPlugPlayControl
@ stdcall ZwPowerInformation(long ptr long ptr long)  NTDLL.ZwPowerInformation
@ stdcall ZwPrivilegeCheck(ptr ptr ptr)  NTDLL.ZwPrivilegeCheck
@ stdcall ZwPrivilegeObjectAuditAlarm(ptr ptr ptr long ptr long) NTDLL.ZwPrivilegeObjectAuditAlarm
@ stdcall ZwPrivilegedServiceAuditAlarm(ptr ptr ptr ptr long) NTDLL.ZwPrivilegedServiceAuditAlarm
@ stdcall ZwProtectVirtualMemory(long ptr ptr long ptr)  NTDLL.ZwProtectVirtualMemory
@ stdcall ZwPulseEvent(long ptr)  NTDLL.ZwPulseEvent
@ stdcall ZwQueryAttributesFile(ptr ptr)  NTDLL.ZwQueryAttributesFile
@ stdcall ZwQueryBootEntryOrder(ptr ptr)  NTDLL.ZwQueryBootEntryOrder
@ stdcall ZwQueryBootOptions(ptr ptr)  NTDLL.ZwQueryBootOptions
@ stdcall ZwQueryDebugFilterState(long long)  NTDLL.ZwQueryDebugFilterState
@ stdcall ZwQueryDefaultLocale(long ptr)  NTDLL.ZwQueryDefaultLocale
@ stdcall ZwQueryDefaultUILanguage(ptr)  NTDLL.ZwQueryDefaultUILanguage
@ stdcall ZwQueryDirectoryFile(long long ptr ptr ptr ptr long long long ptr long)  NTDLL.ZwQueryDirectoryFile
@ stdcall ZwQueryDirectoryObject(long ptr long long long ptr ptr)  NTDLL.ZwQueryDirectoryObject
@ stdcall ZwQueryDriverEntryOrder(ptr ptr) NTDLL.ZwQueryDriverEntryOrder
@ stdcall ZwQueryEaFile(long ptr ptr long long ptr long ptr long)  NTDLL.ZwQueryEaFile
@ stdcall ZwQueryEvent(long long ptr long ptr)  NTDLL.ZwQueryEvent
@ stdcall ZwQueryFullAttributesFile(ptr ptr)  NTDLL.ZwQueryFullAttributesFile
@ stdcall ZwQueryInformationAtom(long long ptr long ptr)  NTDLL.ZwQueryInformationAtom
@ stdcall ZwQueryInformationFile(long ptr ptr long long)  NTDLL.ZwQueryInformationFile
@ stdcall ZwQueryInformationJobObject(long long ptr long ptr)  NTDLL.ZwQueryInformationJobObject
@ stdcall ZwQueryInformationPort(ptr long ptr long ptr)  NTDLL.ZwQueryInformationPort
@ stdcall ZwQueryInformationProcess(long long ptr long ptr)  NTDLL.ZwQueryInformationProcess
@ stdcall ZwQueryInformationThread(long long ptr long ptr)  NTDLL.ZwQueryInformationThread
@ stdcall ZwQueryInformationToken(long long ptr long ptr)  NTDLL.ZwQueryInformationToken
@ stdcall ZwQueryInstallUILanguage(ptr)  NTDLL.ZwQueryInstallUILanguage
@ stdcall ZwQueryIntervalProfile(long ptr)  NTDLL.ZwQueryIntervalProfile
@ stdcall ZwQueryIoCompletion(long long ptr long ptr)  NTDLL.ZwQueryIoCompletion
@ stdcall ZwQueryKey(long long ptr long ptr)  NTDLL.ZwQueryKey
@ stdcall ZwQueryMultipleValueKey(long ptr long ptr long ptr)  NTDLL.ZwQueryMultipleValueKey
@ stdcall ZwQueryMutant(long long ptr long ptr)  NTDLL.ZwQueryMutant
@ stdcall ZwQueryObject(long long long long long)  NTDLL.ZwQueryObject
@ stdcall ZwQueryOpenSubKeys(ptr ptr)  NTDLL.ZwQueryOpenSubKeys
@ stdcall ZwQueryOpenSubKeysEx(ptr long ptr ptr) NTDLL.ZwQueryOpenSubKeysEx
@ stdcall ZwQueryPerformanceCounter (long long)  NTDLL.ZwQueryPerformanceCounter
@ stdcall ZwQueryPortInformationProcess()  NTDLL.ZwQueryPortInformationProcess
@ stdcall ZwQueryQuotaInformationFile(ptr ptr ptr long long ptr long ptr long)  NTDLL.ZwQueryQuotaInformationFile
@ stdcall ZwQuerySection (long long long long long)  NTDLL.ZwQuerySection
@ stdcall ZwQuerySecurityObject (long long long long long)  NTDLL.ZwQuerySecurityObject
@ stdcall ZwQuerySemaphore (long long long long long)  NTDLL.ZwQuerySemaphore
@ stdcall ZwQuerySymbolicLinkObject(long ptr ptr)  NTDLL.ZwQuerySymbolicLinkObject
@ stdcall ZwQuerySystemEnvironmentValue(ptr ptr long ptr)  NTDLL.ZwQuerySystemEnvironmentValue
@ stdcall ZwQuerySystemEnvironmentValueEx(ptr ptr ptr ptr ptr)  NTDLL.ZwQuerySystemEnvironmentValueEx
@ stdcall ZwQuerySystemInformation(long long long long)  NTDLL.ZwQuerySystemInformation
@ stdcall ZwQuerySystemTime(ptr)  NTDLL.ZwQuerySystemTime
@ stdcall ZwQueryTimer(ptr long ptr long ptr)  NTDLL.ZwQueryTimer
@ stdcall ZwQueryTimerResolution(long long long)  NTDLL.ZwQueryTimerResolution
@ stdcall ZwQueryValueKey(long ptr long ptr long ptr)  NTDLL.ZwQueryValueKey
@ stdcall ZwQueryVirtualMemory(long ptr long ptr long ptr)  NTDLL.ZwQueryVirtualMemory
@ stdcall ZwQueryVolumeInformationFile(long ptr ptr long long)  NTDLL.ZwQueryVolumeInformationFile
@ stdcall ZwQueueApcThread(long ptr long long long)  NTDLL.ZwQueueApcThread
@ stdcall ZwRaiseException(ptr ptr long)  NTDLL.ZwRaiseException
@ stdcall ZwRaiseHardError(long long long ptr long ptr)  NTDLL.ZwRaiseHardError
@ stdcall ZwReadFile(long long ptr ptr ptr ptr long ptr ptr)  NTDLL.ZwReadFile
@ stdcall ZwReadFileScatter(long long ptr ptr ptr ptr long ptr ptr)  NTDLL.ZwReadFileScatter
@ stdcall ZwReadRequestData(ptr ptr long ptr long ptr)  NTDLL.ZwReadRequestData
@ stdcall ZwReadVirtualMemory(long ptr ptr long ptr)  NTDLL.ZwReadVirtualMemory
@ stdcall ZwRegisterThreadTerminatePort(ptr)  NTDLL.ZwRegisterThreadTerminatePort
@ stdcall ZwReleaseKeyedEvent(ptr ptr long ptr)  NTDLL.ZwReleaseKeyedEvent
@ stdcall ZwReleaseMutant(long ptr)  NTDLL.ZwReleaseMutant
@ stdcall ZwReleaseSemaphore(long long ptr)  NTDLL.ZwReleaseSemaphore
@ stdcall ZwRemoveIoCompletion(ptr ptr ptr ptr ptr)  NTDLL.ZwRemoveIoCompletion
@ stdcall ZwRemoveProcessDebug(ptr ptr)  NTDLL.ZwRemoveProcessDebug
@ stdcall ZwRenameKey(ptr ptr)  NTDLL.ZwRenameKey
@ stdcall ZwReplaceKey(ptr long ptr)  NTDLL.ZwReplaceKey
@ stdcall ZwReplyPort(ptr ptr)  NTDLL.ZwReplyPort
@ stdcall ZwReplyWaitReceivePort(ptr ptr ptr ptr)  NTDLL.ZwReplyWaitReceivePort
@ stdcall ZwReplyWaitReceivePortEx(ptr ptr ptr ptr ptr) NTDLL.ZwReplyWaitReceivePortEx
@ stdcall ZwReplyWaitReplyPort(ptr ptr) NTDLL.ZwReplyWaitReplyPort
@ stdcall ZwRequestDeviceWakeup(ptr) NTDLL.ZwRequestDeviceWakeup
@ stdcall ZwRequestPort(ptr ptr) NTDLL.ZwRequestPort
@ stdcall ZwRequestWaitReplyPort(ptr ptr ptr) NTDLL.ZwRequestWaitReplyPort
@ stdcall ZwRequestWakeupLatency(long) NTDLL.ZwRequestWakeupLatency
@ stdcall ZwResetEvent(long ptr) NTDLL.ZwResetEvent
@ stdcall ZwResetWriteWatch(long ptr long) NTDLL.ZwResetWriteWatch
@ stdcall ZwRestoreKey(long long long) NTDLL.ZwRestoreKey
@ stdcall ZwResumeProcess(ptr) NTDLL.ZwResumeProcess
@ stdcall ZwResumeThread(long long) NTDLL.ZwResumeThread
@ stdcall ZwSaveKey(long long) NTDLL.ZwSaveKey
@ stdcall ZwSaveKeyEx(ptr ptr long) NTDLL.ZwSaveKeyEx
@ stdcall ZwSaveMergedKeys(ptr ptr ptr) NTDLL.ZwSaveMergedKeys
@ stdcall ZwSecureConnectPort(ptr ptr ptr ptr ptr ptr ptr ptr ptr) NTDLL.ZwSecureConnectPort
@ stdcall ZwSetBootEntryOrder(ptr ptr) NTDLL.ZwSetBootEntryOrder
@ stdcall ZwSetBootOptions(ptr long) NTDLL.ZwSetBootOptions
@ stdcall ZwSetContextThread(long ptr) NTDLL.ZwSetContextThread
@ stdcall ZwSetDebugFilterState(long long long) NTDLL.ZwSetDebugFilterState
@ stdcall ZwSetDefaultHardErrorPort(ptr) NTDLL.ZwSetDefaultHardErrorPort
@ stdcall ZwSetDefaultLocale(long long) NTDLL.ZwSetDefaultLocale
@ stdcall ZwSetDefaultUILanguage(long) NTDLL.ZwSetDefaultUILanguage
@ stdcall ZwSetDriverEntryOrder(ptr ptr) NTDLL.ZwSetDriverEntryOrder
@ stdcall ZwSetEaFile(long ptr ptr long) NTDLL.ZwSetEaFile
@ stdcall ZwSetEvent(long long) NTDLL.ZwSetEvent
@ stdcall ZwSetEventBoostPriority(ptr) NTDLL.ZwSetEventBoostPriority
@ stdcall ZwSetHighEventPair(ptr) NTDLL.ZwSetHighEventPair
@ stdcall ZwSetHighWaitLowEventPair(ptr) NTDLL.ZwSetHighWaitLowEventPair
@ stdcall ZwSetInformationDebugObject(ptr long ptr long ptr) NTDLL.ZwSetInformationDebugObject
@ stdcall ZwSetInformationFile(long long long long long) NTDLL.ZwSetInformationFile
@ stdcall ZwSetInformationJobObject(long long ptr long) NTDLL.ZwSetInformationJobObject
@ stdcall ZwSetInformationKey(long long ptr long) NTDLL.ZwSetInformationKey
@ stdcall ZwSetInformationObject(long long ptr long) NTDLL.ZwSetInformationObject
@ stdcall ZwSetInformationProcess(long long long long) NTDLL.ZwSetInformationProcess
@ stdcall ZwSetInformationThread(long long ptr long) NTDLL.ZwSetInformationThread
@ stdcall ZwSetInformationToken(long long ptr long) NTDLL.ZwSetInformationToken
@ stdcall ZwSetIntervalProfile(long long) NTDLL.ZwSetIntervalProfile
@ stdcall ZwSetIoCompletion(ptr long ptr long long) NTDLL.ZwSetIoCompletion
@ stdcall ZwSetLdtEntries(long int64 long int64) NTDLL.ZwSetLdtEntries
@ stdcall ZwSetLowEventPair(ptr) NTDLL.ZwSetLowEventPair
@ stdcall ZwSetLowWaitHighEventPair(ptr) NTDLL.ZwSetLowWaitHighEventPair
@ stdcall ZwSetQuotaInformationFile(ptr ptr ptr long) NTDLL.ZwSetQuotaInformationFile
@ stdcall ZwSetSecurityObject(long long ptr) NTDLL.ZwSetSecurityObject
@ stdcall ZwSetSystemEnvironmentValue(ptr ptr) NTDLL.ZwSetSystemEnvironmentValue
@ stdcall ZwSetSystemEnvironmentValueEx(ptr ptr ptr ptr ptr)  NTDLL.ZwSetSystemEnvironmentValueEx
@ stdcall ZwSetSystemInformation(long ptr long) NTDLL.ZwSetSystemInformation
@ stdcall ZwSetSystemPowerState(long long long) NTDLL.ZwSetSystemPowerState
@ stdcall ZwSetSystemTime(ptr ptr) NTDLL.ZwSetSystemTime
@ stdcall ZwSetThreadExecutionState(long ptr) NTDLL.ZwSetThreadExecutionState
@ stdcall ZwSetTimer(long ptr ptr ptr long long ptr) NTDLL.ZwSetTimer
@ stdcall ZwSetTimerResolution(long long ptr) NTDLL.ZwSetTimerResolution
@ stdcall ZwSetUuidSeed(ptr) NTDLL.ZwSetUuidSeed
@ stdcall ZwSetValueKey(long long long long long long) NTDLL.ZwSetValueKey
@ stdcall ZwSetVolumeInformationFile(long ptr ptr long long) NTDLL.ZwSetVolumeInformationFile
@ stdcall ZwShutdownSystem(long) NTDLL.ZwShutdownSystem
@ stdcall ZwSignalAndWaitForSingleObject(long long long ptr) NTDLL.ZwSignalAndWaitForSingleObject
@ stdcall ZwStartProfile(ptr) NTDLL.ZwStartProfile
@ stdcall ZwStopProfile(ptr) NTDLL.ZwStopProfile
@ stdcall ZwSuspendProcess(ptr) NTDLL.ZwSuspendProcess
@ stdcall ZwSuspendThread(long ptr) NTDLL.ZwSuspendThread
@ stdcall ZwSystemDebugControl(long ptr long ptr long ptr) NTDLL.ZwSystemDebugControl
@ stdcall ZwTerminateJobObject(long long) NTDLL.ZwTerminateJobObject
@ stdcall ZwTerminateProcess(long long) NTDLL.ZwTerminateProcess
@ stdcall ZwTerminateThread(long long) NTDLL.ZwTerminateThread
@ stdcall ZwTestAlert() NTDLL.ZwTestAlert
@ stdcall ZwTraceEvent(long long long ptr) NTDLL.ZwTraceEvent
@ stdcall ZwTranslateFilePath(ptr long ptr long) NTDLL.ZwTranslateFilePath
@ stdcall ZwUnloadDriver(ptr) NTDLL.ZwUnloadDriver
@ stdcall ZwUnloadKey2(ptr long) NTDLL.ZwUnloadKey2
@ stdcall ZwUnloadKey(long) NTDLL.ZwUnloadKey
@ stdcall ZwUnloadKeyEx(ptr ptr) NTDLL.ZwUnloadKeyEx
@ stdcall ZwUnlockFile(long ptr ptr ptr ptr) NTDLL.ZwUnlockFile
@ stdcall ZwUnlockVirtualMemory(long ptr ptr long) NTDLL.ZwUnlockVirtualMemory
@ stdcall ZwUnmapViewOfSection(long ptr) NTDLL.ZwUnmapViewOfSection
@ stdcall ZwVdmControl(long ptr) NTDLL.ZwVdmControl
@ stdcall ZwWaitForDebugEvent(ptr long ptr ptr) NTDLL.ZwWaitForDebugEvent
@ stdcall ZwWaitForKeyedEvent(ptr ptr long ptr) NTDLL.ZwWaitForKeyedEvent
@ stdcall ZwWaitForMultipleObjects32(long ptr long long ptr) NTDLL.ZwWaitForMultipleObjects32
@ stdcall ZwWaitForMultipleObjects(long ptr long long ptr) NTDLL.ZwWaitForMultipleObjects
@ stdcall ZwWaitForSingleObject(long long long) NTDLL.ZwWaitForSingleObject
@ stdcall ZwWaitHighEventPair(ptr) NTDLL.ZwWaitHighEventPair
@ stdcall ZwWaitLowEventPair(ptr) NTDLL.ZwWaitLowEventPair
@ stdcall ZwWriteFile(long long ptr ptr ptr ptr long ptr ptr) NTDLL.ZwWriteFile
@ stdcall ZwWriteFileGather(long long ptr ptr ptr ptr long ptr ptr) NTDLL.ZwWriteFileGather
@ stdcall ZwWriteRequestData(ptr ptr long ptr long ptr) NTDLL.ZwWriteRequestData
@ stdcall ZwWriteVirtualMemory(long ptr ptr long ptr) NTDLL.ZwWriteVirtualMemory
@ stdcall ZwYieldExecution() NTDLL.ZwYieldExecution
@ cdecl -arch=i386 _CIcos() NTDLL._CIcos
@ cdecl -arch=i386 _CIlog() NTDLL._CIlog
@ cdecl -arch=i386 _CIpow() NTDLL._CIpow
@ cdecl -arch=i386 _CIsin() NTDLL._CIsin
@ cdecl -arch=i386 _CIsqrt() NTDLL._CIsqrt
@ cdecl -arch=x86_64,arm __C_specific_handler(ptr long ptr ptr) NTDLL.__C_specific_handler
@ cdecl __isascii(long) NTDLL.__isascii
@ cdecl __iscsym(long) NTDLL.__iscsym
@ cdecl __iscsymf(long) NTDLL.__iscsymf
@ cdecl __toascii(long) NTDLL.__toascii
@ cdecl -arch=i386 -ret64 _alldiv(double double) NTDLL._alldiv
@ cdecl -arch=i386 _alldvrm() NTDLL._alldvrm
@ cdecl -arch=i386 -ret64 _allmul(double double) NTDLL._allmul
@ cdecl -arch=i386 -norelay _alloca_probe() NTDLL._alloca_probe
@ cdecl -arch=i386 -ret64 _allrem(double double) NTDLL._allrem
@ cdecl -arch=i386 _allshl() NTDLL._allshl
@ cdecl -arch=i386 _allshr() NTDLL._allshr
@ cdecl -ret64 _atoi64(str) NTDLL._atoi64
@ cdecl -arch=i386 -ret64 _aulldiv(double double) NTDLL._aulldiv
@ cdecl -arch=i386 _aulldvrm() NTDLL._aulldvrm
@ cdecl -arch=i386 -ret64 _aullrem(double double) NTDLL._aullrem
@ cdecl -arch=i386 _aullshr() NTDLL._aullshr
@ extern -arch=i386 _chkstk NTDLL._chkstk
@ cdecl -arch=i386,x86_64,arm _fltused() NTDLL._fltused
@ cdecl -arch=i386 -ret64 _ftol() NTDLL._ftol
@ cdecl _i64toa(double ptr long) NTDLL._i64toa
@ cdecl _i64tow(double ptr long) NTDLL._i64tow
@ cdecl _itoa(long ptr long) NTDLL._itoa
@ cdecl _itow(long ptr long) NTDLL._itow
@ cdecl _lfind(ptr ptr ptr long ptr) NTDLL._lfind
@ cdecl -arch=x86_64 _local_unwind() NTDLL._local_unwind
@ cdecl _ltoa(long ptr long) NTDLL._ltoa
@ cdecl _ltow(long ptr long) NTDLL._ltow
@ cdecl _memccpy(ptr ptr long long) NTDLL._memccpy
@ cdecl _memicmp(str str long) NTDLL._memicmp
@ cdecl -arch=x86_64 _setjmp(ptr ptr) NTDLL._setjmp
@ cdecl -arch=x86_64 _setjmpex(ptr ptr) NTDLL._setjmpex
@ varargs _snprintf(ptr long str) NTDLL._snprintf
@ varargs _snwprintf(ptr long wstr) NTDLL._snwprintf
@ cdecl _splitpath(str ptr ptr ptr ptr) NTDLL._splitpath
@ cdecl _strcmpi(str str)  NTDLL._strcmpi
@ cdecl _stricmp(str str) NTDLL._stricmp
@ cdecl _strlwr(str) NTDLL._strlwr
@ cdecl _strnicmp(str str long) NTDLL._strnicmp
@ cdecl _strupr(str) NTDLL._strupr
@ cdecl _tolower(long) NTDLL._tolower
@ cdecl _toupper(long) NTDLL._toupper
@ cdecl _ui64toa(double ptr long) NTDLL._ui64toa
@ cdecl _ui64tow(double ptr long) NTDLL._ui64tow
@ cdecl _ultoa(long ptr long) NTDLL._ultoa
@ cdecl _ultow(long ptr long) NTDLL._ultow
@ cdecl _vscwprintf(wstr ptr) NTDLL._vscwprintf
@ cdecl _vsnprintf(ptr long str ptr) NTDLL._vsnprintf
@ cdecl _vsnwprintf(ptr long wstr ptr) NTDLL._vsnwprintf
@ cdecl _wcsicmp(wstr wstr) NTDLL._wcsicmp
@ cdecl _wcslwr(wstr) NTDLL._wcslwr
@ cdecl _wcsnicmp(wstr wstr long) NTDLL._wcsnicmp
@ cdecl _wcstoui64(wstr ptr long) NTDLL._wcstoui64
@ cdecl _wcsupr(wstr) NTDLL._wcsupr
@ cdecl _wtoi(wstr) NTDLL._wtoi
@ cdecl _wtoi64(wstr) NTDLL._wtoi64
@ cdecl _wtol(wstr) NTDLL._wtol
@ cdecl abs(long) NTDLL.abs
@ cdecl -arch=i386,x86_64 atan(double) NTDLL.atan
@ cdecl atoi(str) NTDLL.atoi
@ cdecl atol(str) NTDLL.atol
@ cdecl bsearch(ptr ptr long long ptr) NTDLL.bsearch
@ cdecl ceil(double) NTDLL.ceil
@ cdecl cos(double) NTDLL.cos
@ cdecl fabs(double) NTDLL.fabs
@ cdecl floor(double) NTDLL.floor
@ cdecl isalnum(long) NTDLL.isalnum
@ cdecl isalpha(long) NTDLL.isalpha
@ cdecl iscntrl(long) NTDLL.iscntrl
@ cdecl isdigit(long) NTDLL.isdigit
@ cdecl isgraph(long) NTDLL.isgraph
@ cdecl islower(long) NTDLL.islower
@ cdecl isprint(long) NTDLL.isprint
@ cdecl ispunct(long) NTDLL.ispunct
@ cdecl isspace(long) NTDLL.isspace
@ cdecl isupper(long) NTDLL.isupper
@ cdecl iswalpha(long) NTDLL.iswalpha
@ cdecl iswctype(long long) NTDLL.iswctype
@ cdecl iswdigit(long) NTDLL.iswdigit
@ cdecl iswlower(long) NTDLL.iswlower
@ cdecl iswspace(long) NTDLL.iswspace
@ cdecl iswxdigit(long) NTDLL.iswxdigit
@ cdecl isxdigit(long) NTDLL.isxdigit
@ cdecl labs(long) NTDLL.labs
@ cdecl -arch=i386,x86_64 log(double) NTDLL.log
@ cdecl -arch=x86_64 longjmp(ptr) NTDLL.longjmp
@ cdecl mbstowcs(ptr str long) NTDLL.mbstowcs
@ cdecl memchr(ptr long long) NTDLL.memchr
@ cdecl memcmp(ptr ptr long) NTDLL.memcmp
@ cdecl memcpy(ptr ptr long)  NTDLL.memcpy
@ cdecl memmove(ptr ptr long) NTDLL.memmove
@ cdecl memset(ptr long long) NTDLL.memset
@ cdecl -arch=i386,x86_64 pow(double double) NTDLL.pow
@ cdecl qsort(ptr long long ptr) NTDLL.qsort
@ cdecl sin(double) NTDLL.sin
@ varargs sprintf(ptr str) NTDLL.sprintf
@ cdecl -arch=i386,x86_64 sqrt(double) NTDLL.sqrt
@ varargs sscanf(str str) NTDLL.sscanf
@ cdecl strcat(str str) NTDLL.strcat
@ cdecl strchr(str long) NTDLL.strchr
@ cdecl strcmp(str str) NTDLL.strcmp
@ cdecl strcpy(ptr str) NTDLL.strcpy
@ cdecl strcspn(str str) NTDLL.strcspn
@ cdecl strlen(str) NTDLL.strlen
@ cdecl strncat(str str long) NTDLL.strncat
@ cdecl strncmp(str str long) NTDLL.strncmp
@ cdecl strncpy(ptr str long) NTDLL.strncpy
@ cdecl strpbrk(str str) NTDLL.strpbrk
@ cdecl strrchr(str long) NTDLL.strrchr
@ cdecl strspn(str str) NTDLL.strspn
@ cdecl strstr(str str) NTDLL.strstr
@ cdecl strtol(str ptr long) NTDLL.strtol
@ cdecl strtoul(str ptr long) NTDLL.strtoul
@ varargs swprintf(ptr wstr) NTDLL.swprintf
@ cdecl -arch=i386,x86_64 tan(double) NTDLL.tan
@ cdecl tolower(long) NTDLL.tolower
@ cdecl toupper(long) NTDLL.toupper
@ cdecl towlower(long) NTDLL.towlower
@ cdecl towupper(long) NTDLL.towupper
@ stdcall vDbgPrintEx(long long str ptr) NTDLL.vDbgPrintEx
@ stdcall vDbgPrintExWithPrefix(str long long str ptr) NTDLL.vDbgPrintExWithPrefix
@ cdecl vsprintf(ptr str ptr) NTDLL.vsprintf
@ cdecl wcscat(wstr wstr) NTDLL.wcscat
@ cdecl wcschr(wstr long) NTDLL.wcschr
@ cdecl wcscmp(wstr wstr) NTDLL.wcscmp
@ cdecl wcscpy(ptr wstr) NTDLL.wcscpy
@ cdecl wcscspn(wstr wstr) NTDLL.wcscspn
@ cdecl wcslen(wstr) NTDLL.wcslen
@ cdecl wcsncat(wstr wstr long) NTDLL.wcsncat
@ cdecl wcsncmp(wstr wstr long) NTDLL.wcsncmp
@ cdecl wcsncpy(ptr wstr long) NTDLL.wcsncpy
@ cdecl wcspbrk(wstr wstr) NTDLL.wcspbrk
@ cdecl wcsrchr(wstr long) NTDLL.wcsrchr
@ cdecl wcsspn(wstr wstr) NTDLL.wcsspn
@ cdecl wcsstr(wstr wstr) NTDLL.wcsstr
@ cdecl wcstol(wstr ptr long) NTDLL.wcstol
@ cdecl wcstombs(ptr ptr long) NTDLL.wcstombs
@ cdecl wcstoul(wstr ptr long) NTDLL.wcstoul
