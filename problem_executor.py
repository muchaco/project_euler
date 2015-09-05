__author__ = 'muchaco'

from unittest import TestCase
import math
from time import time


class UnitTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(UnitTest, self).__init__(*args, **kwargs)

    def test_sum_of_multiples(self):
        self.assertEquals(sum_of_multiples([3, 5], 10), 23)
        self.assertEquals(sum_of_multiples([3, 5], 1000), 233168)

    def test_ith_fibonacci(self):
        self.assertEquals(ith_fibonacci(1), 1)
        self.assertEquals(ith_fibonacci(2), 1)
        self.assertEquals(ith_fibonacci(3), 2)
        self.assertEquals(ith_fibonacci(10), 55)

    def test_prime_factors(self):
        self.assertEquals(set_prime_factors_of(13195), {5, 7, 13, 29})
        #self.assertEquals(dict_prime_factors_of(235432125), {59: 1, 3: 2, 5: 3, 3547: 1})

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(9009), True)
        self.assertFalse(is_palindrome(9008), False)
        self.assertTrue(is_palindrome(1), True)

    def test_is_prime(self):
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(41))

    def test_num_of_divisors(self):
        self.assertEquals(num_of_divisors(15, True), 4)
        self.assertEquals(num_of_divisors(10, True), 4)
        self.assertEquals(num_of_divisors(28, True), 6)
        self.assertEquals(num_of_divisors(28, False), 5)

    def test_sum_of_divisors(self):
        self.assertEquals(sum_of_divisors(15, True), 24)
        self.assertEquals(sum_of_divisors(15, False), 9)
        self.assertEquals(sum_of_divisors(10, True), 18)
        self.assertEquals(sum_of_divisors(28, True), 56)
        self.assertEquals(sum_of_divisors(28, False), 28)

    def test_sum_of_digits(self):
        self.assertEquals(sum_of_digits(12), 3)
        self.assertEquals(sum_of_digits(123), 6)
        self.assertEquals(sum_of_digits(1234), 10)
        self.assertEquals(sum_of_digits(555112002310), 25)

    def test_write_down_number(self):
        self.assertEquals(len(number_to_string(2)), 3)
        self.assertEquals(len(number_to_string(11)), 6)
        self.assertEquals(len(number_to_string(17)), 9)
        self.assertEquals(len(number_to_string(20)), 6)
        self.assertEquals(len(number_to_string(36)), 9)
        self.assertEquals(len(number_to_string(47)), 10)
        self.assertEquals(len(number_to_string(100)), len("onehundred"))
        self.assertEquals(len(number_to_string(342)), 23)
        self.assertEquals(len(number_to_string(115)), 20)


def sum_of_multiples(list_of_bases, max_number):
    my_set = set()
    for j in list_of_bases:
        my_set = my_set.union(set([i for i in xrange(max_number) if i % j == 0]))
    return sum(my_set)


def ith_fibonacci(i):
    nums = [1, 1]
    while len(nums) < i:
        nums.append(nums[-1]+nums[-2])
    return nums[i-1]


def set_prime_factors_of(number):
    factors = set()
    i = 2
    while number != 1:
        while number % i == 0:
            factors.add(i)
            number /= i
        i += 1
    return factors

is_palindrome = lambda word: str(word) == str(word)[::-1]


def ith_prime(number):
    primes = [2]
    while len(primes) < number:
        primes.append(next_prime(primes[-1]))
    return primes[-1]


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def next_prime(number):
    number += 1
    while not is_prime(number):
        number += 1
    return number


def atlo1(a, b, matrix):
    try:
        return matrix[a][b] * matrix[a+1][b-1] * matrix[a+2][b-2] * matrix[a+3][b-3]
    except IndexError:
        return 0


def atlo2(a, b, matrix):
    try:
        return matrix[a][b] * matrix[a+1][b+1] * matrix[a+2][b+2] * matrix[a+3][b+3]
    except IndexError:
        return 0


def lefele(a, b, matrix):
    try:
        return matrix[a][b] * matrix[a+1][b] * matrix[a+2][b] * matrix[a+3][b]
    except IndexError:
        return 0


def oldal(a, b, matrix):
    try:
        return matrix[a][b] * matrix[a][b+1] * matrix[a][b+2] * matrix[a][b+3]
    except IndexError:
        return 0


def start_from(a, b, matrix):
    return max([oldal(a, b, matrix), atlo1(a, b, matrix), atlo2(a, b, matrix), lefele(a, b, matrix)])


def divisors(n, include_self):
    _set = {1}
    if include_self:
        _set.add(n)
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            j = n/i
            if j < i:
                break
            else:
                _set |= {i, j}
    return _set

sum_of_divisors = lambda n, b: sum(divisors(n, b))
num_of_divisors = lambda n, b: len(divisors(n, b))
next_collatz = lambda num: num / 2 if num % 2 == 0 else 3 * num + 1
collatz = {1: 1}


def get_collatz(num):
    nn = next_collatz(num)
    try:
        collatz[num] = collatz[nn] + 1
    except KeyError:
        get_collatz(next_collatz(num))
        collatz[num] = collatz[nn] + 1


def greatest_product_in(number, length):
    i = 0
    prods = []
    while i + length <= len(number):
        akt_num = number[i:i + length]
        prod = 1
        for j in akt_num:
            prod *= int(j)
        prods.append(prod)
        i += 1
    return max(prods)

sum_of_digits = lambda n: sum([int(i) for i in str(n)])


def number_to_string(number):
    numbers = ["null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers_teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen"]
    numbers_10 = ["null", "teen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                  "hundred"]
    str_num = str(number)
    if len(str_num) < 2:
        return numbers[number]
    if len(str_num) < 3:
        if str_num[0] == "1":
            if number < 19:
                return numbers_teen[number-10]
            return numbers[number-10] + numbers_10[int(str_num[0])]
        if str_num[1] == "0":
            return numbers_10[int(str_num[0])]
        return numbers_10[int(str_num[0])] + numbers[int(str_num[1])]
    if len(str_num) < 4:
        if int(str_num[1:]) == 0:
            return numbers[int(str_num[0])] + "hundred"
        return numbers[int(str_num[0])] + "hundredand" + number_to_string(int(str(number)[1:]))
    return "onethousand"


def ncr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

is_amicable = lambda n: sum_of_divisors(sum_of_divisors(n, False), False) == n and sum_of_divisors(n, False) != n

is_abundant_num = lambda i: sum_of_divisors(i, False) > i
is_perfect_num = lambda i: sum_of_divisors(i, False) == i
is_deficient_num = lambda i: sum_of_divisors(i, False) < i


def is_num_sum_of_two_in_list(n, lst):
    lst.sort()
    length = len(lst)
    if length < 2:
        return False
    i = 0
    j = length-1
    while j != i:
        actual_sum = lst[i] + lst[j]
        if actual_sum == n:
            return True
        elif actual_sum > n:
            j -= 1
        else:
            i += 1
    return False

missing = {5, 6, 10, 20}


def problem1():
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    # multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    return str(sum_of_multiples([3, 5], 10))


def problem2():
    # Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
    # the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci
    # sequence whose values do not exceed four million, find the sum of the even-valued terms.
    fib = [1, 2]
    while fib[-1] < 4000000:
        fib.append(fib[-1]+fib[-2])
    fib = [i for i in fib if i % 2 == 0]
    return str(sum(fib))


def problem3():
    # The prime factors of 13195 are 5, 7, 13 and 29.
    # What is the largest prime factor of the number 600851475143 ?
    return str(max(set_prime_factors_of(600851475143)))


def problem4():
    # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    # is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.
    palindromes = []
    for i in xrange(10**3-1, 10**(3-1)-1, -1):
        for j in xrange(10**3-1, i-1, -1):
            if is_palindrome(i*j):
                palindromes.append(i*j)
    return str(max(palindromes))


def problem7():
    # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    # What is the 10001st prime number?
    return str(ith_prime(10001))


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
    return str(greatest_product_in(number, 13))


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
                        return str(a*b*c)


def problem11():
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
    return str(max([start_from(i, j, matrix) for i in xrange(20) for j in xrange(20)]))


def problem12():
    # The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
    # 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    # What is the value of the first triangle number to have over five hundred divisors?
    over = 500
    triangle_nums = [1]
    while num_of_divisors(triangle_nums[-1], True) < over + 1:
        triangle_nums.append(triangle_nums[-1] + len(triangle_nums) + 1)
    return str(triangle_nums[-1])


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
    return _sum[:11]


def problem14():
    # Which starting number, under one million, produces the longest chain with Collatz problem
    maximum = 10**6
    for i in xrange(1, maximum):
        try:
            collatz[i]
        except KeyError:
            get_collatz(i)
    return str(max([i for i in xrange(1, maximum)], key=lambda n: collatz[n]))


def problem15():
    # Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are
    # exactly 6 routes to the bottom right corner. How many such routes are there through a 20x20 grid?
    return str(ncr(2 * 20, 20))


def problem16():
    # What is the sum of the digits of the number 2**1000?
    return str(sum_of_digits(2**1000))


def problem17():
    # If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    # how many letters would be used?
    return str(sum([len(number_to_string(i)) for i in xrange(1, 1001)]))


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
    return str(counter)


def problem21():
    return str(sum([i if is_amicable(i) else 0 for i in xrange(0, 10001)]))


def problem22():
    def score_of_name(name, scores):
        score = 0
        for j in name:
            score += scores.index(j.lower())
        score *= names.index(name) + 1
        return score

    alphabet = ["\"", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z"]
    with open("names.txt") as f:
        line = f.read()
        names = line.split(",")
    names.sort()
    s = 0
    for i in names:
        s += score_of_name(i, alphabet)
    return str(s)


def problem23():
    abundant = list()
    lst = list()
    for i in xrange(1, 28124):
        if not is_num_sum_of_two_in_list(i, abundant):
            lst.append(i)
        if is_abundant_num(i):
            abundant.append(i)
    return str(sum(lst))


def problem24():
    # The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
    # What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    from itertools import permutations
    return str(list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[10**6-1])


def problem25():
    # What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    f = [1, 1]
    while len(str(f[-1])) < 1000:
        f.append(f[-1]+f[-2])
    return str(len(f))


def execute_problem(ith):
    if ith in missing:
        print "This problem isn't solved yet"
        return
    t0 = time()
    print "The answer is:   " + globals()['problem' + str(ith)]()
    print "Execution time:  " + str(time() - t0) + " sec"

if __name__ == "__main__":
    execute_problem(24)