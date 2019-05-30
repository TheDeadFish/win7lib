cmake_minimum_required(VERSION 3.12)
include (tools/spec2def.cmake)

set(CMAKE_SHARED_LIBRARY_PREFIX "")
set(CMAKE_SHARED_MODULE_PREFIX "")
set (CMAKE_MODULE_LINKER_FLAGS "-s")

set (CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
set (CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

add_definitions(-DUNICODE -D_UNICODE -D_WIN32_WINNT=0x502 -DWINVER=0x502)

include_directories(src/include)
add_subdirectory(src/kernel32_vista)
add_subdirectory(src/ntdll_vista)
add_subdirectory(src/iphlpapi_vista)
