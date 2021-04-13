rangemax = 1000000

champernowne = "0"
integer = 1
while (len(champernowne) < rangemax + 1):
    champernowne += str(integer)
    integer += 1

solution40 = int(champernowne[1]) * int(champernowne[10]) \
    * int(champernowne[100]) * int(champernowne[1000]) \
    * int(champernowne[10000]) * int(champernowne[100000]) \
    * int(champernowne[1000000])

print("Sol40: ", solution40)
