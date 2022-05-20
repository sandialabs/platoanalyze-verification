#  run verification problem
if (ANALYZE_EXECUTABLE)
  set( TEST_COMMAND "${ANALYZE_EXECUTABLE} --output-viz=${OUTPUT_DATA} --input-config=${CONFIG_FILE}" )
  execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
  if (HAD_ERROR)
    message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
  endif()
endif()

foreach( varName ${COMPARE_PY} )
  #  generate comparison
  set( TEST_COMMAND "python ${varName}_compare.py &> ${varName}.data" )
  execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
  if (HAD_ERROR)
    message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
  endif()

  if(DOXYGEN)
    # generate solution image if SOLUTION_PY defined
    message( "Generating image of problem solution.")
    set( TEST_COMMAND "pvbatch --use-offscreen-rendering ${varName}_display.py" )
    execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
    if (HAD_ERROR)
      message("FAILED: ${TEST_COMMAND}")
    endif()

    #  generate comparison plots
    set( TEST_COMMAND "gnuplot ${varName}_plot.gnu" )
    execute_process(COMMAND bash "-c" "${TEST_COMMAND}" RESULT_VARIABLE HAD_ERROR)
    if (HAD_ERROR)
      message(FATAL_ERROR "FAILED: ${TEST_COMMAND}")
    endif()
  endif()
endforeach()

#  check error norm
foreach( varName ${COMPARE_PY} )
execute_process(COMMAND bash "-c" "awk '/L2_error_norm_value/{print $2}' ${varName}.data | tail -1 > cmake_error_norm_value")
file(READ cmake_error_norm_value TEST_ERROR_NORM)
execute_process(COMMAND bash "-c" "awk '/L2_error_norm_tolerance/{print $2}' ${varName}.data | tail -1 > cmake_error_norm_tolerance")
file(READ cmake_error_norm_tolerance ERROR_TOLERANCE)
if( ${TEST_ERROR_NORM} GREATER ${ERROR_TOLERANCE} )
  message("Error norm: ${TEST_ERROR_NORM}")
  message("Error tolerance: ${ERROR_TOLERANCE}")
  message(FATAL_ERROR "Error norm is great than tolerance.")
else()
  message(STATUS "Error norm: ${TEST_ERROR_NORM}-- Error tolerance: ${ERROR_TOLERANCE}")
endif()
endforeach()

