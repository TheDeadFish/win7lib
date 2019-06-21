set (EXM_DIR ${CMAKE_SOURCE_DIR}/bin/exm)

if(ARCH STREQUAL "amd64")
	set (ARCH32 "")
else()	
	set (ARCH32 "32")
endif()

function (add_exm_file name arch)
	if(arch MATCHES "^x64")
		if(NOT ARCH STREQUAL "amd64")
			return()
		endif()
	else()
		if(ARCH STREQUAL "amd64")
			return()
		endif()
	endif()

	set (exm_file "${EXM_DIR}/${name},extxp${ARCH32}.exm")
	if (NOT exm_cmd)
		set(exm_out ${exm_file} PARENT_SCOPE)
	else()
		set(exm_file "+${exm_file}")
	endif()
	
	set (deps ${ARGN})
	list(FILTER deps EXCLUDE REGEX ^-)
	set(exm_cmd ${exm_cmd} DEPENDS ${deps} COMMAND 
		exe_mod ${exm_file}:${arch} ${ARGN} PARENT_SCOPE)

endfunction()

function (add_exm_target name)
	add_custom_command(OUTPUT ${exm_out}
		${exm_cmd} COMMAND_EXPAND_LISTS)
	add_custom_target(exm_${name} ALL DEPENDS ${exm_out})	
endfunction()
