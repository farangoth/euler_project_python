with open("p008_digits.txt", "r") as f:
    digits = f.read()

len_prod = 13
prod_max = 1
for n in range(0, len(digits) - len_prod):
    str_slice = digits[n:n + len_prod]
    prod = 1
    for digit in str_slice:
        prod *= int(digit)
        if prod > prod_max:
            prod_max = prod

print("Sol8: ", prod_max)
