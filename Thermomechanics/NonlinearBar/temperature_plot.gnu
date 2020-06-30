set terminal png
set output "Thermomechanics_NonlinearBar_temperature_comparison.png"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
plot 'temperature.data' u 1:2 w l lw 6 title "numerical", \
     'temperature.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "Thermomechanics_NonlinearBar_temperature_comparison.eps"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
plot 'temperature.data' u 1:2 w l lw 6 title "numerical", \
     'temperature.data' u 1:3 w l lw 3 title "analytical"
