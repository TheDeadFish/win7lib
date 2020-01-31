remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x601 -DWINVER=0x601
	-D_SHELL32_)
add_library(shell32ex STATIC internal.cc
	stockIcon.cc shell32.cc stubs.c
)

spec2def(shellex.dll ../shell32/shell32ex.spec)
add_library(shellex MODULE	shell32.def dllMain.c
	${CMAKE_CURRENT_BINARY_DIR}/shell32ex.def	)
	
target_link_libraries(shellex shell32ex -lshell32 -lshlwapi -lcomctl32)	
target_link_options(shellex PRIVATE -nostartfiles)
