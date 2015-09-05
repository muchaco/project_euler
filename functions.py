__author__ = 'muchaco'

import math

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


def max_path_sum(file):
    with open(file) as f:
        adj = f.read().split("\n")
        adj = [[int(j) for j in i.split(" ")] + [0] for i in adj]
    # parse_triangle(input, adj)
    for i in xrange(1, len(adj)):
        for j in xrange(i+1):
            adj[i][j] += max(adj[i-1][j], adj[i-1][j-1])
    return str(max(adj[len(adj)-1]))

if __name__ == "__main__":
    pass