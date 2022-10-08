"""What is the largest n-digit pandigital prime that exists?"""

import functions

primes = functions.get_primes_with_sieve(10**9)
print(primes)

primes_pandigitals = [prime for prime in primes if any(functions.is_pandigital(prime, p) for p in range(2,10))]
print(primes_pandigitals)

print("Sol41: ", primes_pandigitals[-1])