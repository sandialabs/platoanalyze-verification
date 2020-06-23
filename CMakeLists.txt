# copy over the doxygen configuration for verification documentation
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tools/index.dox ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)

ADD_SUBDIRECTORY(LinearThermal)

ADD_CUSTOM_TARGET(VerificationDoc
  COMMAND ${CMAKE_COMMAND}
  -DDOXY_FILE=${CMAKE_CURRENT_SOURCE_DIR}/tools/verification.doxyfile
  -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/doc.cmake
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR} )
