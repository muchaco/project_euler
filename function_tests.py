__author__ = 'muchaco'

from unittest import TestCase
from functions import *


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
        self.assertEquals(Primes.set_prime_factors_of(13195), {5, 7, 13, 29})

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(9009), True)
        self.assertFalse(is_palindrome(9008), False)
        self.assertTrue(is_palindrome(1), True)

    def test_is_prime(self):
        self.assertFalse(Primes._is_prime(9))
        self.assertFalse(Primes._is_prime(4))
        self.assertTrue(Primes._is_prime(2))
        self.assertTrue(Primes._is_prime(23))
        self.assertTrue(Primes._is_prime(41))

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
        self.assertEquals(sum_of_divisors(6, False), 6)
        self.assertEquals(sum_of_divisors(4, False), 3)
        self.assertEquals(sum_of_divisors(12, False), 16)

    def test_sum_of_digits(self):
        self.assertEquals(sum_of_digits(12), 3)
        self.assertEquals(sum_of_digits(123), 6)
        self.assertEquals(sum_of_digits(1234), 10)
        self.assertEquals(sum_of_digits(555112002310), 25)
        self.assertEquals(sum_of_digits(1634, lambda n: n**4), 1634)
        self.assertEquals(sum_of_digits(8208, lambda n: n**4), 8208)
        self.assertEquals(sum_of_digits(9474, lambda n: n**4), 9474)
        self.assertEquals(sum_of_digits(145, factorial), 145)

    def test_circ_number(self):
        self.assertEquals(circ_number(145), {145, 451, 514})
        self.assertEquals(circ_number(1456), {1456, 4561, 5614, 6145})
        self.assertEquals(circ_number(14541), {14541, 45411, 54114, 41145, 11454})
        self.assertEquals(circ_number(11), {11})

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

    def test_is_num_sum_of_two_in_list(self):
        self.assertTrue(is_num_sum_of_two_in_list(5, [1, 3, 4]))
        self.assertFalse(is_num_sum_of_two_in_list(12, [1, 3, 4]))
        self.assertTrue(is_num_sum_of_two_in_list(100, [50, 25, 25, 50]))
        self.assertFalse(is_num_sum_of_two_in_list(100, [50, 25, 25]))
        self.assertFalse(is_num_sum_of_two_in_list(2, [1, 2, 3]))
        self.assertFalse(is_num_sum_of_two_in_list(2, [1, 2, 3, 3, -2]))
        self.assertTrue(is_num_sum_of_two_in_list(5, [1, 1, 1, 1, 4, 3]))
        self.assertTrue(is_num_sum_of_two_in_list(32, [10, 3, 4, 10, 8, 8, 76, 9, 12, 22, 23, 26]))

    def test_dict_prime_factors_of(self):
        self.assertEquals(Primes.dict_prime_factors_of(34), {2: 1, 17: 1})
        self.assertEquals(Primes.dict_prime_factors_of(35), {5: 1, 7: 1})
        self.assertEquals(Primes.dict_prime_factors_of(350), {2: 1, 5: 2, 7: 1})
        self.assertEquals(Primes.dict_prime_factors_of(235432125), {59: 1, 3: 2, 5: 3, 3547: 1})

    def test_factorial(self):
        self.assertEquals(factorial(5), 120)
        self.assertEquals(factorial(32), 263130836933693530167218012160000000)
        self.assertEquals(factorial(1), 1)

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(123456789, 9))
        self.assertFalse(is_pandigital(123456709, 9))
        self.assertFalse(is_pandigital(823431388, 9))
        self.assertFalse(is_pandigital(8234313, 9))
        self.assertFalse(is_pandigital(112233445566778899, 9))
        self.assertTrue(is_pandigital(12345, 5))

if __name__ == "__main__":
    pass