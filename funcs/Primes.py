import math
from funcs import common

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

    def is_prime(self, n, strict=False):
        if n >= self.length:
            if strict:
                return False
            return Primes.static_is_prime(n)
        if not common.is_integer(n):
            return False
        return self.sieve[int(n)]

    def next_prime(self, n):
        if n >= self.length:
            return Primes.static_next_prime(n)
        i = n
        while self.sieve[i] == 0:
            if i >= self.length:
                return Primes.static_next_prime(i)
            i += 1
        return i

    def get_primes(self):
        return self.primes

    def ith_prime(self, i):
        try:
            return self.primes[i]
        except IndexError:
            return Primes.static_ith_prime(i)

    def is_all_prime(self, num_list):
        return all(self.is_prime(j) for j in num_list)

    def is_truncatable_prime(self, prime):
        return self.is_all_prime(common.make_truncatable_list(prime))

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
        if number < 0:
            number *= -1
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
    def static_is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in xrange(3, int(math.sqrt(n)) + 1, 2))

    @staticmethod
    def static_next_prime(number):
        number += 1
        while not Primes.static_is_prime(number):
            number += 1
        return number

    @staticmethod
    def static_ith_prime(number):
        primes = [2]
        while len(primes) < number:
            primes.append(Primes.static_next_prime(primes[-1]))
        return primes[-1]

    @staticmethod
    def static_is_all_prime(num_list):
        return all(Primes.is_prime(j) for j in num_list)

    @staticmethod
    def static_is_truncatable_prime(prime):
        return Primes.static_is_all_prime(common.make_truncatable_list(prime))