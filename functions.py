"""Mathematical functions to solve Euler problems.
<http://euler-project.com>"""

from operator import concat
from typing import Concatenate
import numpy as np


def is_multi(i, N):
    """Return True if i is a multiple of N."""
    return i % N == 0


def recur_fibon(n):
    """Return the nth term of Fibonacci sequence."""
    if n <= 1:
        return n
    else:
        return (recur_fibon(n - 1) + recur_fibon(n - 2))


def fibo(N):
    """Return list of Fibonacci terms under N."""
    fibo_terms = []

    n = 1
    while (recur_fibon(n) < N):
        fibo_terms.append(recur_fibon(n + 1))
        n += 1

    return fibo_terms


def factors(N):
    """Return the list of factors for an integer N."""
    factors = []

    for p in range(1, int(np.sqrt(N) + 1)):
        if N % p == 0:
            factors.append(p)
            factors.append(int(N / p))

    factors.append(N)
    return (factors)


def proper_divisors(N):
    """Return the list of proper divisors for an integer N."""
    divisors = set()

    divisors.add(1)
    for p in range(2, int(np.sqrt(N) + 1)):
        if N % p == 0:
            divisors.add(p)
            divisors.add(int(N / p))

    return divisors


def is_prime(N):
    """Return True if the integer is prime."""
    if N <= 1:
        return False
    for n in range(2, N // 2 + 1):
        if N % n == 0:
            return False
        else:
            continue

    return True


def list_primes_v1(N):
    """Return prime numbers under N."""
    list_primes = []

    for n in range(N + 1):
        if is_prime(n):
            list_primes.append(n)

    return list_primes


def is_palindrom(N):
    """Check if the number is a palindrom, readable in both directions."""
    digits = [int(n) for n in str(N)]

    for pos in range(int(len(digits) / 2)):
        if digits[pos] == digits[-pos - 1]:
            continue
        else:
            return False
    return bool


def div_check(n, rangemax):
    """Check if the integer is divisible by all primes under a range."""
    if all(n % p == 0 for p in list_primes_crible(rangemax)):
        return True
    else:
        return False


def list_primes_crible(N):
    """Return Euratosthene crible for integers under N."""
    list_numbers = [n for n in range(2, N + 1)]
    list_is_prime = [True for n in list_numbers]

    for n in list_numbers:
        if list_is_prime[n - 2]:
            list_is_prime[n - 2] = True
            i = 2
            while (i * n < N + 1):
                list_is_prime[n * i - 2] = False
                i += 1
        else:
            continue

    list_numbers = np.array(list_numbers)
    list_primes = list_numbers[list_is_prime]
    return list_primes


def get_primes_with_sieve(N):
    """Return Euratosthene crible for integers under N."""
    # Create a list of as many True as there is uneven numbers under N.
    sieve = [True] * (N // 2)
    for n in range(3, int(N**1 / 2) + 1, 2):
        if sieve[n // 2]:
            # Replace True by False for all the multiple
            sieve[n * n // 2::n] = [False] * ((N - n * n - 1) // (2 * n) + 1)

    is_abundant
    return [2] + [2 * n + 1 for n in range(1, N // 2) if sieve[n]]


def list_primes_v2(N):
    """Return list of primes up to the N-th prime."""
    list_primes = [2]
    n = 2

    while len(list_primes) < N:
        n += 1
        if is_prime(n):
            list_primes.append(n)

    return list_primes


def common_factors(*args):
    """Return a list of common factors."""
    list_factors = [[] for n in args]

    i = 0
    for n in args:
        list_factors[i] = factors(n)
        i += 1

    list_common_factors = {
        fact
        for sublist in list_factors for fact in sublist
        if all(fact in sublist for sublist in list_factors)
    }

    return list_common_factors


def pgcd_list_naif(*args):
    """Return the GCD of a list of numbers."""
    list_common_factors = common_factors(args)

    pgcd = 1
    for fact in list_common_factors:
        if fact > pgcd:
            pgcd = fact

    return pgcd


def euclide(a, b):
    """Return the GCD of two intergers using Euclide."""
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a


def pgcd(*args):
    """Return the GCD of a list of integers."""
    gcd = euclide(args[0], args[1])

    for a in args:
        gcd = euclide(gcd, a)

    return gcd


def calc_lcm(a, b):
    """Return the least common multiple of two intergers."""
    return int((a * b) / euclide(a, b))


def lcm(*args):
    """Return the least common multiple of a list of intergers."""
    result = calc_lcm(args[0], args[1])
    for a in args:
        result = calc_lcm(a, result)

    return result


def factorize_v1(N):
    """Return prime factors and exposants."""
    primes = list_primes_crible(int(N / 2) + 1)
    prime_factors = dict()

    for prime in primes:
        prime_factors.update({prime: 0})

    for prime in prime_factors.keys():
        if N % prime == 0:
            exposant = 1
            reste = N % (prime**exposant)
            while reste == 0:
                exposant += 1
                reste = N % (prime**exposant)
            prime_factors.update({prime: exposant - 1})

    return prime_factors


def is_pythagorean(a, b, c):
    """Check if the triplet respect a**2+b**2=c**2."""
    return a**2 + b**2 == c**2


def triangle_numbers(N):
    """Generate the N-th first triangle numbers."""
    list_triangle = [1]
    for n in range(2, N):
        list_triangle.append(list_triangle[-1] + n)

    return list_triangle


def collatz(N):
    """Return the chain of Collatz starting fron N."""
    collatz_chain = [N]

    while (collatz_chain[-1] != 1):
        if collatz_chain[-1] % 2 == 0:
            collatz_chain.append(collatz_chain[-1] // 2)
        else:
            collatz_chain.append(3 * collatz_chain[-1] + 1)

    return collatz_chain


def litteraze(N):
    """Return the English spelling of an intergers up to 9999."""
    dict_numbers = {
        0: "",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
        10: "TEN",
        11: "ELEVEN",
        12: "TWELVE",
        13: "THIRTEEN",
        14: "FOURTEEN",
        15: "FIFTEEN",
        16: "SIXTEEN",
        17: "SEVENTEEN",
        18: "EIGHTEEN",
        19: "NINETEEN",
        20: "TWENTY",
        30: "THIRTY",
        40: "FORTY",
        50: "FIFTY",
        60: "SIXTY",
        70: "SEVENTY",
        80: "EIGHTY",
        90: "NINETY",
        100: "HUNDRED",
        1000: "THOUSAND",
        "AND": "AND"
    }

    in_letters = []
    digits = str(N)

    if len(digits) >= 4:
        in_letters.append(dict_numbers.get(int(digits[-4])))
        in_letters.append(dict_numbers.get(1000))
    if len(digits) >= 3:
        if int(digits[-3]):
            in_letters.append(dict_numbers.get(int(digits[-3])))
            in_letters.append(dict_numbers.get(100))
        if digits[-2:] != "00":
            in_letters.append(dict_numbers.get("AND"))
    if 0 < int(digits[-2:]) <= 20:
        in_letters.append(dict_numbers.get(int(digits[-2:])))
    else:
        in_letters.append(dict_numbers.get(int(digits[-2]) * 10))
        in_letters.append(dict_numbers.get(int(digits[-1])))

    return in_letters


def maximum(*args):
    """Return the maximum from a list."""
    result = args[0]
    for n in args:
        if n > result:
            result = n

    return result


def best_sum(triangle):
    """Return the best sum available for a path along the triangle."""
    for index_row in range(len(triangle) - 2, -1, -1):
        for index_column in range(0, len(triangle[index_row]) - 1):
            triangle[index_row][index_column] = \
                triangle[index_row][index_column] + \
                maximum(triangle[index_row+1][index_column],
                        triangle[index_row+1][index_column+1])

    return triangle[0][0]


def is_leap(year):
    """Return True if the year is a leap one."""
    if year % 100:
        if year % 400:
            return True
        else:
            return False
    if year % 4:
        return True
    else:
        return False


def days_gap(date1, date2):
    """Return the numbers of days between two dates."""
    pass


def which_day():
    """Return the day of a date [yyyy, mm, dd]."""
    pass


def factorial(N):
    """Return the factorial N!."""
    result = 1
    for n in range(1, N + 1):
        result *= n

    return result


def sum_factors(N):
    """Return the sum of the factors of an integer."""
    result = 0
    for factor in proper_divisors(N):  # all factors but himself
        result += factor

    return result


def is_amicable(a, b):
    """Check if the two integers are amicables."""
    return sum_factors(a) == b and sum_factors(b) == a


def is_perfect(N):
    """Check if the integer is a perfect number ie. sum(divisors(n)) = n."""
    return sum_factors(N) == N


def is_abundant(N):
    """Check if an integer is abundant."""
    return sum_factors(N) > N


def get_abundant_numbers(N):
    """Return all abundant numbers under an integer."""
    abundant_numbers = [n for n in range(1, N + 1) if is_abundant(n)]

    return abundant_numbers


def get_fibo(n, n1, n2):
    """Return the n-th first terms of Fibonacci sequence."""
    fibonacci = [n1, n2]

    while (len(fibonacci) < n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci


def euclide_division(A, B):
    """Returns the result of the division of A by B as a list of the digits of the denominators."""
    a = A
    list_rest = []
    cycle = []

    if a < B:
            cycle.append(0)
            a = a*10

    while( not(a in list_rest) ):
        list_rest.append(a)
        cycle.append(a//B)
        a = a%B * 10

    return cycle

def quadratic(n, a, b):
    """Return a quadratic form from parameters."""
    return n**2 + a * n + b


def is_sum_digits_to_power(N, p):
    """Check if the integer is equal to the p-th powers of its digits."""
    digits = str(N)
    sum_digits = 0
    for digit in digits:
        sum_digits += int(digit)**p

    return N == sum_digits


def rotate(L, n):
    """Rotate a list n-times."""
    return L[n:] + L[:n]


def get_circular_primes(N):
    """Returns circular primes under N.
    A circular prime is a prime which all
    rotations of digits is still prime."""
    circular_primes = []
    primes = get_primes_with_sieve(N)
    for prime in primes:
        if all([
                int(rotate(str(prime), n)) in primes
                for n in range(len(str(prime)))
        ]):
            circular_primes.append(prime)

    return circular_primes


def convert_decimal_to_base(N, base):
    """Convert an integer in base 10 to another base."""
    if N == 0:
        return ''
    else:
        return convert_decimal_to_base(N // 2, base) + str(N % 2)

def concatenated_product(p, N):
    """Returns the conactenated product of p and range(1,N)."""

    list_prod = [str(p*n) for n in range(1,N+1)]
    
    return int(''.join(list_prod))

def is_pandigital(N, p):
    """Returns True if all digit (1-p) are present in the integer N."""
    
    if len(str(N)) != p:
        return False

    for n in range(1, p+1):
        if str(n) not in str(N):
            return False
    
    return True