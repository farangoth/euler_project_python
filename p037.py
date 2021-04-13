"""Find the sum of the only eleven primes that are both truncatable from
left to right and right to left."""

import functions as fct

rangemax = 1000000

primes = fct.get_primes_with_sieve(rangemax)
print("Primes generated")
truncatable_primes = primes.copy()
truncatable_primes.remove(2)
truncatable_primes.remove(3)
truncatable_primes.remove(5)
truncatable_primes.remove(7)
while (len(truncatable_primes) > 11):
    for prime in primes:
        for n in range(1, len(str(prime))):
            if (not (int(str(prime)[:-n]) in primes)
                    or not (int(str(prime)[n:]) in primes)):
                if prime in truncatable_primes:
                    truncatable_primes.remove(prime)
                break

print(truncatable_primes)
print("Sol37: ", sum(truncatable_primes))
