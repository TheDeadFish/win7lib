@setlocal
@call exmod.bat
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@set CXXFLAGS=%OCCFLG% %PUSH_ARG%
@pushd build32
@%CMAKE% ..\. -DMINGW_TOOLCHAIN_PREFIX= -DARCH=i386
@mingw32-make 
@popd
