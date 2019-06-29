spec2def(ntdll.dll ../ntdll_vista/ntdllex.spec)

list(APPEND OBJS
	${CMAKE_CURRENT_BINARY_DIR}/ntdllex.def
	$<TARGET_FILE:ntdllex> -lntdll)

add_exm_file(x64.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def
)
add_exm_file(x86.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/x86.5.2.3790.3959.def
)
add_exm_file(wow.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/wow.5.2.3790.3959.def
)

	
add_exm_target(ntdll.dll)




# redirection only stuff
add_library(ntdll_redir OBJECT redirect.c)
set(REDIR_OBJS
	${CMAKE_CURRENT_SOURCE_DIR}/redirect.def
	$<TARGET_OBJECTS:ntdll_redir> -lntdll)
	
#add_exm_file(ntdll.dll x64.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def
#)
#add_exm_file(ntdll.dll x86.5.2.3790.3959 ${OBJS}
	#${CMAKE_CURRENT_SOURCE_DIR}/x86.5.2.3790.3959.def
#)
add_exm_file(wow.5.2.3790.3959 
	${CMAKE_CURRENT_SOURCE_DIR}/wow.5.2.3790.3959.def
	${REDIR_OBJS}
)

add_exm_target(ntdll.dll redir)
