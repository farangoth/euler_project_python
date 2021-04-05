"""Longest Collatz chain under 1000000."""

import functions

rangemax = 1000000
collatz_longest = 1
collatz_longest_length = 1
for start in range(1, rangemax):
    collatz_length = len(functions.collatz(start))
    if collatz_length > collatz_longest_length:
        collatz_longest = start
        collatz_longest_length = collatz_length

print("Sol14: Start -", collatz_longest, " Length -", collatz_longest_length)
