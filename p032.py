"""Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital."""

import functions as f

list_pandigital = set()

for multicand in range(1, 100):
    for multiplier in range(99, 10000):
        product = multicand * multiplier
        if f.is_pandigital(''.join(str([multicand,multiplier,product])), 9) and len(str(product)) <= 4:
            print(multicand, "*", multiplier, "=", product)
            list_pandigital.add(product)

print(list_pandigital)
print("Sol32: ", sum(list_pandigital))