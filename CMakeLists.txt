# copy over the doxygen configuration for verification documentation
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tools/index.dox ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)

set(ImageDirs) ## this variable accumulates a list of directories that may have images for doxygen.

ADD_SUBDIRECTORY(Thermal/LinearThermal)
ADD_SUBDIRECTORY(Thermal/NonlinearThermal)
ADD_SUBDIRECTORY(Thermomechanics/StaticNonlinearBar)
ADD_SUBDIRECTORY(Thermomechanics/NonlinearBar)
ADD_SUBDIRECTORY(InherentStrain/2LayerNormal)
ADD_SUBDIRECTORY(InherentStrain/2LayerShear)

# modify the list of ImageDirs to be space delimited instead of semicolon delimited.
string(REPLACE ";" " " ImageDirs "${ImageDirs}")

# copy/modify verification.doxyfile to have a IMAGE_DIRS point to the list of test directories
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tools/verification.doxyfile ${CMAKE_CURRENT_BINARY_DIR})

if( DOXYGEN )
ADD_CUSTOM_TARGET(VerificationDoc
  COMMAND ${CMAKE_COMMAND}
  -DDOXY_FILE=${CMAKE_CURRENT_BINARY_DIR}/verification.doxyfile
  -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/doc.cmake
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR} )
else()
  message("'doxygen' was not found but is required to generate verification document.")
  message("'VerificationDoc' custom target not added.")
endif()
