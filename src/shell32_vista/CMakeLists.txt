
remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x600 -DWINVER=0x600)

spec2def(iphlpaex.dll shell32.spec)

list(APPEND SOURCE
    stockIcon.cc
		shell32.cc
    )
    

add_library(shell32_obj OBJECT ${SOURCE})

add_library(shel32ex MODULE $<TARGET_OBJECTS:shell32_obj>    
    ${CMAKE_CURRENT_BINARY_DIR}/shell32.def
		dllMain.c internal.cc
)



target_link_libraries(shel32ex shell32 shlwapi comctl32)
target_link_options(shel32ex PRIVATE -nostartfiles)
