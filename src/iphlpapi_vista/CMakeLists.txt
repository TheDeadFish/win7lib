
remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x600 -DWINVER=0x600)

spec2def(iphlpaex.dll iphlpapi.spec)
spec2def(iphlpaex.dll iphlpapi2.spec)

list(APPEND SOURCE
    iphlpapi_main.c
    )
    

add_library(iphlpapi_obj OBJECT ${SOURCE})

add_library(iphlpaex MODULE $<TARGET_OBJECTS:iphlpapi_obj>    
    ${CMAKE_CURRENT_BINARY_DIR}/iphlpapi.def
    ${CMAKE_CURRENT_BINARY_DIR}/iphlpapi2.def
    dllMain.c
)



target_link_libraries(iphlpaex iphlpapi)
target_link_options(iphlpaex PRIVATE -nostartfiles)
