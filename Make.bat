@setlocal
@call exmod.bat
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@set CXXFLAGS=%OCCFLG% %PUSH_ARG%
@pushd build32
@%CMAKE% ..\. -DMINGW_TOOLCHAIN_PREFIX= -DARCH=i386
@mingw32-make 
@popd
@endlocal

@setlocal
@call exmod.bat x64
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@set CXXFLAGS=%OCCFLG% %PUSH_ARG%
@pushd build64
@%CMAKE% ..\. -DMINGW_TOOLCHAIN_PREFIX= -DARCH=amd64
@mingw32-make
@popd
