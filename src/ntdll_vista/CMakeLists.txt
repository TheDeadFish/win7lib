remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x600 -DWINVER=0x600
    -D__NTDLL__ -D_NTOSKRNL_ -D_NTSYSTEM_)
add_library(ntdllex STATIC 	
	condvar.c srw.c
)
