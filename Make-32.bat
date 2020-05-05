@setlocal
@call exmod.bat
@if not exist build32 mkdir build32
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@set CXXFLAGS=%OCCFLG% %PUSH_ARG%
@pushd build32
@%CMAKE% ..\. -DMINGW_TOOLCHAIN_PREFIX= -DARCH=i386
@ninja
@popd

copy /Y bin\bin32\*.dll %PROGRAMS%\lib 
