"""What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?"""

n_digits = 1000
fibonacci = [1, 1]

while (len(str(fibonacci[-1])) < n_digits):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Sol26: ", len(fibonacci))
