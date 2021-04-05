"""What is the sum of the digits of the number 2**1000?"""

digits = str(2**1000)

sum = 0
for digit in digits:
    sum += int(digit)

print("Sol16: ", sum)
