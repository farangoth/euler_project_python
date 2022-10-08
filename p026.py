"""Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

import functions

d_max = 0
cycle_max = []

for d in range(1,1001):
    cycle = functions.euclide_division(1, d)
    if len(cycle)>len(cycle_max):
        d_max = d
        cycle_max = cycle

print("Sol26: d=", d_max, ", cycle=", cycle_max, ", length ", len(cycle_max) )

