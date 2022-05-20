# copy files from current source dir to binary dir
set( testFiles "cylinder.exo;cylinder_shifted.exo;analyzeOperations.xml;analyzeInputMass.xml;analyzeInputIxx.xml;analyzeInputIyy.xml;analyzeInputIzz.xml;analyzeInputIxy.xml;analyzeInputIxz.xml;analyzeInputIyz.xml;analyzeInputCGx.xml;analyzeInputCGy.xml;analyzeInputCGz.xml;massProperties_compare.py" )

foreach( testFile ${testFiles} )
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${testFile} ${CMAKE_CURRENT_BINARY_DIR}/${testFile} COPYONLY)
endforeach(testFile)

# Setup test
set( COMPARE_PY  "massProperties" )  ## variable(s) to verify

get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
set( TEST_NAME ${testDirName} )

## create test
add_test( NAME ${TEST_NAME}
          COMMAND ${CMAKE_COMMAND}
          -DCOMPARE_PY=${COMPARE_PY}
          -DDOXYGEN=0
          -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/verify.cmake )
