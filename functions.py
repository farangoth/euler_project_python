#/usr/bin/env python3

import numpy as np

def is_multi(i, N):
    """Returns True if i is a multiple of N"""

    return i%N == 0

def recur_fibon(n):
    if n <= 1:
        return n
    else:
        return(recur_fibon(n-1) + recur_fibon(n-2))

def fibo(N):
    """Returns list of Fibonacci terms under N"""
    fibo_terms = []

    n = 1
    while(recur_fibon(n) < N):
        fibo_terms.append(recur_fibon(n+1))
        n += 1

    return(fibo_terms)


def factors(N):
    """Returns the list of factors for an integer N."""

    list_factor = []

    for p in range(1, int(np.sqrt(N)+1)):
        if N%p == 0:
            list_factor.append(p)
            list_factor.append(int(N/p))

    list_factor.append(N)
    return(list_factor)

def is_prime(N):
    """Returns True if the integer is prime."""

    if len(factors(N)) == 2:
        return True
    else:
        return False

def list_primes_v1(N):
    """Returns prime numbers under N."""
    list_primes = []

    for n in range(N+1):
        if is_prime(n):
            list_primes.append(n)
        print(list_primes)

    return list_primes

def is_palindrom(N):
    digits = [int(n) for n in str(N)]

    for pos in range(int(len(digits)/2)):
        if digits[pos] == digits[-pos-1]:
            continue
        else:
            return False
    return bool

def div_check(n, rangemax):
    if all(n%p == 0 for p in list_primes_v1(rangemax)):
        return True
    else:
        return False

def list_primes_crible(N):
    """Returns Euratosthene crible for integers under N."""

    list_numbers = [n for n in range(2,N+1)]
    list_is_prime = [True for n in list_numbers]

    for n in list_numbers:
        if list_is_prime[n-2]:
            list_is_prime[n-2] = True
            i = 2
            while(i*n < N+1):
                list_is_prime[n*i-2] = False
                i += 1
        else:
            continue

    list_numbers = np.array(list_numbers)
    list_primes = list_numbers[list_is_prime]
    return list_primes

def common_factors(list):
    list_factors = [[] for n in list]

    i = 0
    for n in list:
        list_factors[i] = factors(n)
        i += 1

    list_common_factors = {fact for sublist in list_factors for fact in sublist if all(fact in sublist for sublist in list_factors)}

    return list_common_factors

def pgcd_list_naif(list):
    list_common_factors = common_factors(list)

    pgcd = 1
    for fact in list_common_factors:
        if fact > pgcd:
            pgcd = fact
    return pgcd

def euclide(a, b):
    """Returns the GCD of two intergers using Euclide."""
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b

    return a

def pgcd(*args):
    """Returns the GCD of a list of integers."""
    gcd = euclide(args[0], args[1])

    for a in args:
        gcd = euclide(gcd, a)

    return gcd

def calc_lcm(a, b):
    return int((a*b)/euclide(a,b))

def lcm(*args):
    result = calc_lcm(args[0], args[1])
    for a in args:
        result = calc_lcm(a, result)
    return result

def factorize_v1(N):
    primes = list_primes_crible(int(N/2)+1)
    prime_factors = dict()

    for prime in primes:
        prime_factors.update({prime: 0})

    for prime in prime_factors.keys():
        if N%prime == 0:
            exposant = 1
            reste = N%(prime**exposant)
            while reste == 0:
                exposant += 1
                reste = N%(prime**exposant)
            prime_factors.update({prime: exposant-1})
    return prime_factors
