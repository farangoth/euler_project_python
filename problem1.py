#/usr/bin/env python3

from functions import *

def problem1():
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    list_multi = []

    for i in range(1,1000):
        if is_multi(i, 5) or is_multi(i,3):
            if i not in list_multi:
                list_multi.append(i)

    solution1 = sum(list_multi)

    print("Sol1: ", solution1)
    return solution1

def problem2():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

    N = 4000000
    solution2 = 0

    list_fibo = fibo(N)
    for i in list_fibo:
        if is_multi(i, 2):
            solution2 += i

    print("Sol2: ", solution2)
    return solution2

def problem3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """

    N = 600851475143
    list_factors = factors(N)

    list_prime_factors = [p for p in list_factors if is_prime(p)]

    P = 0
    for p in list_prime_factors:
        if p > P:
            P = p

    print("Sol3: ", P)
    return P

def problem4():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    list_palidroms = []
    for n in range(100,999):
        for m in range(100,999):
            if is_palindrom(n*m):
                list_palidroms.append(n*m)

    solution4 = 0
    for n in list_palidroms:
        if n > solution4:
            solution4 = n

    print("Sol4: ", solution4)
    return solution4

def problem5():
    """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    N = 20

    solution5 = lcm(*range(1,N))

    print("Sol5: ", solution5)
    return solution5

def problem6():
    """Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

    sum1 = 0
    sum2 = 0
    for n in range(0,101):
        sum1 += n
        sum2 += n**2

    solution6 = -sum2 + sum1**2
    print("Sol6: ", solution6)
    return

def problem7():
    """What is the 10 001st prime number?"""

    N = 10001
    primes = list_primes_v2(N)

    print("Sol7: ", primes[-1])
    return primes[-1]

def problem8():
    """Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?
    """

    digits = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    str_digits = str(digits)
    len_prod = 13

    prod_max = 1

    for n in range(0, len(str_digits)-len_prod):
        str_slice = str_digits[n:n+len_prod]
        prod = 1
        for digit in str_slice:
            prod *= int(digit)
        if prod > prod_max:
            prod_max = prod

    print("Sol8: ", prod_max)
    return prod_max

def problem9():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    sum = 1000

    for a in range(1,sum):
        for b in range(1, sum-a):
            c = sum - (a + b)
            if is_pythagorean(a, b, c):
                print("Sol9: ", a, b, c, " - ", a*b*c)
                return a*b*c

def problem10():
    """Find the sum of all the primes below two million."""

    rangemax = 2000000
    primes = list_primes_crible(rangemax)
    sum_primes = 0

    for prime in primes:
        sum_primes += prime

    print("Sol10 :", sum_primes)
    return sum_primes

def problem11():
    """What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?"""

    grid = [
    [ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8],
    [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0],
    [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65],
    [52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91],
    [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
    [24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50],
    [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
    [67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21],
    [24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
    [21,36,23, 9,75,00,76,44,20,45,35,14, 0,61,33,97,34,31,33,95],
    [78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92],
    [16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57],
    [86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58],
    [19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40],
    [ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66],
    [88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69],
    [ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36],
    [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16],
    [20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54],
    [ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]
    ]

    max_prod = 0
    # horizontal couple
    for row in grid:
        for index in range(0, len(row)-3):
            prod = row[index]*row[index+1]*row[index+2]*row[index+3]
            if prod > max_prod:
                max_prod = prod
    # vertical couple
    for index_column in range(0, len(grid[0])):
        for index_line in range(0, len(grid[0])-3):
            prod = grid[index_line][index_column]* \
            grid[index_line+1][index_column]* \
            grid[index_line+2][index_column]* \
            grid[index_line+3][index_column]

            if prod > max_prod:
                max_prod = prod

    # diagonal SE couple
    for index_column in range(0, len(grid[0])-3):
        for index_line in range(0, len(grid[0])-3):
            prod = grid[index_line][index_column]* \
            grid[index_line+1][index_column+1]* \
            grid[index_line+2][index_column+2]* \
            grid[index_line+3][index_column+3]

            if prod > max_prod:
                max_prod = prod

    # diagonal SW couple
    for index_column in range(3, len(grid[0])-3):
        for index_line in range(3, len(grid[0])):
            prod = grid[index_line][index_column]* \
            grid[index_line-1][index_column+1]* \
            grid[index_line-2][index_column+2]* \
            grid[index_line-3][index_column+3]

            if prod > max_prod:
                max_prod = prod

    print("Sol11: ", max_prod)
    return max_prod

def problem12():
    """What is the value of the first triangle number to have over five hundred divisors?"""

    n_factors = 0
    triangle_number = 0
    n = 1

    while n_factors < 500:
        triangle_number += n
        n_factors = len(factors(triangle_number))
        n += 1

    print("Sol12: ", triangle_number, " - ", n_factors, "factors.")

def problem13():
    numbers = [37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676,
        89261670696623633820136378418383684178734361726757,
        28112879812849979408065481931592621691275889832738,
        44274228917432520321923589422876796487670272189318,
        47451445736001306439091167216856844588711603153276,
        70386486105843025439939619828917593665686757934951,
        62176457141856560629502157223196586755079324193331,
        64906352462741904929101432445813822663347944758178,
        92575867718337217661963751590579239728245598838407,
        58203565325359399008402633568948830189458628227828,
        80181199384826282014278194139940567587151170094390,
        35398664372827112653829987240784473053190104293586,
        86515506006295864861532075273371959191420517255829,
        71693888707715466499115593487603532921714970056938,
        54370070576826684624621495650076471787294438377604,
        53282654108756828443191190634694037855217779295145,
        36123272525000296071075082563815656710885258350721,
        45876576172410976447339110607218265236877223636045,
        17423706905851860660448207621209813287860733969412,
        81142660418086830619328460811191061556940512689692,
        51934325451728388641918047049293215058642563049483,
        62467221648435076201727918039944693004732956340691,
        15732444386908125794514089057706229429197107928209,
        55037687525678773091862540744969844508330393682126,
        18336384825330154686196124348767681297534375946515,
        80386287592878490201521685554828717201219257766954,
        78182833757993103614740356856449095527097864797581,
        16726320100436897842553539920931837441497806860984,
        48403098129077791799088218795327364475675590848030,
        87086987551392711854517078544161852424320693150332,
        59959406895756536782107074926966537676326235447210,
        69793950679652694742597709739166693763042633987085,
        41052684708299085211399427365734116182760315001271,
        65378607361501080857009149939512557028198746004375,
        35829035317434717326932123578154982629742552737307,
        94953759765105305946966067683156574377167401875275,
        88902802571733229619176668713819931811048770190271,
        25267680276078003013678680992525463401061632866526,
        36270218540497705585629946580636237993140746255962,
        24074486908231174977792365466257246923322810917141,
        91430288197103288597806669760892938638285025333403,
        34413065578016127815921815005561868836468420090470,
        23053081172816430487623791969842487255036638784583,
        11487696932154902810424020138335124462181441773470,
        63783299490636259666498587618221225225512486764533,
        67720186971698544312419572409913959008952310058822,
        95548255300263520781532296796249481641953868218774,
        76085327132285723110424803456124867697064507995236,
        37774242535411291684276865538926205024910326572967,
        23701913275725675285653248258265463092207058596522,
        29798860272258331913126375147341994889534765745501,
        18495701454879288984856827726077713721403798879715,
        38298203783031473527721580348144513491373226651381,
        34829543829199918180278916522431027392251122869539,
        40957953066405232632538044100059654939159879593635,
        29746152185502371307642255121183693803580388584903,
        41698116222072977186158236678424689157993532961922,
        62467957194401269043877107275048102390895523597457,
        23189706772547915061505504953922979530901129967519,
        86188088225875314529584099251203829009407770775672,
        11306739708304724483816533873502340845647058077308,
        82959174767140363198008187129011875491310547126581,
        97623331044818386269515456334926366572897563400500,
        42846280183517070527831839425882145521227251250327,
        55121603546981200581762165212827652751691296897789,
        32238195734329339946437501907836945765883352399886,
        75506164965184775180738168837861091527357929701337,
        62177842752192623401942399639168044983993173312731,
        32924185707147349566916674687634660915035914677504,
        99518671430235219628894890102423325116913619626622,
        73267460800591547471830798392868535206946944540724,
        76841822524674417161514036427982273348055556214818,
        97142617910342598647204516893989422179826088076852,
        87783646182799346313767754307809363333018982642090,
        10848802521674670883215120185883543223812876952786,
        71329612474782464538636993009049310363619763878039,
        62184073572399794223406235393808339651327408011116,
        66627891981488087797941876876144230030984490851411,
        60661826293682836764744779239180335110989069790714,
        85786944089552990653640447425576083659976645795096,
        66024396409905389607120198219976047599490197230297,
        64913982680032973156037120041377903785566085089252,
        16730939319872750275468906903707539413042652315011,
        94809377245048795150954100921645863754710598436791,
        78639167021187492431995700641917969777599028300699,
        15368713711936614952811305876380278410754449733078,
        40789923115535562561142322423255033685442488917353,
        44889911501440648020369068063960672322193204149535,
        41503128880339536053299340368006977710650566631954,
        81234880673210146739058568557934581403627822703280,
        82616570773948327592232845941706525094512325230608,
        22918802058777319719839450180888072429661980811197,
        77158542502016545090413245809786882778948721859617,
        72107838435069186155435662884062257473692284509516,
        20849603980134001723930671666823555245252804609722,
        53503534226472524250874054075591789781264330331690
        ]

    sum = 0
    for number in numbers:
        sum += number

    print("Sol13: ", str(sum)[:10])

def problem14():
    """Longest Collatz chain under 1000000."""

    rangemax = 1000000
    collatz_longest = 1
    collatz_longest_length = 1
    for start in range(1,rangemax):
        collatz_length = len(collatz(start))
        if collatz_length > collatz_longest_length:
            collatz_longest = start
            collatz_longest_length = collatz_length

    print("Sol14: Start -", collatz_longest," Length -", collatz_longest_length)

    return collatz_length, collatz_longest_length

if __name__=="__main__":
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
    # problem6()
    # problem7()
    # problem8()
    # problem9()
    # problem10()
    # problem11()
    problem14()
