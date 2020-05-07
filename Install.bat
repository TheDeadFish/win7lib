:: install.bat <dll_dir> <lib_dir> <bin_dir>

@copy /Y %3\*.dll %1
@del %2\libwin7.a
@libmerge %2\libwin7.a -i ^
	-pntdll_ %3\libntdllexS.a ^
	-pkrnl32_ %3\libkrnl32exS.a ^
	-puser32_ %3\libuser32ex.a ^
	-pshell32_ %3\libshell32ex.a
