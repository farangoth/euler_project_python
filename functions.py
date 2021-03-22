#/usr/bin/env python3

import numpy as np

def is_multi(i, N):
    """Returns True if i is a multiple of N"""

    return i%N == 0

def recur_fibon(n):
    """Returns the nth term of Fibonacci sequence."""
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

    factors = []

    for p in range(1, int(np.sqrt(N)+1)):
        if N%p == 0:
            factors.append(p)
            factors.append(int(N/p))

    factors.append(N)
    return(factors)

def is_prime(N):
    """Returns True if the integer is prime."""

    if N <= 1:
        return False
    for n in range(2, N//2+1):
        if N%n == 0:
            return False
        else:
            continue

    return True

def list_primes_v1(N):
    """Returns prime numbers under N."""

    list_primes = []

    for n in range(N+1):
        if is_prime(n):
            list_primes.append(n)

    return list_primes

def is_palindrom(N):
    """Returns True if the number is a palindrom, readable in both directions."""

    digits = [int(n) for n in str(N)]

    for pos in range(int(len(digits)/2)):
        if digits[pos] == digits[-pos-1]:
            continue
        else:
            return False
    return bool

def div_check(n, rangemax):
    """Returns True if the number is divisible by all prime numbers under rangemax."""

    if all(n%p == 0 for p in list_primes_crible(rangemax)):
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

def list_primes_v2(N):
    """Returns list of primes up to the N-th prime."""

    list_primes = [2]
    n = 2

    while len(list_primes) < N :
        n += 1
        if is_prime(n):
            list_primes.append(n)

    return list_primes

def common_factors(*args):
    """Returns a list of common factors."""

    list_factors = [[] for n in args]

    i = 0
    for n in args:
        list_factors[i] = factors(n)
        i += 1

    list_common_factors = {fact for sublist in list_factors for fact in sublist if all(fact in sublist for sublist in list_factors)}

    return list_common_factors

def pgcd_list_naif(*args):
    """Returns the GCD of a list of numbers."""

    list_common_factors = common_factors(args)

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
    """Returns the least common multiple of two intergers."""

    return int((a*b)/euclide(a,b))

def lcm(*args):
    """Returns the least common multiple of a list of intergers."""

    result = calc_lcm(args[0], args[1])
    for a in args:
        result = calc_lcm(a, result)

    return result

def factorize_v1(N):
    """Returns the prime factors and their exposants of an interger, in the shape of a dictionary."""
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

def is_pythagorean(a, b, c):
    """Checks if the triplet respect a**2+b**2=c**2."""

    return a**2 + b**2 == c**2

def triangle_numbers(N):
    """Generates the N-th first triangle numbers."""

    list_triangle = [1]
    for n in range(2, N):
        list_triangle.append(list_triangle[-1]+n)

    return list_triangle

def collatz(N):
    """Returns the chain of Collatz starting fron N."""

    collatz_chain = [N]

    while(collatz_chain[-1] != 1):
        if collatz_chain[-1]%2 == 0:
            collatz_chain.append(collatz_chain[-1]//2)
        else:
            collatz_chain.append(3*collatz_chain[-1]+1)
            
    return collatz_chain
