set terminal png
set output "4LayerNormal_comparison.png"
set ylabel "Total Displacement (m)"
set xlabel "Position (m)"
plot 'dispz.data' u 1:2 w l lw 6 title "numerical", \
     'dispz.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "4LayerNormal_comparison.eps"
set ylabel "Total Displacement (m)"
set xlabel "Position (m)"
plot 'dispz.data' u 1:2 w l lw 6 title "numerical", \
     'dispz.data' u 1:3 w l lw 3 title "analytical"
