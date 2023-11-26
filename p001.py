"""Solving P1 from Euler porject."""
import time
import functions as f

start = time.time()

list_multi = []

for i in range(1, 1000):
    if f.is_multi(i, 5) or f.is_multi(i, 3):
        if i not in list_multi:
            list_multi.append(i)

solution1 = sum(list_multi)

end = time.time()

print("Sol1: ", solution1)
print("time ", str(end-start))
