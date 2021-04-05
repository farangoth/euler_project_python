import functions

rangemax = 1000
max_primes_sequences = 0
a_max = 0
b_max = 0
primes_sequence = 0
n = 0

for a in range(-1 * rangemax, rangemax):
    for b in range(-1 * (rangemax + 1), rangemax + 1):
        n = 0
        primes_sequence = 0
        while (functions.is_prime(functions.quadratic(n, a, b))):
            n += 1
            primes_sequence += 1

        if primes_sequence > max_primes_sequences:
            max_primes_sequences = primes_sequence
            a_max = a
            b_max = b

solution27 = [a_max * b_max]

print("Sol27: ", a_max, b_max, "generate", max_primes_sequences, "\n",
      "product: ", solution27)
