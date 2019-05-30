@setlocal
@call egccx.bat %1
@set PATH=%CD%\tools;%PATH%
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@pushd build
@%CMAKE% ..\.
@mingw32-make
@popd
