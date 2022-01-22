set terminal png
set output "MPCs_TensileBar_comparison.png"
set ylabel "X Displacement (m)"
set xlabel "Position (m)"
plot 'displacement.data' u 1:2 w l lw 6 title "numerical", \
     'displacement.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "MPCs_TensileBar_comparison.eps"
set ylabel "X Displacement (m)"
set xlabel "Position (m)"
plot 'displacement.data' u 1:2 w l lw 6 title "numerical", \
     'displacement.data' u 1:3 w l lw 3 title "analytical"
