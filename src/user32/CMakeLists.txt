spec2def(user32.dll user32ex.spec)

list(APPEND OBJS
	${CMAKE_CURRENT_BINARY_DIR}/user32ex.def
	$<TARGET_FILE:user32ex> -lntdll)

add_exm_file(x64.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def)
add_exm_file(x86.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/x86.5.2.3790.3959.def)
add_exm_file(wow.5.2.3790.3959 ${OBJS}
	${CMAKE_CURRENT_SOURCE_DIR}/wow.5.2.3790.3959.def)
	
add_exm_target(user32.dll)
