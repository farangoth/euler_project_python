"""Problem 35:
How many circular primes are there below one million?"""

import functions as fct

rangemax = 1000000

print("Sol35: ", len(fct.get_circular_primes(rangemax)))
