import functions as f

list_multi = []

for i in range(1, 1000):
    if f.is_multi(i, 5) or f.is_multi(i, 3):
        if i not in list_multi:
            list_multi.append(i)

solution1 = sum(list_multi)

print("Sol1: ", solution1)
