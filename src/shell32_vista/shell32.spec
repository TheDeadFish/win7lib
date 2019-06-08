2 stdcall SHChangeNotifyRegister(long long long long long ptr) SHELL32.SHChangeNotifyRegister
3 stdcall SHDefExtractIconA(str long long ptr ptr long) SHELL32.SHDefExtractIconA
4 stdcall SHChangeNotifyDeregister(long) SHELL32.SHChangeNotifyDeregister
5 stdcall -noname SHChangeNotifyUpdateEntryList(long long long long) SHELL32.#5
6 stdcall SHDefExtractIconW(wstr long long ptr ptr long) SHELL32.SHDefExtractIconW
7 stdcall -noname SHLookupIconIndexA(str long long) SHELL32.#7
8 stdcall -noname SHLookupIconIndexW(wstr long long) SHELL32.#8
9 stdcall PifMgr_OpenProperties(wstr wstr long long) SHELL32.PifMgr_OpenProperties
10 stdcall PifMgr_GetProperties(ptr wstr ptr long long) SHELL32.PifMgr_GetProperties
11 stdcall PifMgr_SetProperties(ptr wstr ptr long long) SHELL32.PifMgr_SetProperties
12 stdcall -noname SHStartNetConnectionDialogA(ptr str long) SHELL32.#12
13 stdcall PifMgr_CloseProperties(ptr long) SHELL32.PifMgr_CloseProperties
14 stdcall SHStartNetConnectionDialogW(ptr wstr long) SHELL32.SHStartNetConnectionDialogW
15 stdcall -noname ILGetDisplayName(ptr ptr) SHELL32.#15
16 stdcall ILFindLastID(ptr) SHELL32.ILFindLastID
17 stdcall ILRemoveLastID(ptr) SHELL32.ILRemoveLastID
18 stdcall ILClone(ptr) SHELL32.ILClone
19 stdcall ILCloneFirst(ptr) SHELL32.ILCloneFirst
20 stdcall -noname ILGlobalClone(ptr) SHELL32.#20
21 stdcall ILIsEqual(ptr ptr) SHELL32.ILIsEqual
22 stdcall DAD_DragEnterEx2(ptr long long ptr) SHELL32.DAD_DragEnterEx2
23 stdcall ILIsParent(ptr ptr long) SHELL32.ILIsParent
24 stdcall ILFindChild(ptr ptr) SHELL32.ILFindChild
25 stdcall ILCombine(ptr ptr) SHELL32.ILCombine
26 stdcall ILLoadFromStream(ptr ptr) SHELL32.ILLoadFromStream
27 stdcall ILSaveToStream(ptr ptr) SHELL32.ILSaveToStream
28 stdcall SHILCreateFromPath(ptr ptr ptr)  SHELL32.SHILCreateFromPath
29 stdcall -noname PathIsRoot(ptr)  SHELL32.#29
30 stdcall -noname PathBuildRoot(ptr long)  SHELL32.#30
31 stdcall -noname PathFindExtension(wstr)  SHELL32.#31
32 stdcall -noname PathAddBackslash(wstr)  SHELL32.#32
33 stdcall -noname PathRemoveBlanks(wstr)  SHELL32.#33
34 stdcall -noname PathFindFileName(wstr)  SHELL32.#34
35 stdcall -noname PathRemoveFileSpec(ptr)  SHELL32.#35
36 stdcall -noname PathAppend(ptr ptr)  SHELL32.#36
37 stdcall -noname PathCombine(wstr wstr wstr)  SHELL32.#37
38 stdcall -noname PathStripPath(wstr)  SHELL32.#38
39 stdcall -noname PathIsUNC(wstr)  SHELL32.#39
40 stdcall -noname PathIsRelative(wstr)  SHELL32.#40
41 stdcall IsLFNDriveA(str) SHELL32.IsLFNDriveA
42 stdcall IsLFNDriveW(wstr) SHELL32.IsLFNDriveW
43 stdcall PathIsExe(ptr)  SHELL32.PathIsExe
44 stub -noname Control_RunDLLNoFallback SHELL32.#44
45 stdcall -noname PathFileExists(ptr)  SHELL32.#45
46 stdcall -noname PathMatchSpec(wstr wstr)  SHELL32.#46
47 stdcall PathMakeUniqueName(ptr long ptr ptr ptr)  SHELL32.PathMakeUniqueName
48 stdcall -noname PathSetDlgItemPath(long long wstr)  SHELL32.#48
49 stdcall PathQualify(ptr)  SHELL32.PathQualify
50 stdcall -noname PathStripToRoot(wstr)  SHELL32.#50
51 stdcall PathResolve(str long long)  SHELL32.PathResolve
52 stdcall -noname PathGetArgs(wstr)  SHELL32.#52
53 stdcall -noname IsSuspendAllowed() SHELL32.#53
54 stdcall -noname LogoffWindowsDialog(ptr) SHELL32.#54
55 stdcall -noname PathQuoteSpaces(wstr)  SHELL32.#55
56 stdcall -noname PathUnquoteSpaces(wstr)  SHELL32.#56
57 stdcall -noname PathGetDriveNumber(wstr)  SHELL32.#57
58 stdcall -noname ParseField(str long ptr long)  SHELL32.#58
59 stdcall RestartDialog(long wstr long) SHELL32.RestartDialog
60 stdcall -noname ExitWindowsDialog(long) SHELL32.#60
61 stdcall -noname RunFileDlg(long long long wstr wstr long) SHELL32.#61
62 stdcall PickIconDlg(long long long long) SHELL32.PickIconDlg
63 stdcall GetFileNameFromBrowse(long long long long wstr wstr wstr) SHELL32.GetFileNameFromBrowse
64 stdcall DriveType(long) SHELL32.DriveType
65 stdcall -noname InvalidateDriveType(long) SHELL32.#65
66 stdcall IsNetDrive(long) SHELL32.IsNetDrive
67 stdcall Shell_MergeMenus(long long long long long long) SHELL32.Shell_MergeMenus
68 stdcall SHGetSetSettings(ptr long long) SHELL32.SHGetSetSettings
69 stdcall -noname SHGetNetResource(ptr long ptr long) SHELL32.#69
70 stdcall -noname SHCreateDefClassObject(long long long long long) SHELL32.#70
71 stdcall Shell_GetImageLists(ptr ptr) SHELL32.Shell_GetImageLists
72 stdcall Shell_GetCachedImageIndex(ptr ptr long)  SHELL32.Shell_GetCachedImageIndex
73 stdcall SHShellFolderView_Message(long long long) SHELL32.SHShellFolderView_Message
74 stdcall SHCreateStdEnumFmtEtc(long ptr ptr) SHELL32.SHCreateStdEnumFmtEtc
75 stdcall PathYetAnotherMakeUniqueName(ptr wstr wstr wstr) SHELL32.PathYetAnotherMakeUniqueName
76 stdcall -noname DragQueryInfo(ptr ptr) SHELL32.#76
77 stdcall SHMapPIDLToSystemImageListIndex(ptr ptr ptr) SHELL32.SHMapPIDLToSystemImageListIndex
78 stdcall -noname OleStrToStrN(str long wstr long)  SHELL32.#78
79 stdcall -noname StrToOleStrN(wstr long str long)  SHELL32.#79
80 stdcall SHOpenPropSheetW(wstr ptr long ptr ptr ptr wstr) SHELL32.SHOpenPropSheetW
81 stdcall OpenAs_RunDLL(long long str long)  SHELL32.OpenAs_RunDLL
82 stdcall -noname DDECreatePostNotify(ptr) SHELL32.#82
83 stdcall -noname CIDLData_CreateFromIDArray(ptr long ptr ptr) SHELL32.#83
84 stdcall -noname SHIsBadInterfacePtr(ptr long) SHELL32.#84
85 stdcall OpenRegStream(long str str long) shlwapi.SHOpenRegStreamA
86 stdcall -noname SHRegisterDragDrop(long ptr) SHELL32.#86
87 stdcall -noname SHRevokeDragDrop(long) SHELL32.#87
88 stdcall SHDoDragDrop(long ptr ptr long ptr) SHELL32.SHDoDragDrop
89 stdcall SHCloneSpecialIDList(long long long) SHELL32.SHCloneSpecialIDList
90 stdcall SHFindFiles(ptr ptr) SHELL32.SHFindFiles
91 stdcall -noname SHFindComputer(ptr ptr) SHELL32.#91
92 stdcall PathGetShortPath(ptr)  SHELL32.PathGetShortPath
93 stdcall -noname Win32CreateDirectory(wstr ptr)  SHELL32.#93
94 stdcall -noname Win32RemoveDirectory(wstr)  SHELL32.#94
95 stdcall -noname SHLogILFromFSIL(ptr) SHELL32.#95
96 stdcall -noname StrRetToStrN(ptr long ptr ptr)  SHELL32.#96
97 stdcall -noname SHWaitForFileToOpen(long long long) SHELL32.#97
98 stdcall SHGetRealIDL(ptr ptr ptr) SHELL32.SHGetRealIDL
99 stdcall -noname SetAppStartingCursor(long long) SHELL32.#99
100 stdcall SHRestricted(long) SHELL32.SHRestricted
101 stdcall OpenAs_RunDLLA(long long str long) SHELL32.OpenAs_RunDLLA
102 stdcall SHCoCreateInstance(wstr ptr long ptr ptr) SHELL32.SHCoCreateInstance
103 stdcall SignalFileOpen(ptr) SHELL32.SignalFileOpen
104 stdcall OpenAs_RunDLLW(long long wstr long) SHELL32.OpenAs_RunDLLW
105 stdcall Activate_RunDLL(long ptr ptr ptr) SHELL32.Activate_RunDLL
106 stdcall AppCompat_RunDLLW(ptr ptr wstr long) SHELL32.AppCompat_RunDLLW
107 stdcall CheckEscapesA(str long) SHELL32.CheckEscapesA
108 stdcall CheckEscapesW(wstr long) SHELL32.CheckEscapesW
109 stdcall CommandLineToArgvW(wstr ptr) SHELL32.CommandLineToArgvW
110 stdcall Control_FillCache_RunDLL(long long long long)  SHELL32.Control_FillCache_RunDLL
111 stdcall Control_FillCache_RunDLLA(long long long long) SHELL32.Control_FillCache_RunDLLA
112 stdcall Control_FillCache_RunDLLW(long long long long) SHELL32.Control_FillCache_RunDLLW
113 stdcall Control_RunDLL(ptr ptr str long)  SHELL32.Control_RunDLL
114 stdcall Control_RunDLLA(ptr ptr str long) SHELL32.Control_RunDLLA
115 stdcall Control_RunDLLAsUserW(ptr ptr wstr long) SHELL32.Control_RunDLLAsUserW
116 stdcall Control_RunDLLW(ptr ptr wstr long) SHELL32.Control_RunDLLW
@ stdcall -private DllCanUnloadNow() SHELL32.DllCanUnloadNow
@ stdcall -private DllGetClassObject(ptr ptr ptr) SHELL32.DllGetClassObject
119 stdcall IsLFNDrive(ptr)  SHELL32.IsLFNDrive
@ stdcall -private DllGetVersion(ptr) SHELL32.DllGetVersion
121 stdcall SHFlushClipboard() SHELL32.SHFlushClipboard
122 stdcall -noname RunDll_CallEntry16(long long long str long) SHELL32.#122
123 stdcall -noname SHFreeUnusedLibraries() SHELL32.#123
@ stdcall -private DllInstall(long wstr) SHELL32.DllInstall
@ stdcall -private DllRegisterServer() SHELL32.DllRegisterServer
126 stdcall -noname SHOutOfMemoryMessageBox(long long long) SHELL32.#126
127 stdcall -noname SHWinHelp(long long long long) SHELL32.#127
128 stdcall -noname SHDllGetClassObject(ptr ptr ptr)  SHELL32.#128
129 stdcall DAD_AutoScroll(long ptr ptr) SHELL32.DAD_AutoScroll
130 stdcall -noname DAD_DragEnter(long) SHELL32.#130
131 stdcall DAD_DragEnterEx(long double) SHELL32.DAD_DragEnterEx
132 stdcall DAD_DragLeave() SHELL32.DAD_DragLeave
@ stdcall -private DllUnregisterServer() SHELL32.DllUnregisterServer
134 stdcall DAD_DragMove(double) SHELL32.DAD_DragMove
135 stdcall DoEnvironmentSubstA(str str) SHELL32.DoEnvironmentSubstA
136 stdcall DAD_SetDragImage(long long) SHELL32.DAD_SetDragImage
137 stdcall DAD_ShowDragImage(long) SHELL32.DAD_ShowDragImage
138 stdcall DoEnvironmentSubstW(wstr wstr) SHELL32.DoEnvironmentSubstW
139 stdcall DragAcceptFiles(long long) SHELL32.DragAcceptFiles
140 stdcall DragFinish(long) SHELL32.DragFinish
141 stdcall DragQueryFile(long long ptr long)  SHELL32.DragQueryFile
142 stdcall DragQueryFileA(long long ptr long) SHELL32.DragQueryFileA
143 stdcall DragQueryFileAorW(ptr long wstr long long long) SHELL32.DragQueryFileAorW
144 stdcall DragQueryFileW(long long ptr long) SHELL32.DragQueryFileW
145 stdcall -noname PathFindOnPath(wstr wstr)  SHELL32.#145
146 stdcall -noname RLBuildListOfPaths() SHELL32.#146
147 stdcall SHCLSIDFromString(long long)  SHELL32.SHCLSIDFromString
148 stdcall SHMapIDListToImageListIndexAsync(ptr ptr ptr long ptr ptr ptr ptr ptr) SHELL32.SHMapIDListToImageListIndexAsync
149 stdcall SHFind_InitMenuPopup(long long long long) SHELL32.SHFind_InitMenuPopup
150 stdcall DragQueryPoint(long ptr) SHELL32.DragQueryPoint
151 stdcall SHLoadOLE(long) SHELL32.SHLoadOLE
152 stdcall ILGetSize(ptr) SHELL32.ILGetSize
153 stdcall ILGetNext(ptr) SHELL32.ILGetNext
154 stdcall ILAppendID(long long long) SHELL32.ILAppendID
155 stdcall ILFree(ptr) SHELL32.ILFree
156 stdcall -noname ILGlobalFree(ptr) SHELL32.#156
157 stdcall ILCreateFromPath(ptr)  SHELL32.ILCreateFromPath
158 stdcall -noname PathGetExtension(wstr long long)  SHELL32.#158
159 stdcall -noname PathIsDirectory(wstr)  SHELL32.#159
160 stdcall -noname SHNetConnectionDialog(ptr wstr long) SHELL32.#160
161 stdcall SHRunControlPanel(long long) SHELL32.SHRunControlPanel
162 stdcall SHSimpleIDListFromPath(ptr)  SHELL32.SHSimpleIDListFromPath
163 stdcall -noname StrToOleStr(wstr str)  SHELL32.#163
164 stdcall Win32DeleteFile(wstr)  SHELL32.Win32DeleteFile
165 stdcall SHCreateDirectory(long ptr) SHELL32.SHCreateDirectory
166 stdcall CallCPLEntry16(long long long long long long) SHELL32.CallCPLEntry16
167 stdcall SHAddFromPropSheetExtArray(long long long) SHELL32.SHAddFromPropSheetExtArray
168 stdcall SHCreatePropSheetExtArray(long wstr long) SHELL32.SHCreatePropSheetExtArray
169 stdcall SHDestroyPropSheetExtArray(long) SHELL32.SHDestroyPropSheetExtArray
170 stdcall SHReplaceFromPropSheetExtArray(long long long long) SHELL32.SHReplaceFromPropSheetExtArray
171 stdcall PathCleanupSpec(ptr ptr) SHELL32.PathCleanupSpec
172 stdcall -noname SHCreateLinks(long str ptr long ptr) SHELL32.#172
173 stdcall SHValidateUNC(long long long) SHELL32.SHValidateUNC
174 stdcall SHCreateShellFolderViewEx(ptr ptr) SHELL32.SHCreateShellFolderViewEx
175 stdcall -noname SHGetSpecialFolderPath(long long long long)  SHELL32.#175
176 stdcall SHSetInstanceExplorer(long) SHELL32.SHSetInstanceExplorer
177 stdcall -noname DAD_SetDragImageFromListView(ptr long long) SHELL32.#177
178 stdcall SHObjectProperties(long long wstr wstr) SHELL32.SHObjectProperties
179 stdcall SHGetNewLinkInfoA(str str ptr long long) SHELL32.SHGetNewLinkInfoA
180 stdcall SHGetNewLinkInfoW(wstr wstr ptr long long) SHELL32.SHGetNewLinkInfoW
181 stdcall -noname RegisterShellHook(long long) SHELL32.#181
182 varargs ShellMessageBoxW(long long wstr wstr long) SHELL32.ShellMessageBoxW
183 varargs ShellMessageBoxA(long long str str long) SHELL32.ShellMessageBoxA
184 stdcall -noname ArrangeWindows(long long long long long) SHELL32.#184
185 stdcall -noname SHHandleDiskFull(ptr long) SHELL32.#185
186 stdcall -noname ILGetDisplayNameEx(ptr ptr ptr long) SHELL32.#186
187 stdcall -noname ILGetPseudoNameW(ptr ptr wstr long) SHELL32.#187
188 stdcall -noname ShellDDEInit(long) SHELL32.#188
189 stdcall ILCreateFromPathA(str) SHELL32.ILCreateFromPathA
190 stdcall ILCreateFromPathW(wstr) SHELL32.ILCreateFromPathW
191 stdcall SHUpdateImageA(str long long long) SHELL32.SHUpdateImageA
192 stdcall SHUpdateImageW(wstr long long long) SHELL32.SHUpdateImageW
193 stdcall SHHandleUpdateImage(ptr) SHELL32.SHHandleUpdateImage
194 stdcall -noname SHCreatePropSheetExtArrayEx(long wstr long ptr) SHELL32.#194
195 stdcall SHFree(ptr) SHELL32.SHFree
196 stdcall SHAlloc(long) SHELL32.SHAlloc
197 stdcall -noname SHGlobalDefect(long) SHELL32.#197
198 stdcall -noname SHAbortInvokeCommand() SHELL32.#198
199 stdcall DuplicateIcon(long long) SHELL32.DuplicateIcon
200 stdcall -noname SHCreateDesktop(ptr) SHELL32.#200
201 stdcall -noname SHDesktopMessageLoop(ptr) SHELL32.#201
202 stub -noname DDEHandleViewFolderNotify SHELL32.#202
203 stdcall -noname AddCommasW(long wstr) SHELL32.#203
204 stdcall -noname ShortSizeFormatW(double) SHELL32.#204
205 stdcall -noname Printer_LoadIconsW(wstr ptr ptr) SHELL32.#205
206 stdcall ExtractAssociatedIconA(long str ptr) SHELL32.ExtractAssociatedIconA
207 stdcall ExtractAssociatedIconExA(long str long long) SHELL32.ExtractAssociatedIconExA
208 stdcall ExtractAssociatedIconExW(long wstr long long) SHELL32.ExtractAssociatedIconExW
209 stdcall -noname Int64ToString(int64 wstr long long ptr long) SHELL32.#209
210 stdcall -noname LargeIntegerToString(ptr wstr long long ptr long) SHELL32.#210
211 stdcall -noname Printers_GetPidl(ptr str long long) SHELL32.#211
212 stdcall -noname Printers_AddPrinterPropPages(ptr ptr) SHELL32.#212
213 stdcall -noname Printers_RegisterWindowW(wstr long ptr ptr) SHELL32.#213
214 stdcall -noname Printers_UnregisterWindow(long long) SHELL32.#214
215 stdcall -noname SHStartNetConnectionDialog(long str long) SHELL32.#215
216 stdcall ExtractAssociatedIconW(long wstr ptr) SHELL32.ExtractAssociatedIconW
217 stdcall ExtractIconA(long str long) SHELL32.ExtractIconA
218 stdcall ExtractIconEx(ptr long ptr ptr long)  SHELL32.ExtractIconEx
219 stdcall ExtractIconExA(str long ptr ptr long) SHELL32.ExtractIconExA
220 stdcall ExtractIconExW(wstr long ptr ptr long) SHELL32.ExtractIconExW
221 stdcall ExtractIconResInfoA(ptr str long ptr ptr) SHELL32.ExtractIconResInfoA
222 stdcall ExtractIconResInfoW(ptr wstr long ptr ptr) SHELL32.ExtractIconResInfoW
223 stdcall ExtractIconW(long wstr long) SHELL32.ExtractIconW
224 stdcall ExtractVersionResource16W(wstr ptr) SHELL32.ExtractVersionResource16W
225 stdcall FindExeDlgProc(ptr long ptr ptr) SHELL32.FindExeDlgProc
226 stdcall FindExecutableA(str str ptr) SHELL32.FindExecutableA
227 stdcall FindExecutableW(wstr wstr ptr) SHELL32.FindExecutableW
228 stdcall FreeIconList(long) SHELL32.FreeIconList
229 stdcall InternalExtractIconListA(ptr str ptr) SHELL32.InternalExtractIconListA
230 stdcall -noname FirstUserLogon(wstr wstr) SHELL32.#230
231 stdcall -noname SHSetFolderPathA(long ptr long str) SHELL32.#231
232 stdcall -noname SHSetFolderPathW(long ptr long wstr) SHELL32.#232
233 stdcall -noname SHGetUserPicturePathW(wstr long ptr) SHELL32.#233
234 stdcall -noname SHSetUserPicturePathW(wstr long ptr) SHELL32.#234
235 stdcall -noname SHOpenEffectiveToken(ptr) SHELL32.#235
236 stdcall -noname SHTestTokenPrivilegeW(ptr ptr) SHELL32.#236
237 stdcall -noname SHShouldShowWizards(ptr) SHELL32.#237
238 stdcall InternalExtractIconListW(ptr wstr ptr) SHELL32.InternalExtractIconListW
239 stdcall PathIsSlowW(wstr long) SHELL32.PathIsSlowW
240 stdcall PathIsSlowA(str long) SHELL32.PathIsSlowA
241 stdcall -noname SHGetUserDisplayName(wstr ptr) SHELL32.#241
242 stdcall -noname SHGetProcessDword(long long) SHELL32.#242
243 stdcall -noname SHSetShellWindowEx(ptr ptr) user32.SetShellWindowEx
244 stdcall -noname SHSettingsChanged(ptr ptr) SHELL32.#244
245 stdcall SHTestTokenMembership(ptr ptr) SHELL32.SHTestTokenMembership
246 stub -noname SHInvokePrivilegedFunctionW SHELL32.#246
247 stub -noname SHGetActiveConsoleSessionId SHELL32.#247
248 stdcall -noname SHGetUserSessionId(ptr) SHELL32.#248
249 stdcall -noname PathParseIconLocation(wstr)  SHELL32.#249
250 stdcall -noname PathRemoveExtension(wstr)  SHELL32.#250
251 stdcall -noname PathRemoveArgs(wstr)  SHELL32.#251
252 stdcall -noname PathIsURL(wstr) shlwapi.PathIsURLW
253 stub -noname SHIsCurrentProcessConsoleSession SHELL32.#253
254 stub -noname DisconnectWindowsDialog SHELL32.#254
255 stdcall Options_RunDLL(ptr ptr str long) SHELL32.Options_RunDLL
256 stdcall SHCreateShellFolderView(ptr ptr) SHELL32.SHCreateShellFolderView
257 stdcall -noname SHGetShellFolderViewCB(ptr) SHELL32.#257
258 stdcall -noname LinkWindow_RegisterClass() SHELL32.#258
259 stdcall -noname LinkWindow_UnregisterClass(long) SHELL32.#259
260 stdcall Options_RunDLLA(ptr ptr str long) SHELL32.Options_RunDLLA
261 stdcall Options_RunDLLW(ptr ptr wstr long) SHELL32.Options_RunDLLW
262 stdcall PrintersGetCommand_RunDLL(ptr ptr wstr long) SHELL32.PrintersGetCommand_RunDLL
263 stdcall PrintersGetCommand_RunDLLA(ptr ptr str long) SHELL32.PrintersGetCommand_RunDLLA
264 stdcall PrintersGetCommand_RunDLLW(ptr ptr wstr long) SHELL32.PrintersGetCommand_RunDLLW
265 stdcall RealShellExecuteA(ptr str str str str str str str long ptr) SHELL32.RealShellExecuteA
266 stdcall RealShellExecuteExA(ptr str str str str str str str long ptr long) SHELL32.RealShellExecuteExA
267 stdcall RealShellExecuteExW(ptr str str str str str str str long ptr long) SHELL32.RealShellExecuteExW
268 stdcall RealShellExecuteW(ptr wstr wstr wstr wstr wstr wstr wstr long ptr) SHELL32.RealShellExecuteW
269 stdcall RegenerateUserEnvironment(ptr long) SHELL32.RegenerateUserEnvironment
270 stdcall SHAddToRecentDocs(long ptr) SHELL32.SHAddToRecentDocs
271 stdcall SHAppBarMessage(long ptr) SHELL32.SHAppBarMessage
272 stdcall SHBindToParent(ptr ptr ptr ptr) SHELL32.SHBindToParent
273 stdcall SHBrowseForFolder(ptr)  SHELL32.SHBrowseForFolder
274 stdcall SHBrowseForFolderA(ptr) SHELL32.SHBrowseForFolderA
275 stdcall SHBrowseForFolderW(ptr) SHELL32.SHBrowseForFolderW
276 stdcall SHChangeNotify(long long ptr ptr) SHELL32.SHChangeNotify
277 stdcall SHChangeNotifySuspendResume(long ptr long long) SHELL32.SHChangeNotifySuspendResume
278 stdcall SHCreateDirectoryExA(long str ptr) SHELL32.SHCreateDirectoryExA
279 stdcall SHCreateDirectoryExW(long wstr ptr) SHELL32.SHCreateDirectoryExW
280 stub SHCreateLocalServerRunDll SHELL32.SHCreateLocalServerRunDll
281 stdcall SHCreateProcessAsUserW(ptr) SHELL32.SHCreateProcessAsUserW
282 stdcall SHCreateQueryCancelAutoPlayMoniker(ptr) SHELL32.SHCreateQueryCancelAutoPlayMoniker
283 stdcall SHCreateShellItem(ptr ptr ptr ptr) SHELL32.SHCreateShellItem
284 stdcall SHEmptyRecycleBinA(long str long) SHELL32.SHEmptyRecycleBinA
285 stdcall SHEmptyRecycleBinW(long wstr long) SHELL32.SHEmptyRecycleBinW
286 stub SHEnableServiceObject SHELL32.SHEnableServiceObject
287 stdcall SHEnumerateUnreadMailAccountsW(ptr long ptr long) SHELL32.SHEnumerateUnreadMailAccountsW
288 stdcall SHExtractIconsW(wstr long long long ptr ptr long long) user32.PrivateExtractIconsW
289 stdcall SHFileOperation(ptr)  SHELL32.SHFileOperation
290 stdcall SHFileOperationA(ptr) SHELL32.SHFileOperationA
291 stdcall SHFileOperationW(ptr) SHELL32.SHFileOperationW
292 stdcall SHFormatDrive(long long long long) SHELL32.SHFormatDrive
293 stdcall SHFreeNameMappings(ptr) SHELL32.SHFreeNameMappings
294 stdcall SHGetDataFromIDListA(ptr ptr long ptr long) SHELL32.SHGetDataFromIDListA
295 stdcall SHGetDataFromIDListW(ptr ptr long ptr long) SHELL32.SHGetDataFromIDListW
296 stdcall SHGetDesktopFolder(ptr) SHELL32.SHGetDesktopFolder
297 stdcall SHGetDiskFreeSpaceA(str ptr ptr ptr) kernel32.GetDiskFreeSpaceExA
298 stdcall SHGetDiskFreeSpaceExA(str ptr ptr ptr) kernel32.GetDiskFreeSpaceExA
299 stdcall SHGetDiskFreeSpaceExW(wstr ptr ptr ptr) kernel32.GetDiskFreeSpaceExW
300 stdcall SHGetFileInfo(ptr long ptr long long)  SHELL32.SHGetFileInfo
301 stdcall SHGetFileInfoA(ptr long ptr long long) SHELL32.SHGetFileInfoA
302 stdcall SHGetFileInfoW(ptr long ptr long long) SHELL32.SHGetFileInfoW
303 stdcall SHGetFolderLocation(long long long long ptr) SHELL32.SHGetFolderLocation
304 stdcall SHGetFolderPathA(long long long long ptr) SHELL32.SHGetFolderPathA
305 stdcall SHGetFolderPathAndSubDirA(long long long long str ptr) SHELL32.SHGetFolderPathAndSubDirA
306 stdcall SHGetFolderPathAndSubDirW(long long long long wstr ptr) SHELL32.SHGetFolderPathAndSubDirW
307 stdcall SHGetFolderPathW(long long long long ptr) SHELL32.SHGetFolderPathW
308 stdcall SHGetIconOverlayIndexA(str long) SHELL32.SHGetIconOverlayIndexA
309 stdcall SHGetIconOverlayIndexW(wstr long) SHELL32.SHGetIconOverlayIndexW
310 stdcall SHGetInstanceExplorer(long) SHELL32.SHGetInstanceExplorer
311 stdcall SHGetMalloc(ptr) SHELL32.SHGetMalloc
312 stdcall SHGetNewLinkInfo(str str ptr long long)  SHELL32.SHGetNewLinkInfo
313 stdcall SHGetPathFromIDList(ptr ptr)  SHELL32.SHGetPathFromIDList
314 stdcall SHGetPathFromIDListA(ptr ptr) SHELL32.SHGetPathFromIDListA
315 stdcall SHGetPathFromIDListW(ptr ptr) SHELL32.SHGetPathFromIDListW
316 stdcall SHGetSettings(ptr long) SHELL32.SHGetSettings
317 stdcall SHGetSpecialFolderLocation(long long ptr) SHELL32.SHGetSpecialFolderLocation
318 stdcall SHGetSpecialFolderPathA(long ptr long long) SHELL32.SHGetSpecialFolderPathA
319 stdcall SHGetSpecialFolderPathW(long ptr long long) SHELL32.SHGetSpecialFolderPathW
320 stdcall SHGetUnreadMailCountW (long wstr long ptr wstr long) SHELL32.SHGetUnreadMailCountW
321 stdcall SHHelpShortcuts_RunDLL(long long long long)  SHELL32.SHHelpShortcuts_RunDLL
322 stdcall SHHelpShortcuts_RunDLLA(long long long long) SHELL32.SHHelpShortcuts_RunDLLA
323 stdcall SHHelpShortcuts_RunDLLW(long long long long) SHELL32.SHHelpShortcuts_RunDLLW
324 stdcall SHInvokePrinterCommandA(ptr long str str long) SHELL32.SHInvokePrinterCommandA
325 stdcall SHInvokePrinterCommandW(ptr long wstr wstr long) SHELL32.SHInvokePrinterCommandW
326 stdcall SHIsFileAvailableOffline(wstr ptr) SHELL32.SHIsFileAvailableOffline
327 stdcall SHLoadInProc(long) SHELL32.SHLoadInProc
328 stdcall SHLoadNonloadedIconOverlayIdentifiers() SHELL32.SHLoadNonloadedIconOverlayIdentifiers
329 stdcall SHOpenFolderAndSelectItems(ptr long ptr long) SHELL32.SHOpenFolderAndSelectItems
330 stdcall SHParseDisplayName(wstr ptr ptr long ptr) SHELL32.SHParseDisplayName
331 stdcall SHPathPrepareForWriteA(long ptr str long) SHELL32.SHPathPrepareForWriteA
332 stdcall SHPathPrepareForWriteW(long ptr wstr long) SHELL32.SHPathPrepareForWriteW
333 stdcall SHQueryRecycleBinA(str ptr) SHELL32.SHQueryRecycleBinA
334 stdcall SHQueryRecycleBinW(wstr ptr) SHELL32.SHQueryRecycleBinW
335 stdcall SHSetLocalizedName(wstr wstr long) SHELL32.SHSetLocalizedName
336 stdcall SHSetUnreadMailCountW (wstr long wstr) SHELL32.SHSetUnreadMailCountW
337 stdcall SHUpdateRecycleBinIcon() SHELL32.SHUpdateRecycleBinIcon
338 stdcall SheChangeDirA(str) SHELL32.SheChangeDirA
339 stdcall SheChangeDirExA(str) SHELL32.SheChangeDirExA
340 stdcall SheChangeDirExW(wstr) SHELL32.SheChangeDirExW
341 stdcall SheChangeDirW(wstr) SHELL32.SheChangeDirW
342 stdcall SheConvertPathW(wstr wstr long) SHELL32.SheConvertPathW
343 stdcall SheFullPathA(str long str) SHELL32.SheFullPathA
344 stdcall SheFullPathW(wstr long wstr) SHELL32.SheFullPathW
345 stdcall SheGetCurDrive() SHELL32.SheGetCurDrive
346 stdcall SheGetDirA(long long) SHELL32.SheGetDirA
347 stdcall SheGetDirExW(wstr ptr wstr) SHELL32.SheGetDirExW
348 stdcall SheGetDirW(long long) SHELL32.SheGetDirW
349 stdcall SheGetPathOffsetW(wstr) SHELL32.SheGetPathOffsetW
350 stdcall SheRemoveQuotesA(str) SHELL32.SheRemoveQuotesA
351 stdcall SheRemoveQuotesW(wstr) SHELL32.SheRemoveQuotesW
352 stdcall SheSetCurDrive(long) SHELL32.SheSetCurDrive
353 stdcall SheShortenPathA(str long) SHELL32.SheShortenPathA
354 stdcall SheShortenPathW(wstr long) SHELL32.SheShortenPathW
355 stdcall ShellAboutA(long str str long) SHELL32.ShellAboutA
356 stdcall ShellAboutW(long wstr wstr long) SHELL32.ShellAboutW
357 stdcall ShellExec_RunDLL(ptr ptr wstr long) SHELL32.ShellExec_RunDLL
358 stdcall ShellExec_RunDLLA(ptr ptr str long) SHELL32.ShellExec_RunDLLA
359 stdcall ShellExec_RunDLLW(ptr ptr wstr long) SHELL32.ShellExec_RunDLLW
360 stdcall ShellExecuteA(long str str str str long) SHELL32.ShellExecuteA
361 stdcall ShellExecuteEx(long)  SHELL32.ShellExecuteEx
362 stdcall ShellExecuteExA (long) SHELL32.ShellExecuteExA
363 stdcall ShellExecuteExW (long) SHELL32.ShellExecuteExW
364 stdcall ShellExecuteW(long wstr wstr wstr wstr long) SHELL32.ShellExecuteW
365 stdcall ShellHookProc(long ptr ptr) SHELL32.ShellHookProc
366 stdcall Shell_NotifyIcon(long ptr)  SHELL32.Shell_NotifyIcon
367 stdcall Shell_NotifyIconA(long ptr) SHELL32.Shell_NotifyIconA
368 stdcall Shell_NotifyIconW(long ptr) SHELL32.Shell_NotifyIconW
369 stdcall StrChrA(str long) shlwapi.StrChrA
370 stdcall StrChrIA(str long) shlwapi.StrChrIA
371 stdcall StrChrIW(wstr long) shlwapi.StrChrIW
372 stdcall StrChrW(wstr long) shlwapi.StrChrW
373 stdcall StrCmpNA(str str long) shlwapi.StrCmpNA
374 stdcall StrCmpNIA(str str long) shlwapi.StrCmpNIA
375 stdcall StrCmpNIW(wstr wstr long) shlwapi.StrCmpNIW
376 stdcall StrCmpNW(wstr wstr long) shlwapi.StrCmpNW
377 stdcall StrCpyNA (ptr str long) kernel32.lstrcpynA
378 stdcall StrCpyNW(wstr wstr long) shlwapi.StrCpyNW
379 stdcall StrNCmpA(str str long) shlwapi.StrCmpNA
380 stdcall StrNCmpIA(str str long) shlwapi.StrCmpNIA
381 stdcall StrNCmpIW(wstr wstr long) shlwapi.StrCmpNIW
382 stdcall StrNCmpW(wstr wstr long) shlwapi.StrCmpNW
383 stdcall StrNCpyA (ptr str long) kernel32.lstrcpynA
384 stdcall StrNCpyW(wstr wstr long) shlwapi.StrCpyNW
385 stdcall StrRChrA(str str long) shlwapi.StrRChrA
386 stdcall StrRChrIA(str str long) shlwapi.StrRChrIA
387 stdcall StrRChrIW(wstr wstr long) shlwapi.StrRChrIW
388 stdcall StrRChrW(wstr wstr long) shlwapi.StrRChrW
389 stdcall StrRStrA(str str str) SHELL32.StrRStrA
390 stdcall StrRStrIA(str str str) shlwapi.StrRStrIA
391 stdcall StrRStrIW(wstr wstr wstr) shlwapi.StrRStrIW
392 stdcall StrRStrW(wstr wstr wstr) SHELL32.StrRStrW
393 stdcall StrStrA(str str) shlwapi.StrStrA
394 stdcall StrStrIA(str str) shlwapi.StrStrIA
395 stdcall StrStrIW(wstr wstr) shlwapi.StrStrIW
396 stdcall StrStrW(wstr wstr) shlwapi.StrStrW
397 stdcall WOWShellExecute(ptr str str str str long ptr) SHELL32.WOWShellExecute
520 stdcall SHAllocShared(ptr long long) shlwapi.SHAllocShared
521 stdcall SHLockShared(long long) shlwapi.SHLockShared
522 stdcall SHUnlockShared(ptr) shlwapi.SHUnlockShared
523 stdcall SHFreeShared(long long) shlwapi.SHFreeShared
524 stdcall RealDriveType(long long) SHELL32.RealDriveType
525 stdcall -noname RealDriveTypeFlags(long long) SHELL32.#525
526 stdcall SHFlushSFCache() SHELL32.SHFlushSFCache
640 stdcall -noname NTSHChangeNotifyRegister(long long long long long long) SHELL32.#640
641 stdcall -noname NTSHChangeNotifyDeregister(long) SHELL32.#641
643 stdcall -noname SHChangeNotifyReceive(long long ptr ptr) SHELL32.#643
644 stdcall SHChangeNotification_Lock(long long ptr ptr) SHELL32.SHChangeNotification_Lock
645 stdcall SHChangeNotification_Unlock(long) SHELL32.SHChangeNotification_Unlock
646 stdcall -noname SHChangeRegistrationReceive(ptr long) SHELL32.#646
648 stdcall -noname SHWaitOp_Operate(ptr long) SHELL32.#648
650 stdcall -noname PathIsSameRoot(wstr wstr)  SHELL32.#650
651 stdcall -noname OldReadCabinetState(long long)  SHELL32.#651
652 stdcall WriteCabinetState(long) SHELL32.WriteCabinetState
653 stdcall PathProcessCommand(long long long long)  SHELL32.PathProcessCommand
654 stdcall ReadCabinetState(long long) SHELL32.ReadCabinetState
660 stdcall -noname FileIconInit(long) SHELL32.#660
680 stdcall IsUserAnAdmin() SHELL32.IsUserAnAdmin
681 stdcall -noname SHGetAppCompatFlags(long) shlwapi.SHGetAppCompatFlags
683 stub -noname SHStgOpenStorageW SHELL32.#683
684 stub -noname SHStgOpenStorageA SHELL32.#684
685 stdcall SHPropStgCreate(ptr ptr ptr long long long ptr ptr) SHELL32.SHPropStgCreate
688 stdcall SHPropStgReadMultiple(ptr long long ptr ptr) SHELL32.SHPropStgReadMultiple
689 stdcall SHPropStgWriteMultiple(ptr ptr long ptr ptr long) SHELL32.SHPropStgWriteMultiple
690 stub -noname SHIsLegacyAnsiProperty SHELL32.#690
691 stub -noname SHFileSysBindToStorage SHELL32.#691
700 stdcall CDefFolderMenu_Create(ptr ptr long ptr ptr ptr ptr ptr ptr) SHELL32.CDefFolderMenu_Create
701 stdcall CDefFolderMenu_Create2(ptr ptr long ptr ptr ptr long ptr ptr) SHELL32.CDefFolderMenu_Create2
702 stdcall -noname CDefFolderMenu_MergeMenu(ptr long long ptr) SHELL32.#702
703 stdcall -noname GUIDFromStringA(str ptr) SHELL32.#703
704 stdcall -noname GUIDFromStringW(wstr ptr) SHELL32.#704
707 stdcall -noname SHOpenPropSheetA(str ptr long ptr ptr ptr str) SHELL32.#707
708 stdcall -noname SHGetSetFolderCustomSettingsA(ptr str long) SHELL32.#708
709 stdcall SHGetSetFolderCustomSettingsW(ptr wstr long) SHELL32.SHGetSetFolderCustomSettingsW
711 stdcall -noname CheckWinIniForAssocs() SHELL32.#711
712 stdcall -noname SHCopyMonikerToTemp(ptr wstr wstr long) SHELL32.#712
713 stdcall -noname PathIsTemporaryA(str) SHELL32.#713
714 stdcall -noname PathIsTemporaryW(wstr) SHELL32.#714
715 stdcall -noname SHCreatePropertyBag(ptr ptr) SHELL32.#715
716 stdcall SHMultiFileProperties(ptr long) SHELL32.SHMultiFileProperties
719 stdcall -noname SHParseDarwinIDFromCacheW(wstr wstr) SHELL32.#719
720 stdcall -noname MakeShellURLFromPathA(str str long) SHELL32.#720
721 stdcall -noname MakeShellURLFromPathW(wstr wstr long) SHELL32.#721
722 stub -noname SHCreateInstance SHELL32.#722
723 stdcall -noname SHCreateSessionKey(long ptr) SHELL32.#723
724 stdcall -noname SHIsTempDisplayMode() SHELL32.#724
725 stdcall -noname GetFileDescriptor(ptr long long wstr) SHELL32.#725
726 stdcall -noname CopyStreamUI(ptr ptr ptr) SHELL32.#726
727 stdcall SHGetImageList(long ptr ptr) SHELL32.SHGetImageList
730 stdcall RestartDialogEx(long wstr long long) SHELL32.RestartDialogEx
731 stdcall -noname -stub SHRegisterDarwinLink(long long long) SHELL32.#731
732 stdcall -noname SHReValidateDarwinCache() SHELL32.#732
733 stdcall -noname CheckDiskSpace() SHELL32.#733
740 stub -noname SHCreateFileDataObject SHELL32.#740
743 stdcall SHCreateFileExtractIconW(wstr long ptr ptr) SHELL32.SHCreateFileExtractIconW
744 stub -noname Create_IEnumUICommand SHELL32.#744
745 stub -noname Create_IUIElement SHELL32.#745
747 stdcall SHLimitInputEdit(ptr ptr) SHELL32.SHLimitInputEdit
748 stdcall -noname SHLimitInputCombo(ptr ptr) SHELL32.#748
749 stub SHGetShellStyleHInstance SHELL32.SHGetShellStyleHInstance
750 stub SHGetAttributesFromDataObject SHELL32.SHGetAttributesFromDataObject
751 stub -noname SHSimulateDropOnClsid SHELL32.#751
752 stdcall -noname SHGetComputerDisplayNameW(long long long long) SHELL32.#752
753 stdcall -noname CheckStagingArea() SHELL32.#753
754 stub -noname SHLimitInputEditWithFlags SHELL32.#754
755 stdcall -noname PathIsEqualOrSubFolder(wstr wstr) SHELL32.#755
756 stub -noname DeleteFileThumbnail SHELL32.#756

# vista functions
@ stdcall SHGetStockIconInfo(long long ptr)
@ stdcall SHGetFolderPathEx(ptr long ptr ptr long)
@ stdcall SHGetKnownFolderPath(ptr long ptr ptr)
