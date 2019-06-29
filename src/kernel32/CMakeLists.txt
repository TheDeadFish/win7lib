spec2def(kernel32.dll ../kernel32_vista/krnl32ex.spec)

list(APPEND OBJS
	${CMAKE_CURRENT_BINARY_DIR}/krnl32ex.def
	$<TARGET_FILE:krnl32ex> -lntdll)

add_exm_file(x64.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def)
add_exm_file(x86.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/x86.5.2.3790.3959.def)
add_exm_file(wow.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/wow.5.2.3790.3959.def)
	
add_exm_target(kernel32.dll)
