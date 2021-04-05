# Building the diagonal
diagonal = [3]
while (len(diagonal) < 2000):
    diagonal.append(diagonal[-1] + 2 * (len(diagonal) // 4 + 1))

solution28 = 1
for number in diagonal:
    solution28 += number

print("Sol28: ", solution28)
