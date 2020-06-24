# copy over the doxygen configuration for verification documentation
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tools/index.dox ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)

set(ImageDirs) ## this variable accumulates a list of directories that may have images for doxygen.

ADD_SUBDIRECTORY(LinearThermal)
ADD_SUBDIRECTORY(NonlinearThermal)

# modify the list of ImageDirs to be space delimited instead of semicolon delimited.
string(REPLACE ";" " " ImageDirs "${ImageDirs}")

# copy/modify verification.doxyfile to have a IMAGE_DIRS point to the list of test directories
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tools/verification.doxyfile ${CMAKE_CURRENT_BINARY_DIR})

ADD_CUSTOM_TARGET(VerificationDoc
  COMMAND ${CMAKE_COMMAND}
  -DDOXY_FILE=${CMAKE_CURRENT_BINARY_DIR}/verification.doxyfile
  -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/doc.cmake
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR} )
