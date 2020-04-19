macro(def_test_dir name)
	set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${BIN_DIR}/tests/${name})
	add_subdirectory(${name})
endmacro()


remove_definitions(-D_WIN32_WINNT=0x502 -DWINVER=0x502)
add_definitions(-D_WIN32_WINNT=0x601 -DWINVER=0x601
	-D_KERNEL32_)

def_test_dir(kernel32_vista)
