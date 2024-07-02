set terminal png
set output "Thermomechanics_NonlinearBar_displacement_comparison.png"
set ylabel "Axial Displacement (m)"
set xlabel "Position (m)"
plot 'displacement.data' u 1:2 w l lw 6 title "numerical", \
     'displacement.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "Thermomechanics_NonlinearBar_displacement_comparison.eps"
set ylabel "Axial Displacement (m)"
set xlabel "Position (m)"
plot 'displacement.data' u 1:2 w l lw 6 title "numerical", \
     'displacement.data' u 1:3 w l lw 3 title "analytical"
