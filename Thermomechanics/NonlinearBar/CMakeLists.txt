set(testFiles "amgx.json;1dbar.exo")
set(testFiles "${testFiles};Thermomechanics_NonlinearBar_layout.png;index.dox")
set(testFiles "${testFiles};temperature_plot.gnu;displacement_plot.gnu")

add_verification_test("1dbar.xml" "output_data" "temperature;displacement" ${testFiles})
