remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x601 -DWINVER=0x601
	-D_SHELL32_)
add_library(shell32ex STATIC
	stockIcon.cc shell32.cc
)
