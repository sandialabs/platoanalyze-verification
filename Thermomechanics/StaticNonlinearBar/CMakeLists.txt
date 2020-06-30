# OBLIGATORY: Doxygen will not find images in this directory if the next line is not included
set(ImageDirs ${ImageDirs} ${CMAKE_CURRENT_BINARY_DIR} PARENT_SCOPE)

# copy files from current source dir to binary dir
set( testFiles "1dbar.xml;amgx.json;1dbar.exo" )
set( testFiles "${testFiles};Thermomechanics_StaticNonlinearBar_layout.png;index.dox" )
set( testFiles "${testFiles};temperature_plot.gnu;temperature_compare.py;temperature_display.py" )
set( testFiles "${testFiles};displacement_plot.gnu;displacement_compare.py;displacement_display.py" )

foreach( testFile ${testFiles} )
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${testFile} ${CMAKE_CURRENT_BINARY_DIR}/${testFile} COPYONLY)
endforeach(testFile)

# copy some verification test utility files
configure_file(  ${CMAKE_SOURCE_DIR}/tests/verification/tools/line.py ${CMAKE_CURRENT_BINARY_DIR}/line.py COPYONLY)

set( CONFIG_FILE "1dbar.xml"   )  ## Plato Analyze input file
set( OUTPUT_DIR  "output_data" )  ## Plato Analyze output directory

set( COMPARE_PY  "temperature;displacement"  )  ## verification script

get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
set( TEST_NAME ${testDirName} )

## create test
add_test( NAME ${TEST_NAME}
          COMMAND ${CMAKE_COMMAND}
          -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
          -DCONFIG_FILE=${CONFIG_FILE}
          -DOUTPUT_DIR=${OUTPUT_DIR}
          "-DCOMPARE_PY=${COMPARE_PY}"
          -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/verify.cmake )
