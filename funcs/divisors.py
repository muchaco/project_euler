import math
from Primes import Primes


def divisors(n, include_self):
    """
    :param n: integer
    :param include_self: boolean
    :return: a set of n's divisors
    """
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
is_amicable = lambda n: sum_of_divisors(sum_of_divisors(n, False), False) == n and sum_of_divisors(n, False) != n
is_abundant_num = lambda i: sum_of_divisors(i, False) > i
is_perfect_num = lambda i: sum_of_divisors(i, False) == i
is_deficient_num = lambda i: sum_of_divisors(i, False) < i


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    _lcm = (x*y) / gcd(x, y)
    return _lcm


def gcd_of_list(nums):
    lst = list()
    factors = {}
    for i in nums:
        lst.append(Primes.dict_prime_factors_of(i))
    final_factors = set(lst[0].keys())
    for i in lst:
        final_factors = final_factors & set(i.keys())
    for i in lst:
        for j in final_factors:
            try:
                if factors[j] > i[j]:
                    factors[j] = i[j]
            except KeyError:
                factors[j] = i[j]
    product = 1
    for i in factors.keys():
        product *= i ** factors[i]
    return product


def lcm_of_list(nums):
    lst = list()
    final_factors = {}
    for i in nums:
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
        product *= i ** final_factors[i]
    return product