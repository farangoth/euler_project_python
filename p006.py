sum1 = 0
sum2 = 0
for n in range(0, 101):
    sum1 += n
    sum2 += n**2

solution6 = -sum2 + sum1**2
print("Sol6: ", solution6)
