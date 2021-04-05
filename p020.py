"""Find the sum of the digits in the number 100!."""

import functions

solution20 = 0
for digit in str(functions.factorial(100)):
    solution20 += int(digit)

print("Sol20: ", solution20)
