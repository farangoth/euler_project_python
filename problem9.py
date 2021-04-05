import functions

sum = 1000

for a in range(1, sum):
    for b in range(1, sum - a):
        c = sum - (a + b)
        if functions.is_pythagorean(a, b, c):
            print("Sol9: ", a, b, c, " - ", a * b * c)
