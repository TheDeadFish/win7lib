@setlocal
@call exmod.bat x64
@if not exist build64 mkdir build64
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@set CXXFLAGS=%OCCFLG% %PUSH_ARG% -fno-exceptions
@pushd build64
@%CMAKE% ..\. -DMINGW_TOOLCHAIN_PREFIX= -DARCH=amd64
@ninja
@popd

Install.bat %PROGRAMS%\lib\lib64 %PROGRAMS%\local\lib64 bin\bin64


copy /Y bin\bin64\*.dll %PROGRAMS%\lib\lib64
