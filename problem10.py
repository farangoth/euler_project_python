"""Find the sum of all the primes below two million."""

import functions

rangemax = 2000000
primes = functions.list_primes_crible(rangemax)
sum_primes = 0

for prime in primes:
    sum_primes += prime

print("Sol10 :", sum_primes)
