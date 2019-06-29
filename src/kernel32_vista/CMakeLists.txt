
remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x600 -DWINVER=0x600
	-D_KERNEL32_)

spec2def(krnl32ex.dll krnl32ex.spec)

add_library(krnl32ex STATIC
	sync.c
	datetime.c
	locale.c
	${CMAKE_CURRENT_BINARY_DIR}/locale_table.c  
	stubs.c
	finalpath.c
	symlink.c
	setfileinfo.c	
)

# create locale_table.c
add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/locale_table.c
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/locale.py
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/locale.py 
)
