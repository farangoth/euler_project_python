"""There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

from functools import reduce
import functions as f

cancelling_fractions = []

for n in range(10, 100):
    for d in range(10, n):
        digits_n = [n%10, n//10]
        digits_d = [d%10, d//10]
        if any([a==0 for a in digits_d]) or any([a==0 for a in digits_n]):
            continue
        elif n == d:
            continue
        elif f.pgcd(n, d) == 1:
            continue
        for a in digits_n:    
            if a in digits_d:
                digits_n.remove(a)
                digits_d.remove(a)
                if n/d == int(digits_n[0])/int(digits_d[0]):
                    cancelling_fractions.append([n, d])

print(cancelling_fractions)
product = [reduce((lambda x, y: x * y), [nd[0] for nd in cancelling_fractions]), reduce((lambda x, y: x*y), [nd[1] for nd in cancelling_fractions])]
print(product[0]//f.pgcd(product[0], product[1]))