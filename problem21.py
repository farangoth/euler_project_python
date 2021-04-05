"""Evaluate the sum of all the amicable numbers under 10000."""

import functions

rangemax = 10000
list_amicables = set()
sum_amicables = 0
for N in range(2, rangemax + 1):
    if any([
            functions.is_amicable(N, b) and N != b
            for b in range(2, rangemax + 1)
    ]):
        list_amicables.add(N)
        sum_amicables += N

print(list_amicables)
print("Sol21: ", sum_amicables)
