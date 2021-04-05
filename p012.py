"""What is the value of the first triangle number
to have over five hundred divisors?"""

import functions

n_factors = 0
triangle_number = 0
n = 1

while n_factors < 500:
    triangle_number += n
    n_factors = len(functions.factors(triangle_number))
    n += 1

print("Sol12: ", triangle_number, " - ", n_factors, "factors.")
