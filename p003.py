import functions as f

N = 600851475143
list_factors = f.factors(N)

list_prime_factors = [p for p in list_factors if f.is_prime(p)]

P = 0
for p in list_prime_factors:
    if p > P:
        P = p

print("Sol3: ", P)
