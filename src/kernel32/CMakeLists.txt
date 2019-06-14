

list(APPEND DEFS
	${CMAKE_CURRENT_BINARY_DIR}/../kernel32_vista/krnl32ex.def)

add_exm_file(kernel32 x64.5.2.3790.3959
	${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def 
	$<TARGET_OBJECTS:krnl32ex_obj> ${DEFS})
add_exm_file(kernel32 x86.5.2.3790.3959
	${CMAKE_CURRENT_SOURCE_DIR}/x86.5.2.3790.3959.def 
	$<TARGET_OBJECTS:krnl32ex_obj> ${DEFS})
add_exm_file(kernel32 wow.5.2.3790.3959
	${CMAKE_CURRENT_SOURCE_DIR}/wow.5.2.3790.3959.def 
	$<TARGET_OBJECTS:krnl32ex_obj> ${DEFS})
	
add_exm_target(kernel32)
