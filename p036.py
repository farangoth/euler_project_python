"""Problem 36

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2."""

import functions as fct

rangemax = 1000000
palindroms_base_2_and_10 = []

for N in range(1, rangemax):
    N_base_2 = fct.convert_decimal_to_base(N, 2)
    if fct.is_palindrom(N) and fct.is_palindrom(N_base_2):
        palindroms_base_2_and_10.append(N)

print(palindroms_base_2_and_10)
print("Sol36: ", sum(palindroms_base_2_and_10))
