list(APPEND OBJS
	${CMAKE_CURRENT_BINARY_DIR}/../ntdll_vista/ntdllex.def
	$<TARGET_OBJECTS:ntdllex_obj> -lntdll)

add_exm_file(ntdll.dll x64.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def
)
add_exm_file(ntdll.dll x86.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/x86.5.2.3790.3959.def
)
add_exm_file(ntdll.dll wow.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/wow.5.2.3790.3959.def
)

	
add_exm_target(ntdll)
