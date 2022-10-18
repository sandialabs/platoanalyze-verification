macro(add_verification_test CONFIG_FILE OUTPUT_DATA COMPARE_VAR_NAMES ADDITIONAL_TEST_FILES)
    # Parameters:
    # CONFIG_FILE: Configuration file name for platoanalyze
    # OUTPUT_DATA: Output directory name for platoanalyze
    # COMPARE_VAR_NAMES: The name(s) of the output variable(s) for comparison (displacement, e.g.)
    # ADDITIONAL_TEST_FILES: A list of supporting files, which will be copied to the test directory

    # OBLIGATORY: Doxygen will not find images in this directory if the next line is not included
    set(ImageDirs ${ImageDirs} ${CMAKE_CURRENT_BINARY_DIR} PARENT_SCOPE)

    # copy files from current source dir to binary dir

    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${CONFIG_FILE} ${CMAKE_CURRENT_BINARY_DIR}/${CONFIG_FILE} COPYONLY)
    foreach(compare_name ${COMPARE_VAR_NAMES})
        configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${compare_name}_compare.py ${CMAKE_CURRENT_BINARY_DIR}/${compare_name}_compare.py COPYONLY)
        if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/${compare_name}_display.py)
            configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${compare_name}_display.py ${CMAKE_CURRENT_BINARY_DIR}/${compare_name}_display.py COPYONLY)
        endif()
    endforeach(compare_name)
    foreach( test_file ${ADDITIONAL_TEST_FILES} )
        configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${test_file} ${CMAKE_CURRENT_BINARY_DIR}/${testFile} COPYONLY)
    endforeach(test_file)

    # copy some verification test utility files
    configure_file(${CMAKE_SOURCE_DIR}/tests/verification/tools/verification_utils.py ${CMAKE_CURRENT_BINARY_DIR}/verification_utils.py COPYONLY)

    if(NOT PLATOANALYZE_ENABLE_ENGINEMESH)
        # Replace with vtk versions
        foreach(compare_name ${COMPARE_VAR_NAMES})
            configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${compare_name}_compare_vtk.py ${CMAKE_CURRENT_BINARY_DIR}/${compare_name}_compare.py COPYONLY)
            configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${compare_name}_display_vtk.py ${CMAKE_CURRENT_BINARY_DIR}/${compare_name}_display.py COPYONLY)
        endforeach(compare_name)
        configure_file(${CMAKE_SOURCE_DIR}/tests/verification/tools/line_vtk.py ${CMAKE_CURRENT_BINARY_DIR}/line.py COPYONLY)
    endif()

    get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
    set( TEST_NAME ${testDirName} )

    ## create test
    add_test( NAME ${TEST_NAME}
          COMMAND ${CMAKE_COMMAND}
          -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
          -DCONFIG_FILE=${CONFIG_FILE}
          -DOUTPUT_DATA=${OUTPUT_DATA}
          "-DCOMPARE_PY=${COMPARE_VAR_NAMES}"
          -DDOXYGEN=${DOXYGEN}
          -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/verify.cmake )
endmacro()
