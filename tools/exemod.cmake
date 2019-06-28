set (EXM_DIR ${CMAKE_SOURCE_DIR}/bin/exm)

if(ARCH STREQUAL "amd64")
	set (ARCH32 "")
else()	
	set (ARCH32 "32")
endif()

function (add_exm_file arch)
	if(arch MATCHES "^x64")
		if(NOT ARCH STREQUAL "amd64")
			return()
		endif()
	else()
		if(ARCH STREQUAL "amd64")
			return()
		endif()
	endif()

	if (exm_cmd)
		set(PLUS "+")
	endif()
	
	set (deps ${ARGN})
	list(FILTER deps EXCLUDE REGEX ^-)
	set(exm_cmd ${exm_cmd} DEPENDS ${deps} COMMAND 
		exe_mod ${PLUS}EXM_FILE:${arch} ${ARGN} PARENT_SCOPE)

endfunction()

function (add_exm_target name)
	if(NOT exm_cmd)
		return()
	endif()

	set (grp ${ARGN})
	if (NOT grp)
		set(grp "extxp")
	endif()
	
	set (exm_file "${EXM_DIR}/${name},${grp}${ARCH32}.exm")
	string(REPLACE "EXM_FILE" ${exm_file} exm_cmd "${exm_cmd}")
	add_custom_command(OUTPUT ${exm_file}
		${exm_cmd} COMMAND_EXPAND_LISTS)
	
	string(REPLACE "," "_" target "${name},${grp}")
	add_custom_target(${target} ALL DEPENDS ${exm_file})
	set(exm_cmd "" PARENT_SCOPE)
	
endfunction()
