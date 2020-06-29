# OBLIGATORY: Doxygen will not find images in this directory if the next line is not included
set(ImageDirs ${ImageDirs} ${CMAKE_CURRENT_BINARY_DIR} PARENT_SCOPE)

# copy files from current source dir to binary dir
set( testFiles "1dbar.xml;amgx.json;1dbar.exo;plot.gnu;compare.py;solution.py;Thermomechanics_NonlinearBar_layout.png;index.dox" )

foreach( testFile ${testFiles} )
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${testFile} ${CMAKE_CURRENT_BINARY_DIR}/${testFile} COPYONLY)
endforeach(testFile)

# copy some verification test utility files
configure_file(  ${CMAKE_SOURCE_DIR}/tests/verification/tools/line.py ${CMAKE_CURRENT_BINARY_DIR}/line.py COPYONLY)

set( CONFIG_FILE "1dbar.xml"   )  ## Plato Analyze input file
set( OUTPUT_DIR  "output_data" )  ## Plato Analyze output directory
set( COMPARE_PY  "compare.py"  )  ## verification script
set( SOLUTION_PY "solution.py" )  ## paraview script for generating image of solution
set( PLOT_GNU    "plot.gnu"    )  ## gnuplot plotting commands

## Note: this test computes the thermal history from initial conditions to thermal 
#        equilibration then compares against a steady-state solution.  Consequently,
#        the agreement won't be as good as say a steady-state simulation.
set( ERROR_TOLERANCE 1e2 )

get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
set( TEST_NAME ${testDirName} )

## create test
add_test( NAME ${TEST_NAME}
          COMMAND ${CMAKE_COMMAND}
          -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
          -DCONFIG_FILE=${CONFIG_FILE}
          -DOUTPUT_DIR=${OUTPUT_DIR}
          -DCOMPARE_PY=${COMPARE_PY}
          -DSOLUTION_PY=${SOLUTION_PY}
          -DERROR_TOLERANCE=${ERROR_TOLERANCE}
          -DPLOT_GNU=${PLOT_GNU}
          -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/verify.cmake )
