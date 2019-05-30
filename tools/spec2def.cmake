function(generate_import_lib _libname _dllname _spec_file)

    message(STATUS hello)

    # Generate the def for the import lib
    add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${_libname}_implib.def
        COMMAND spec2def -n=${_dllname} -a=${ARCH2} ${ARGN} --implib -d=${CMAKE_CURRENT_BINARY_DIR}/${_libname}_implib.def ${CMAKE_CURRENT_SOURCE_DIR}/${_spec_file}
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${_spec_file})
    set_source_files_properties(${CMAKE_CURRENT_BINARY_DIR}/${_libname}_implib.def PROPERTIES EXTERNAL_OBJECT TRUE)

    # Create normal importlib
    add_library(${_libname} STATIC  ${CMAKE_CURRENT_BINARY_DIR}/${_libname}_implib.def)
    set_target_properties(${_libname} PROPERTIES LINKER_LANGUAGE "IMPLIB" PREFIX "")

    # Create delayed importlib
    #add_library(${_libname}_delayed STATIC EXCLUDE_FROM_ALL ${CMAKE_CURRENT_BINARY_DIR}/${_libname}_implib.def)
   # set_target_properties(${_libname}_delayed PROPERTIES LINKER_LANGUAGE "IMPLIB_DELAYED" PREFIX "")
endfunction()

# Cute little hack to produce import libs
set(CMAKE_IMPLIB_CREATE_STATIC_LIBRARY "${CMAKE_DLLTOOL} --def <OBJECTS> --kill-at --output-lib=<TARGET>")
set(CMAKE_IMPLIB_DELAYED_CREATE_STATIC_LIBRARY "${CMAKE_DLLTOOL} --def <OBJECTS> --kill-at --output-delaylib=<TARGET>")
function(spec2def _dllname _spec_file)
    
    cmake_parse_arguments(__spec2def "ADD_IMPORTLIB;NO_PRIVATE_WARNINGS;WITH_RELAY" "VERSION" "" ${ARGN})

    # Get library basename
    get_filename_component(_file ${_spec_file} NAME_WE)

    # Error out on anything else than spec
    if(NOT ${_spec_file} MATCHES ".*\\.spec")
        message(FATAL_ERROR "spec2def only takes spec files as input.")
    endif()

    if (__spec2def_WITH_RELAY)
        set(__with_relay_arg "--with-tracing")
    endif()

    if(__spec2def_VERSION)
        set(__version_arg "--version=0x${__spec2def_VERSION}")
    endif()

    # Generate exports def and C stubs file for the DLL
    add_custom_command(
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${_file}.def ${CMAKE_CURRENT_BINARY_DIR}/${_file}_stubs.c
        COMMAND spec2def.exe -n=${_dllname} -a=${ARCH2} -d=${CMAKE_CURRENT_BINARY_DIR}/${_file}.def -s=${CMAKE_CURRENT_BINARY_DIR}/${_file}_stubs.c ${__with_relay_arg} ${__version_arg} ${CMAKE_CURRENT_SOURCE_DIR}/${_spec_file}
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${_spec_file})

    if(__spec2def_ADD_IMPORTLIB)
        set(_extraflags)
        if(__spec2def_NO_PRIVATE_WARNINGS)
            set(_extraflags --no-private-warnings)
        endif()
        
        generate_import_lib(lib${_file} ${_dllname} ${_spec_file} ${_extraflags})
    endif()
endfunction()
