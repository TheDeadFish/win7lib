project(kernelEx)
cmake_minimum_required(VERSION 3.12)
include (tools/toolchain-gcc.cmake)
include (tools/gcc.cmake)
include(tools/compilerflags.cmake)
include (tools/spec2def.cmake)
include (tools/exemod.cmake)

if(ARCH STREQUAL "amd64")
	set (BIN_DIR ${CMAKE_SOURCE_DIR}/bin/bin64)
else()	
	set (BIN_DIR ${CMAKE_SOURCE_DIR}/bin/bin32)
endif()

set(CMAKE_SHARED_LIBRARY_PREFIX "")
set(CMAKE_SHARED_MODULE_PREFIX "")
set (CMAKE_MODULE_LINKER_FLAGS "-s -Wl,--gc-sections")
set (CMAKE_SHARED_LINKER_FLAGS ${CMAKE_MODULE_LINKER_FLAGS})





set (CMAKE_LIBRARY_OUTPUT_DIRECTORY ${BIN_DIR})
set (CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${BIN_DIR})
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${BIN_DIR})


add_definitions(-DUNICODE -D_UNICODE -D_WIN32_WINNT=0x502 -DWINVER=0x502)

include_directories(src/include)
add_subdirectory(tools)

add_compile_flags("-Wno-attributes")

# build the libraries
add_subdirectory(src/ntdll_vista)
add_subdirectory(src/kernel32_vista)
add_subdirectory(src/iphlpapi_vista)
add_subdirectory(src/shell32_vista)
add_subdirectory(src/user32_vista)

# build the exm files
if(ARCH STREQUAL "amd64")
	add_subdirectory(src/wow64)
endif()
add_subdirectory(src/kernel32)
add_subdirectory(src/ntdll)
add_subdirectory(src/user32)
add_subdirectory(src/shell32)
