import functions as f

N = 4000000
solution2 = 0

list_fibo = f.fibo(N)
for i in list_fibo:
    if f.is_multi(i, 2):
        solution2 += i

print("Sol2: ", solution2)
