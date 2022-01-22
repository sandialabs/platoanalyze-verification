# OBLIGATORY: Doxygen will not find images in this directory if the next line is not included
set(ImageDirs ${ImageDirs} ${CMAKE_CURRENT_BINARY_DIR} PARENT_SCOPE)

# copy files from current source dir to binary dir
set( testFiles "bilayer.xml;amgx.json;bilayer.exo;dispz_plot.gnu;dispz_compare.py;dispz_display.py;index.dox" )

foreach( testFile ${testFiles} )
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${testFile} ${CMAKE_CURRENT_BINARY_DIR}/${testFile} COPYONLY)
endforeach(testFile)

# copy some verification test utility files
configure_file(  ${CMAKE_SOURCE_DIR}/tests/verification/tools/line.py ${CMAKE_CURRENT_BINARY_DIR}/line.py COPYONLY)

if(NOT PLATOANALYZE_ENABLE_ENGINEMESH)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/dispz_compare_vtk.py ${CMAKE_CURRENT_BINARY_DIR}/dispz_compare.py COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/dispz_display_vtk.py ${CMAKE_CURRENT_BINARY_DIR}/dispz_display.py COPYONLY)
    configure_file(  ${CMAKE_SOURCE_DIR}/tests/verification/tools/line_vtk.py ${CMAKE_CURRENT_BINARY_DIR}/line.py COPYONLY)
endif()

set( CONFIG_FILE "bilayer.xml" )  ## Plato Analyze input file
set( OUTPUT_DATA  "output_data" )  ## Plato Analyze output directory
set( COMPARE_PY  "dispz"       )  ## variable(s) to verify

get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
set( TEST_NAME ${testDirName} )

## create test
add_test( NAME ${TEST_NAME}
          COMMAND ${CMAKE_COMMAND}
          -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
          -DCONFIG_FILE=${CONFIG_FILE}
          -DOUTPUT_DATA=${OUTPUT_DATA}
          -DCOMPARE_PY=${COMPARE_PY}
          -DDOXYGEN=${DOXYGEN}
          -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/verify.cmake )
