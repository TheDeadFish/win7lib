remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x601 -DWINVER=0x601
    -D__NTDLL__ -D_NTOSKRNL_ -D_NTSYSTEM_ -D_KERNEL32_)
		
	
spec2def(ntdllex.dll ntdllex.spec)
spec2def(ntdll.dll ntdll.spec)

	
add_library(ntdllexO OBJECT 	
	condvar.c srw.c rtl.c time.c
)		


add_library(ntdllexS STATIC $<TARGET_OBJECTS:ntdllexO>)
add_library(ntdllex SHARED $<TARGET_OBJECTS:ntdllexO> 
	dllMain.c ../include/hotpatch.cc
	${CMAKE_CURRENT_BINARY_DIR}/ntdllex.def
	${CMAKE_CURRENT_BINARY_DIR}/ntdll.def 
	
	)

target_link_libraries(ntdllex ntdll ntdllcrt)
target_link_options(ntdllex PRIVATE -nostartfiles)
