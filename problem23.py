"""Find the sum of all the positive integers which cannot be written
as the sum of two abundant numbers."""

import functions

rangemax = 28123
abundant_numbers = functions.get_abundant_numbers(rangemax)

# list_not_sum_abundants = set()

# for n in range(1,rangemax):
#     if all([not(n-a in abundant_numbers) for a in abundant_numbers]):
#         list_not_sum_abundants.add(n)

not_sum_abundants = [*range(1, rangemax + 1)]
solution23 = 0
for a in abundant_numbers:
    for b in abundant_numbers:
        if a + b in not_sum_abundants:
            not_sum_abundants.remove(a + b)

for n in not_sum_abundants:
    solution23 += n

print("Sol23: ", solution23)
