"""If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?"""

import functions

rangemax = 1000
total_letters = 0
for n in range(1, rangemax + 1):
    for word in functions.litteraze(n):
        total_letters += len(word)

print("Sol17: ", total_letters)
