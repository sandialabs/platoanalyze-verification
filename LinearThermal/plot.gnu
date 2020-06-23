set terminal png
set output "comparison.png"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
plot 'plot.data' u 1:2 w l lw 6 title "numerical", \
     'plot.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "comparison.eps"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
plot 'plot.data' u 1:2 w l lw 6 title "numerical", \
     'plot.data' u 1:3 w l lw 3 title "analytical"
