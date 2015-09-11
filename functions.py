__author__ = 'muchaco'

import math
import itertools

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


is_palindrome = lambda word: str(word) == str(word)[::-1]


def start_from(a, b, matrix):
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
    return max([oldal(a, b, matrix), atlo1(a, b, matrix), atlo2(a, b, matrix), lefele(a, b, matrix)])


def divisors(n, include_self):
    _set = {1}
    if include_self:
        _set.add(n)
    for i in xrange(2, int(math.sqrt(n)) + 1):
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

sum_of_digits = lambda n, j = lambda k: k: sum([j(int(i)) for i in str(n)])


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


def is_num_sum_of_two_in_list(n, lst, distinct_values=True):
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
    if not distinct_values:
        actual_sum = lst[i] + lst[j]
        if actual_sum == n:
            return True
    return False


def max_path_sum(file_name):
    with open(file_name) as f:
        adj = f.read().split("\n")
        adj = [[int(j) for j in i.split(" ")] + [0] for i in adj]
    # parse_triangle(input, adj)
    for i in xrange(1, len(adj)):
        for j in xrange(i+1):
            adj[i][j] += max(adj[i-1][j], adj[i-1][j-1])
    return max(adj[len(adj)-1])


factorial = lambda n: n * factorial(n-1) if n > 1 else n


def index_of(a, x):
    try:
        return a.index(x)
    except ValueError:
        return 0


def length_of_recurring_cycle(i):
    remainders = list([0])
    rem = 1
    while not index_of(remainders, rem):
        remainders.append(rem)
        rem = rem*10 % i
        if rem == 0:
            return 0
    return len(remainders)-index_of(remainders, rem)


def is_pandigital(a, b, include_null = False):
    _str = str(a)
    reference = default_pandigital(b, include_null)
    if len(_str) != len(reference):
        return False
    if set(_str) & set(reference) != set(reference):
        return False
    return True


def default_pandigital(n, include_null = False):
    if include_null:
        string = "0"
    else:
        string = ""
    for i in xrange(1, n+1):
        string += str(i)
    return string

strstr = lambda haystack, needle: False if haystack.upper().find(needle.upper()) < 0 else True


def permutations(head, tail=''):
    lst = []
    if len(head) == 0:
        lst.append(tail)
    else:
        for i in range(len(head)):
            lst += permutations(head[0:i] + head[i+1:], tail+head[i])
    return lst


def circ_number(num):
    circulars = set()
    str_num = str(num)
    circulars.add(num)
    for i in xrange(len(str_num)):
        str_num = str_num[1:] + str_num[0]
        circulars.add(int(str_num))
    return circulars

dec_to_bin = lambda x: dec_to_bin(x / 2) + str(x % 2) if x / 2 >= 1 else str(1)


def make_truncatable_list(num):
    tr_list = set([])
    str_num = str(num)
    for i in xrange(len(str_num)):
        tr_list.add(int(str_num[i:]))
        tr_list.add(int(str_num[:i+1]))
    return list(tr_list)


def num_x_tupli(number, tupli):
    product = ""
    for i in tupli:
        product += str(number * i)
    return int(product)

num_len = lambda n: int(math.log10(n))+1 if n != 0 else 1


def prod(lst):
    ret_val = 1
    for i in lst:
        ret_val *= i
    return ret_val


def word_value(word):
    alphabet = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z"]
    return sum([alphabet.index(i.lower()) for i in word])


nth_triangle_num = lambda x: 0.5*x*(x-1)


def is_triangle_word(word):
    num = word_value(word)
    n = 1
    last_triangle_number = 0
    while last_triangle_number < num:
        last_triangle_number = int(nth_triangle_num(n))
        n += 1
    return last_triangle_number == num


# TODO: create module tests
def power_mod(a, b, modulus):
    pow_remainders = [a]
    bin_b = dec_to_bin(b)
    len_b = len(bin_b)
    for i in xrange(1, len_b):
        pow_remainders.append((pow_remainders[i-1] ** 2) % modulus)
    prod = 1
    for i in xrange(len_b):
        if bin_b[i] == '1':
            prod *= (pow_remainders[len_b-i-1]) % modulus
    return prod % modulus


def varieties(a, b):
    for i in str(b):
        if i not in str(a):
            return False
    for i in str(a):
        if i not in str(b):
            return False
    return True


class Primes:
    def __init__(self, length):
        self.sieve = [1]*length
        self.primes = list()
        self.length = length
        self.sieve[0], self.sieve[1] = 0, 0
        for i in xrange(2, length/2+1):
            if self.sieve[i] == 0:
                continue
            for j in xrange(i*2, length, i):
                self.sieve[j] = 0
        for i in range(2, length):
            if self.sieve[i]:
                self.primes.append(i)


    def is_prime(self, n):
        if n >= self.length:
            return Primes._is_prime(n)
        return self.sieve[n]

    def next_prime(self, n):
        if n >= self.length:
            return Primes._next_prime(n)
        i = n
        while self.sieve[i] == 0:
            if i >= self.length:
                return Primes._next_prime(i)
            i += 1
        return i

    def get_primes(self):
        return self.primes

    def ith_prime(self, i):
        try:
            return self.primes[i]
        except IndexError:
            return Primes._ith_prime(i)

    def is_all_prime(self, num_list):
        return all(self.is_prime(j) for j in num_list)

    def is_truncatable_prime(self, prime):
        return self.is_all_prime(make_truncatable_list(prime))

    @staticmethod
    def set_prime_factors_of(number):
        factors = set()
        i = 2
        while number != 1:
            while number % i == 0:
                factors.add(i)
                number /= i
            i += 1
        return factors

    @staticmethod
    def dict_prime_factors_of(number):
        factors = {}
        i = 2
        while number != 1:
            while number % i == 0:
                try:
                    factors[i] += 1
                except KeyError:
                    factors[i] = 1
                number /= i
            i += 1
        return factors

    @staticmethod
    def _is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in xrange(3, int(math.sqrt(n)) + 1, 2))

    @staticmethod
    def _next_prime(number):
        number += 1
        while not Primes._is_prime(number):
            number += 1
        return number

    @staticmethod
    def _ith_prime(number):
        primes = [2]
        while len(primes) < number:
            primes.append(Primes._next_prime(primes[-1]))
        return primes[-1]

    @staticmethod
    def _is_all_prime(num_list):
        return all(Primes.is_prime(j) for j in num_list)

    @staticmethod
    def _is_truncatable_prime(prime):
        return Primes._is_all_prime(make_truncatable_list(prime))


if __name__ == "__main__":
    pass