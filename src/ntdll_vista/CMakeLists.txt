
remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x600 -DWINVER=0x600
    -D__NTDLL__
    -D_NTOSKRNL_
    -D_NTSYSTEM_)
    
spec2def(ntdllex.dll ntdllex.spec ADD_IMPORTLIB)

list(APPEND SOURCE
    condvar.c
    srw.c
    )
    
add_library(ntdllex_obj OBJECT ${SOURCE})

add_library(ntdllex MODULE $<TARGET_OBJECTS:ntdllex_obj>    
    ${CMAKE_CURRENT_BINARY_DIR}/ntdllex.def
    dllMain.c
)



target_link_libraries(ntdllex ntdll)
target_link_options(ntdllex PUBLIC -nostartfiles -nodefaultlibs)
