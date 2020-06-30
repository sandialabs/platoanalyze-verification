# OBLIGATORY: Doxygen will not find images in this directory if the next line is not included
set(ImageDirs ${ImageDirs} ${CMAKE_CURRENT_BINARY_DIR} PARENT_SCOPE)

# copy files from current source dir to binary dir
set( testFiles "block.xml;amgx.json;block.exo;temperature_plot.gnu;temperature_compare.py;temperature_display.py;NonlinearThermal_layout.png;index.dox" )

foreach( testFile ${testFiles} )
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${testFile} ${CMAKE_CURRENT_BINARY_DIR}/${testFile} COPYONLY)
endforeach(testFile)

# copy some verification test utility files
configure_file(  ${CMAKE_SOURCE_DIR}/tests/verification/tools/line.py ${CMAKE_CURRENT_BINARY_DIR}/line.py COPYONLY)

set( CONFIG_FILE "block.xml"   )  ## Plato Analyze input file
set( OUTPUT_DIR  "output_data" )  ## Plato Analyze output directory
set( COMPARE_PY  "temperature" )  ## variable(s) to verify

get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
set( TEST_NAME ${testDirName} )

## create test
add_test( NAME ${TEST_NAME}
          COMMAND ${CMAKE_COMMAND}
          -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
          -DCONFIG_FILE=${CONFIG_FILE}
          -DOUTPUT_DIR=${OUTPUT_DIR}
          -DCOMPARE_PY=${COMPARE_PY}
          -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/verify.cmake )
