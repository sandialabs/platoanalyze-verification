# run doxygen
set( TEST_COMMAND "doxygen ${DOXY_FILE}" )
execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
if (HAD_ERROR)
  message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
endif()

# build pdf
set( TEST_COMMAND "cd latex; make; cp refman.pdf ../verification.pdf; cd .." )
execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
if (HAD_ERROR)
  message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
endif()
