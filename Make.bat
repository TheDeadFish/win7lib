@setlocal
@call egccx.bat %1
@set CPATH=%CPATH%;%NTNDK%
@set CFLAGS=%OFLAGS% %PUSH_ARG%
@set CXXFLAGS=%OCCFLG% %PUSH_ARG%
@pushd build
@%CMAKE% ..\.
@mingw32-make
@popd
