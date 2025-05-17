add_verification_test("two_block_tensile.xml" "output_data" "displacement" "amgx.json;two_block_tensile.exo;displacement_plot.gnu;Assemblies_CompliantContact_layout.png;index.dox" )
# This runs out of memory on the gpu pipeline, so only run on cpu
set_property(TEST CompliantContact PROPERTY LABELS "CPU_only")
