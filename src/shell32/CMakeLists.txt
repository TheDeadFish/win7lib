spec2def(shell32.dll shell32ex.spec)

list(APPEND OBJS
	${CMAKE_CURRENT_BINARY_DIR}/shell32ex.def
	$<TARGET_FILE:shell32ex> -lshell32 -lshlwapi)

add_exm_file(x64.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def)
add_exm_file(x86.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/x86.5.2.3790.3959.def)
	
add_exm_target(shell32.dll)
