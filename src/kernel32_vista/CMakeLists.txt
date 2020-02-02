
remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x601 -DWINVER=0x601
	-D_KERNEL32_)

spec2def(krnl32ex.dll krnl32ex.spec)
spec2def(krnl32ex.dll kernel32.spec)

add_library(krnl32exO OBJECT
	sync.c
	datetime.c
	locale.c
	${CMAKE_CURRENT_BINARY_DIR}/locale_table.c  
	stubs.c
	finalpath.c
	symlink.c
	setfileinfo.c	
	process.c
	ioex.c
	log.c fileops.c
)


add_library(krnl32exS STATIC $<TARGET_OBJECTS:krnl32exO>)
add_library(krnl32ex SHARED  $<TARGET_OBJECTS:krnl32exO> dllMain.c
	${CMAKE_CURRENT_BINARY_DIR}/krnl32ex.def
	${CMAKE_CURRENT_BINARY_DIR}/kernel32.def )
	
	
	
	
target_link_libraries(krnl32ex ntdllex ntdll)
target_link_options(krnl32ex PRIVATE -nostartfiles)

# create locale_table.c
add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/locale_table.c
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/locale.py
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/locale.py 
)
