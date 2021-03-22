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

    N = 10001
    primes = list_primes_v2(N)

    print("Sol7: ", primes[-1])
    return primes[-1]

def problem8():
    """Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?
    """

    digits = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    str_digits = str(digits)
    len_prod = 13

    prod_max = 1

    for n in range(0, len(str_digits)-len_prod):
        str_slice = str_digits[n:n+len_prod]
        prod = 1
        for digit in str_slice:
            prod *= int(digit)
        if prod > prod_max:
            prod_max = prod

    print("Sol8: ", prod_max)
    return prod_max

def problem9():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    sum = 1000

    for a in range(1,sum):
        for b in range(1, sum-a):
            c = sum - (a + b)
            if is_pythagorean(a, b, c):
                print("Sol9: ", a, b, c, " - ", a*b*c)
                return a*b*c

def problem10():
    """Find the sum of all the primes below two million."""

    rangemax = 2000000
    primes = list_primes_crible(rangemax)
    sum_primes = 0

    for prime in primes:
        sum_primes += prime

    print("Sol10 :", sum_primes)
    return sum_primes

def problem11():
    """What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?"""

    grid = [
    [ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8],
    [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0],
    [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65],
    [52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91],
    [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
    [24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50],
    [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
    [67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21],
    [24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
    [21,36,23, 9,75,00,76,44,20,45,35,14, 0,61,33,97,34,31,33,95],
    [78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92],
    [16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57],
    [86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58],
    [19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40],
    [ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66],
    [88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69],
    [ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36],
    [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16],
    [20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54],
    [ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]
    ]

    max_prod = 0
    # horizontal couple
    for row in grid:
        for index in range(0, len(row)-3):
            prod = row[index]*row[index+1]*row[index+2]*row[index+3]
            if prod > max_prod:
                max_prod = prod
    # vertical couple
    for index_column in range(0, len(grid[0])):
        for index_line in range(0, len(grid[0])-3):
            prod = grid[index_line][index_column]* \
            grid[index_line+1][index_column]* \
            grid[index_line+2][index_column]* \
            grid[index_line+3][index_column]

            if prod > max_prod:
                max_prod = prod

    # diagonal SE couple
    for index_column in range(0, len(grid[0])-3):
        for index_line in range(0, len(grid[0])-3):
            prod = grid[index_line][index_column]* \
            grid[index_line+1][index_column+1]* \
            grid[index_line+2][index_column+2]* \
            grid[index_line+3][index_column+3]

            if prod > max_prod:
                max_prod = prod

    # diagonal SW couple
    for index_column in range(3, len(grid[0])-3):
        for index_line in range(3, len(grid[0])):
            prod = grid[index_line][index_column]* \
            grid[index_line-1][index_column+1]* \
            grid[index_line-2][index_column+2]* \
            grid[index_line-3][index_column+3]

            if prod > max_prod:
                max_prod = prod

    print(max_prod)


if __name__=="__main__":
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
    # problem6()
    # problem7()
    # problem8()
    # problem9()
    # problem10()
    problem11()
