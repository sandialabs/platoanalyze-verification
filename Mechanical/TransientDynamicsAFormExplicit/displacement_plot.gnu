set terminal png
set output "TransientDynamicsAForm_comparison.png"
set ylabel "Deflection (m)"
set xlabel "Position (m)"
plot 'displacement.data' u 1:2 w l lw 6 title "numerical", \
     'displacement.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "TransientDynamicsAForm_comparison.eps"
set ylabel "Deflection (m)"
set xlabel "Position (m)"
plot 'displacement.data' u 1:2 w l lw 6 title "numerical", \
     'displacement.data' u 1:3 w l lw 3 title "analytical"
