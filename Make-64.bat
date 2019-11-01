@setlocal
@call exmod.bat x64
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@set CXXFLAGS=%OCCFLG% %PUSH_ARG%
@pushd build64
@%CMAKE% ..\. -DMINGW_TOOLCHAIN_PREFIX= -DARCH=amd64
@mingw32-make
@popd