"""What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""

import functions as f

len_max = 0
p_max, n_max = 0, 0
product_max = 0

for p in range(1, 10000):
    for n in range(1, 9):
        product = f.concatenated_product(p, n)
        if len(str(product)) > 9:
            break
        if f.is_pandigital(product, 9) and product > product_max:
            p_max, n_max, product_max = p, n, product
            print(p_max, n_max, product_max)

print(p_max, n_max, product_max)