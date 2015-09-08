__author__ = 'muchaco'

from functions import *

def problem1():
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    # multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    return sum_of_multiples([3, 5], 1000)


def problem2():
    # Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
    # the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci
    # sequence whose values do not exceed four million, find the sum of the even-valued terms.
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1]+fib[-2])
    fib = [i for i in fib if i % 2 == 0]
    return sum(fib)


def problem3():
    # The prime factors of 13195 are 5, 7, 13 and 29.
    # What is the largest prime factor of the number 600851475143 ?
    return max(Primes.set_prime_factors_of(600851475143))


def problem4():
    # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    # is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.
    palindromes = []
    for i in xrange(10**3-1, 10**(3-1)-1, -1):
        for j in xrange(10**3-1, i-1, -1):
            if is_palindrome(i*j):
                palindromes.append(i*j)
    return max(palindromes)


def problem5():
    # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    lst = list()
    final_factors = {}
    for i in xrange(2, 21):
        lst.append(Primes.dict_prime_factors_of(i))
    for i in lst:
        for j in i.keys():
            try:
                if final_factors[j] < i[j]:
                    final_factors[j] = i[j]
            except KeyError:
                final_factors[j] = i[j]
    product = 1
    for i in final_factors.keys():
        product *= i**final_factors[i]
    return product


def problem6():
    #Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    return sum([i for i in xrange(1, 101)])**2 - sum([i**2 for i in xrange(1, 101)])


def problem7():
    # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    # What is the 10001st prime number?
    return Primes._ith_prime(10001)


def problem8():
    # The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832. Find
    # the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this
    # product?
    number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858" \
             "6156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966" \
             "4895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072" \
             "9629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010" \
             "5336788122023542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461" \
             "7406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031998" \
             "9000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294" \
             "7654568284891288314260769004224219022671055626321111109370544217506941658960408071984038509624554443629" \
             "8123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050775410022" \
             "5698315520005593572972571636269561882670428252483600823257530420752963450"
    return greatest_product_in(number, 13)


def problem9():
    # A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    # a**2 + b**2 = c**2
    # There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    # Find the product a*b*c.
    while True:
        for d in xrange(1000):
            for s in xrange(1000):
                for t in xrange(1000):
                    a = 2*d*s*t
                    b = d*(s**2-t**2)
                    c = d*(s**2+t**2)
                    if a > 0 and b > 0 and c > 0 and (a+b+c) == 1000:
                        return a*b*c


def problem10():
    # Find the sum of all the primes below two million.
    prime_obj = Primes(2*10**6+1)
    return sum(prime_obj.get_primes())


def problem11():
    # What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
    # in the 20x20 grid?
    matrix = []
    one_line = []
    nums = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 " \
           "48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 " \
           "68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 " \
           "03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 " \
           "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 " \
           "88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 " \
           "03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 " \
           "71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 " \
           "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 " \
           "32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 " \
           "99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 " \
           "51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 "
    int_nums = []
    for i in xrange(len(nums)/3):
        int_nums.append(int(nums[i*3:i*3+3]))

    for i in xrange(20 * 20):
        one_line.append(int_nums[i])
        if i % 20 == 19:
            matrix.append(one_line[:])
            one_line = []
    return max([start_from(i, j, matrix) for i in xrange(20) for j in xrange(20)])


def problem12():
    # The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
    # 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    # What is the value of the first triangle number to have over five hundred divisors?
    over = 500
    triangle_nums = [1]
    while num_of_divisors(triangle_nums[-1], True) < over + 1:
        triangle_nums.append(triangle_nums[-1] + len(triangle_nums) + 1)
    return triangle_nums[-1]


def problem13():
    # Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    nums = [37107287533902102798797998220837590246510135740250,
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
            53503534226472524250874054075591789781264330331690]
    _sum = str(sum(nums))
    return int(_sum[:10])


def problem14():
    # Which starting number, under one million, produces the longest chain with Collatz problem
    maximum = 10**6
    for i in xrange(1, maximum):
        try:
            collatz[i]
        except KeyError:
            get_collatz(i)
    return max([i for i in xrange(1, maximum)], key=lambda n: collatz[n])


def problem15():
    # Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are
    # exactly 6 routes to the bottom right corner. How many such routes are there through a 20x20 grid?
    return ncr(2 * 20, 20)


def problem16():
    # What is the sum of the digits of the number 2**1000?
    return sum_of_digits(2**1000)


def problem17():
    # If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    # how many letters would be used?
    return sum([len(number_to_string(i)) for i in xrange(1, 1001)])


def problem18():
    # Find the maximum total from top to bottom of the triangle in the p018_triangle.txt file
    return max_path_sum("files/p018_triangle.txt")


def problem19():
    # A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    # How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    l = sum(days)
    days_2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    l_2 = sum(days_2)
    first_days = set([1 + sum(days[:i]) for i in xrange(12)])
    first_days_2 = set([1 + sum(days_2[:i]) for i in xrange(12)])
    next_year_first_sunday = 7
    counter = 0
    for i in xrange(1900, 2001):
        if i % 4 == 0 and i != 1900:  # szokoev
            sundays = [next_year_first_sunday + j for j in xrange(0, l_2-next_year_first_sunday+1, 7)]
            next_year_first_sunday = sundays[-1] + 7 - l_2
            counter += len(first_days_2 & set(sundays))
        else:
            sundays = [next_year_first_sunday + j for j in xrange(0, l-next_year_first_sunday+1, 7)]
            next_year_first_sunday = sundays[-1] + 7 - l
            if not i == 1900:
                counter += len(first_days & set(sundays))
    return counter


def problem20():
    # Find the sum of the digits in the number 100!
    return sum_of_digits(factorial(100))


def problem21():
    # Evaluate the sum of all the amicable numbers under 10000.
    return sum([i if is_amicable(i) else 0 for i in xrange(0, 10001)])


def problem22():
    # Using p022_names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
    # first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
    # multiply this value by its alphabetical position in the list to obtain a name score.
    # For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
    # the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
    # What is the total of all the name scores in the file?
    def score_of_name(name, scores):
        score = 0
        for j in name:
            score += scores.index(j.lower())
        score *= names.index(name) + 1
        return score

    alphabet = ["\"", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z"]
    with open("files/p022_names.txt") as f:
        line = f.read()
        names = line.split(",")
    names.sort()
    s = 0
    for i in names:
        s += score_of_name(i, alphabet)
    return s


def problem23():
    # Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    abundant = list()
    result = set()
    for i in xrange(1, 28124):
        if not is_num_sum_of_two_in_list(i, abundant, False):
            result.add(i)
        if is_abundant_num(i):
            abundant.append(i)
    return sum(result)


def problem24():
    # The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
    # What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    from itertools import permutations
    return int("".join(list(permutations("0123456789"))[10**6-1]))


def problem25():
    # What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    f = [1, 1]
    while len(str(f[-1])) < 1000:
        f.append(f[-1]+f[-2])
    return len(f)


def problem26():
    # Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    lengths = [0]
    for i in xrange(1, 1001):
        lengths.append(length_of_recurring_cycle(i))
    return lengths.index(max(lengths))


def problem27():
    # Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
    # primes for consecutive values of n, starting with n = 0.
    quadratic_expression = lambda a, b: lambda n: n**2 + a*n + b
    maximum = 0
    product = 0
    for i in xrange(-1000, 1001):
        for j in xrange(-1000, 1001):
            k = 0
            while Primes._is_prime(quadratic_expression(i, j)(k)):
                k += 1
            if k > maximum:
                maximum = k
                product = i*j
    return product


def problem28():
    #
    _sum = 1
    counter = 1
    size = 1001
    for i in xrange(1, size/2+1):
        counter += i*2
        _sum += counter
        counter += i*2
        _sum += counter
        counter += i*2
        _sum += counter
        counter += i*2
        _sum += counter
    return _sum


def problem29():
    # How many distinct terms are in the sequence generated by ab for 2 <= a <= 100 and 2 <= b <= 100?
    s = set()
    for i in xrange(2, 101):
        for j in xrange(2, 101):
            s.add(i**j)
    return len(s)


def problem30():
    # Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
    _sum = 0
    for i in xrange(3, 1000000):
        fact_sum = sum_of_digits(i, lambda n: n**5)
        if i == fact_sum:
            _sum += fact_sum
    return _sum


def problem31():
    # How many different ways can 200p be made using any number of coins?
    # coins: 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p
    possibilities = 0
    for i in xrange(0, 201):
        for j in xrange(0, 201, 2):
            if i+j >200:
                break
            for k in xrange(0, 201, 5):
                if i+j+k > 200:
                    break
                for l in xrange(0, 201, 10):
                    if i+j+k+l > 200:
                        break
                    for m in xrange(0, 201, 20):
                        if i+j+k+l+m > 200:
                            break
                        for n in xrange(0, 201, 50):
                            if i+j+k+l+m+n > 200:
                                break
                            for o in xrange(0, 201, 100):
                                if i+j+k+l+m+n+o > 200:
                                    break
                                for p in xrange(0, 201, 200):
                                    if i+j+k+l+m+n+o+p == 200:
                                        possibilities += 1
    return possibilities


def problem32():
    # Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
    # 1 through 9 pandigital.
    _sum = set()
    for i in xrange(10):
        for j in xrange(1001, 10000):
            prod = i*j
            if is_pandigital(str(i)+str(j)+str(prod), 9):
                _sum.add(prod)
    for i in xrange(11, 100):
        for j in xrange(101, 1000):
            prod = i*j
            if is_pandigital(str(i)+str(j)+str(prod), 9):
                _sum.add(prod)
    return sum(_sum)


def problem33():
    # The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
    # incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
    # We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    # There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
    # digits in the numerator and denominator.
    # If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    import fractions
    fv = lambda x, y: float(str(x)[1]) if str(x)[0] == y else float(str(x)[0])
    __i = 1
    __j = 1
    for i in xrange(10, 100):
        for j in xrange(i+1, 100):
            _i = set(str(i))
            _j = set(str(j))
            if len(_i) != 2:
                continue
            if len(_j) != 2:
                continue
            _set = _i & _j
            if len(_set) == 1:
                common = _set.pop()
                try:
                    if i/float(j) == fv(i, common)/fv(j, common) and common != '0':
                        __i *= i
                        __j *= j
                except ZeroDivisionError:
                    pass
    return __j/fractions.gcd(__i, __j)


def problem34():
    # Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return sum([i if i == sum_of_digits(i, lambda n: factorials[n]) else 0 for i in xrange(3, 10000000)])


def problem35():
    # How many circular primes are there below one million?
    circ_primes = set([])
    prime_obj = Primes(10**6)
    for i in prime_obj.get_primes():
        if i in circ_primes:
            continue
        temp_set = circ_number(i)
        if all(prime_obj.is_prime(j) for j in temp_set):
            circ_primes |= temp_set
    return len(circ_primes)


def problem36():
    # Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    _sum = 0
    decimal_palindromes = []
    for i in xrange(1, 1000000, 2):
        if is_palindrome(i):
            decimal_palindromes.append(i)
    for i in decimal_palindromes:
        if is_palindrome(dec_to_bin((i))):
            _sum += i
    return _sum


def problem37():
    # Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    prime_obj = Primes(1000000)
    truncatable_primes = set([])
    i = 11
    while len(truncatable_primes) != 11:
        prime = i
        if not prime_obj.is_prime(prime):
            i += 2
            continue
        if prime_obj.is_truncatable_prime(prime):
            truncatable_primes.add(prime)
        i += 2
    return sum(truncatable_primes)


def problem38():
    # What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
    # with (1,2, ... , n) where n > 1?
    possible_nums = [int("9" + str(x)) for x in xrange(1, 1000)] + [int("90" + str(x)) for x in xrange(1, 100)] + \
                    [int("900" + str(x)) for x in xrange(1, 10)]
    possible_tuples = [(1, 2), (1, 2, 3), (1, 2, 3, 4), (1, 2, 3, 4, 5)]
    max_value = 0
    for i in possible_nums:
        for j in possible_tuples:
            act_value = num_x_tupli(i, j)
            if is_pandigital(act_value, 9):
                if max_value < act_value:
                    max_value = act_value
    return max_value


def problem39():
    # If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
    # solutions for p = 120.
    # {20,48,52}, {24,45,51}, {30,40,50}
    # For which value of p <= 1000, is the number of solutions maximised?
    _map = [0]*1001
    for i in xrange(1000):
        for j in xrange(i):
            for k in xrange(j):
                if j**2 + k**2 == i**2 and i+j+k <= 1000:
                    _map[j+k+i] += 1
    return _map.index(sorted(_map)[-1])


def problem40():
    # An irrational decimal fraction is created by concatenating the positive integers:
    # 0.123456789101112131415161718192021...
    # It can be seen that the 12th digit of the fractional part is 1.
    # If dn represents the nth digit of the fractional part, find the value of the following expression.
    # d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
    milestones = [10**i-1 for i in xrange(0, 7)]
    num_length = 0
    str_num = ""
    i = 1
    while num_length < 1000000:
        str_num += str(i)
        num_length += num_len(i)
        i += 1
    return prod([int(str_num[i]) for i in milestones])


def problem41():
    # What is the largest n-digit pandigital prime that exists?
    lst = []
    for i in xrange(2, 10):
        lst += permutations(default_pandigital(i))
    for i in range(len(lst)-1, -1, -1):
        if Primes._is_prime(int(lst[i])):
            return int(lst[i])


def problem42():
    # nth triangle num: 0.5*x*(x-1)
    # the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
    # By converting each letter in a word to a number corresponding to its alphabetical position and adding these
    # values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
    # is a triangle number then we shall call the word a triangle word.
    # Using words.txt a 16K text file containing nearly two-thousand common English words, how many are triangle words?
    with open("files/p042_words.txt") as f:
        line = f.read()
        words = [i.strip("\"") for i in line.split(",")]
    triangle_word_count = 0
    for j in words:
        if is_triangle_word(j):
            triangle_word_count += 1
    return triangle_word_count


def problem43():
    # Find the sum of all 0 to 9 pandigital numbers with the property described in
    # https://projecteuler.net/problem=43
    condition = lambda i: int(i[1:4]) % 2 == 0 and \
                          int(i[2:5]) % 3 == 0 and \
                          int(i[3:6]) % 5 == 0 and \
                          int(i[4:7]) % 7 == 0 and \
                          int(i[5:8]) % 11 == 0 and \
                          int(i[6:9]) % 13 == 0 and \
                          int(i[7:10]) % 17 == 0
    perm = permutations("1023456789")
    chosen_ones = []
    for i in perm:
        if num_len(int(i)) == 10:
            if condition(i):
                chosen_ones.append(int(i))
    return sum(chosen_ones)


def problem67():
    # Find the maximum total from top to bottom of the triangle in the p067_triangle.txt file
    return max_path_sum("files/p067_triangle.txt")

if __name__ == "__main__":
    pass