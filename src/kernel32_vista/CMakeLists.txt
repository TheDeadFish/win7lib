
remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x600 -DWINVER=0x600)

spec2def(krnl32ex.dll krnl32ex.spec)
spec2def(krnl32ex.dll kernel32.spec)

list(APPEND SOURCE
    sync.c
    )
    

add_library(krnl32ex_obj OBJECT ${SOURCE})

add_library(krnl32ex MODULE $<TARGET_OBJECTS:krnl32ex_obj>    
    ${CMAKE_CURRENT_BINARY_DIR}/krnl32ex.def
    ${CMAKE_CURRENT_BINARY_DIR}/kernel32.def
    dllMain.c
)



target_link_libraries(krnl32ex libntdllex ntdll )
target_link_options(krnl32ex PRIVATE -nostartfiles -nodefaultlibs)
