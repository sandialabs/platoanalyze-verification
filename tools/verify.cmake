#  run verification problem
set( TEST_COMMAND "${ANALYZE_EXECUTABLE} --output-viz=${OUTPUT_DIR} --input-config=${CONFIG_FILE}" )
execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
if (HAD_ERROR)
  message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
endif()


#  generate comparison
set( TEST_COMMAND "python ${COMPARE_PY} &> plot.data" )
execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
if (HAD_ERROR)
  message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
endif()

# generate solution image if SOLUTION_PY defined
if( SOLUTION_PY )
  message( "Generating image of problem solution.")
  set( TEST_COMMAND "pvbatch --use-offscreen-rendering ${SOLUTION_PY}" )
  execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
  if (HAD_ERROR)
    message("FAILED: ${TEST_COMMAND}")
  endif()
endif()

#  check error norm
execute_process(COMMAND bash "-c" "awk '/L2_norm_of_error/{print $2}' plot.data | tail -1 > cmake_error_norm_result")
file(READ cmake_error_norm_result TEST_ERROR_NORM)
message(STATUS "ERROR_NORM: ${TEST_ERROR_NORM}")
if( ${TEST_ERROR_NORM} GREATER ${ERROR_TOLERANCE} )
  message("Error norm: ${TEST_ERROR_NORM}")
  message("Error tolerance: ${ERROR_TOLERANCE}")
  message(FATAL_ERROR "Error norm is great than tolerance.")
else()
  message(STATUS "Error norm: ${TEST_ERROR_NORM}-- Error tolerance: ${ERROR_TOLERANCE}")
endif()


#  generate comparison plots
set( TEST_COMMAND "gnuplot ${PLOT_GNU}" )
execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
if (HAD_ERROR)
  message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
endif()
