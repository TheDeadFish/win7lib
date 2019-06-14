set (EXM_DIR ${CMAKE_SOURCE_DIR}/bin/exm)

if(ARCH STREQUAL "amd64")
	set (ARCH32 "")
else()	
	set (ARCH32 "32")
endif()

function (add_exm_file name arch)
	set (exm_file "${EXM_DIR}/${name}-kex${ARCH32}`${arch}.exm")
	add_custom_command( OUTPUT ${exm_file}
		COMMAND exe_mod ${exm_file} ${ARGN}
		DEPENDS ${ARGN} )
	set(exm_deps ${exm_deps} ${exm_file} PARENT_SCOPE)
endfunction()

function (add_exm_target name)
	message(STATUS ${exm_deps})
	add_custom_target(exm_${name} ALL DEPENDS ${exm_deps})
endfunction()
