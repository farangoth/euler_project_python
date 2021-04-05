with open("p013_numbers.txt", "r") as f:
    numbers = [int(number) for number in f.readlines()]

sum = 0
for number in numbers:
    sum += number

print("Sol13: ", str(sum)[:10])
