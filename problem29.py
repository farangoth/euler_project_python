max_a = 100
max_b = 100

powers = set()
for a in range(2, max_a + 1):
    for b in range(2, max_b + 1):
        powers.add(a**b)

print(powers)
solution29 = len(powers)
print("Sol29: ", solution29)
