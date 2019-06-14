add_library(wow64_obj OBJECT hook.c)
add_exm_file(wow64 x64.5.2.3790.3959
	${CMAKE_CURRENT_SOURCE_DIR}/x64.5.2.3790.3959.def 
	$<TARGET_OBJECTS:wow64_obj>)
add_exm_target(wow64)
