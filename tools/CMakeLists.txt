
function(add_host_tool _tool)
    add_executable(${_tool} ${ARGN})
		add_executable(native-${_tool} ALIAS ${_tool})
endfunction()

add_host_tool(spec2def spec2def.c)
