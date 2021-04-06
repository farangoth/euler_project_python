"""Problem 34:
Find the sum of all numbers which are equal to the
sum of the factorial of their digits."""

import functions as fct

rangemax = 362881  # 9!+1
curious_numbers = []
for N in range(3, rangemax):
    sum_factorial_digit = 0
    for digit in str(N):
        sum_factorial_digit += fct.factorial(int(digit))
    if sum_factorial_digit == N:
        curious_numbers.append(N)

print(curious_numbers)
print("Sol34: ", sum(curious_numbers))
