import functions as f

list_palidroms = []
for n in range(100, 999):
    for m in range(100, 999):
        if f.is_palindrom(n * m):
            list_palidroms.append(n * m)

solution4 = 0
for n in list_palidroms:
    if n > solution4:
        solution4 = n

print("Sol4: ", solution4)
