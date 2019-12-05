remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x601 -DWINVER=0x601
    -D__NTDLL__ -D_NTOSKRNL_ -D_NTSYSTEM_)
		
		
add_library(ntdllexO OBJECT 	
	condvar.c srw.c rtl.c
)		


add_library(ntdllex STATIC $<TARGET_OBJECTS:ntdllexO>)
add_library(ntdllexSo SHARED $<TARGET_OBJECTS:ntdllexO> dllMain.c)
target_link_libraries(ntdllexSo ntdll)
target_link_options(ntdllexSo PRIVATE -nostartfiles)
