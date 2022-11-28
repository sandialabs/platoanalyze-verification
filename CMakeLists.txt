# copy over the doxygen configuration for verification documentation
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tools/index.dox ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)

set(ImageDirs) ## this variable accumulates a list of directories that may have images for doxygen.

INCLUDE(AddVerificationTest.cmake) # Helper macro for tests

# these need to be here because the behavior of the 'verify' macro
# depends on the PARAVIEW and GNUPLOT variables
FIND_PROGRAM( PARAVIEW NAMES paraview )
FIND_PROGRAM( GNUPLOT  NAMES gnuplot  )

if(ELLIPTIC)
ADD_SUBDIRECTORY(Mechanical/BodyLoads_Tet4)
ADD_SUBDIRECTORY(Mechanical/BodyLoads_Tet10)
if(HEX_ELEMENTS)
  ADD_SUBDIRECTORY(Mechanical/BodyLoads_Hex8)
  ADD_SUBDIRECTORY(Mechanical/BodyLoads_Hex27)
endif()
ADD_SUBDIRECTORY(Assemblies/MPCs)
ADD_SUBDIRECTORY(Assemblies/CompliantContact)
ADD_SUBDIRECTORY(Thermal/NonlinearThermal)
ADD_SUBDIRECTORY(Thermal/LinearThermal)
ADD_SUBDIRECTORY(Thermomechanics/StaticNonlinearBar)
endif()

if(HYPERBOLIC)
ADD_SUBDIRECTORY(Mechanical/TransientDynamicsImp)
ADD_SUBDIRECTORY(Mechanical/TransientDynamicsAForm)
ADD_SUBDIRECTORY(Mechanical/TransientDynamicsAFormExplicit)
endif()

if(PARABOLIC)
ADD_SUBDIRECTORY(Thermomechanics/NonlinearBar)
endif()

if(HATCHING)
ADD_SUBDIRECTORY(InherentStrain/2LayerNormal)
ADD_SUBDIRECTORY(InherentStrain/4LayerNormal)
ADD_SUBDIRECTORY(InherentStrain/2LayerShear)
endif()

IF( PLATOANALYZE_ENABLE_PYTHON )
  ADD_SUBDIRECTORY(Mechanical/MassProperties)
ENDIF()


FIND_PROGRAM( DOXYGEN  NAMES doxygen  )
if( DOXYGEN AND PARAVIEW AND GNUPLOT)
  # modify the list of ImageDirs to be space delimited instead of semicolon delimited.
  string(REPLACE ";" " " ImageDirs "${ImageDirs}")

  # copy/modify verification.doxyfile to have a IMAGE_DIRS point to the list of test directories
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/tools/verification.doxyfile ${CMAKE_CURRENT_BINARY_DIR})

  ADD_CUSTOM_TARGET(VerificationDoc
    COMMAND ${CMAKE_COMMAND}
    -DDOXY_FILE=${CMAKE_CURRENT_BINARY_DIR}/verification.doxyfile
    -P ${CMAKE_SOURCE_DIR}/tests/verification/tools/doc.cmake
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR} )

else()
  message("doxygen, paraview, and gnuplot are required to generate verification document.")
  message("'VerificationDoc' custom target not added.")
endif()
