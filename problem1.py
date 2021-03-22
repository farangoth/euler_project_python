#/usr/bin/env python3

from functions import *

def problem1():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    list_multi = []

    for i in range(1,1000):
        if is_multi(i, 5) or is_multi(i,3):
            if i not in list_multi:
                list_multi.append(i)

    solution1 = sum(list_multi)

    print("Sol1: ", solution1)
    return solution1

def problem2():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

    N = 4000000
    solution2 = 0

    list_fibo = fibo(N)
    for i in list_fibo:
        if is_multi(i, 2):
            solution2 += i

    print("Sol2: ", solution2)
    return solution2

def problem3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """

    N = 600851475143
    list_factors = factors(N)

    list_prime_factors = [p for p in list_factors if is_prime(p)]

    P = 0
    for p in list_prime_factors:
        if p > P:
            P = p

    print("Sol3: ", P)
    return P

def problem4():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    list_palidroms = []
    for n in range(100,999):
        for m in range(100,999):
            if is_palindrom(n*m):
                list_palidroms.append(n*m)

    solution4 = 0
    for n in list_palidroms:
        if n > solution4:
            solution4 = n

    print("Sol4: ", solution4)
    return solution4

def problem5():
    """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    N = 20

    solution5 = lcm(*range(1,N))

    print("Sol5: ", solution5)
    return solution5

def problem6():
    """Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

    sum1 = 0
    sum2 = 0
    for n in range(0,101):
        sum1 += n
        sum2 += n**2

    solution6 = -sum2 + sum1**2
    print("Sol6: ", solution6)
    return

def problem7():
    """What is the 10 001st prime number?"""

    N = 100001
    primes = list_primes_v1(N)

    print(primes)

if __name__=="__main__":
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
    # problem6()