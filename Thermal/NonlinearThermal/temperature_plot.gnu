set terminal png
set output "NonlinearThermal_comparison.png"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
plot 'temperature.data' u 1:2 w l lw 6 title "numerical", \
     'temperature.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "NonlinearThermal_comparison.eps"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
plot 'temperature.data' u 1:2 w l lw 6 title "numerical", \
     'temperature.data' u 1:3 w l lw 3 title "analytical"