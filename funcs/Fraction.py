import divisors
import common

class Fraction:
    def __init__(self, x, y=1):
        self.x = x
        self.y = y

    def get(self):
        _gcd = divisors.gcd(self.x, self.y)
        return int(self.x/_gcd), int(self.y/_gcd)

    def get_value(self):
        return self.x/float(self.y)

    def is_int(self):
        return self.x % self.y == 0

    def __mul__(self, other):
        return Fraction(other.x*self.x, other.y*self.y)

    def __div__(self, other):
        return Fraction(other.y*self.x, other.x*self.y)

    def __add__(self, other):
        denominator = divisors.lcm(other.y, self.y)
        numerator = other.x*(denominator/other.y) + self.x*(denominator/self.y)
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        denominator = divisors.lcm(other.y, self.y)
        numerator = self.x*(denominator/self.y) - other.x*(denominator/other.y)
        return Fraction(numerator, denominator)

    def __pow__(self, n):
        return common.prod([self]*n)
    def __lt__(self, other):  # self < other
        denominator = divisors.lcm(other.y, self.y)
        return other.x*(denominator/other.y) > self.x*(denominator/self.y)

    def __le__(self, other):  # self <= other
        denominator = divisors.lcm(other.y, self.y)
        return other.x*(denominator/other.y) >= self.x*(denominator/self.y)

    def __eq__(self, other):  # self == other
        return self.get() == other.get()

    def __ne__(self, other):  # self != other
        return self.get() != other.get()

    def __ge__(self, other):  # self >= other
        denominator = divisors.lcm(other.y, self.y)
        return other.x*(denominator/other.y) <= self.x*(denominator/self.y)

    def __gt__(self, other):  # self > other
        denominator = divisors.lcm(other.y, self.y)
        return other.x*(denominator/other.y) < self.x*(denominator/self.y)

    def __str__(self):
        tupli = self.get()
        return "{0}/{1}".format(tupli[0], tupli[1])

    @staticmethod
    def infinite_fraction(x, y, max_iter=-1, iteration=0):
        """
        :param x: integer, numerator
        :param y: integer, denominator
        :param max_iter: integer, how many iteration is allowed
        :param iteration: integer, current iteration
        :return: Fraction
        """
        if max_iter == -1:
            max_iter = len(y)
        if max_iter == 0:
            return Fraction(x)
        if iteration == 0:
            return Fraction(x)+Fraction(1)/Fraction.infinite_fraction(x, y, max_iter, iteration+1)
        if iteration == max_iter:
            return Fraction(y[(iteration-1) % len(y)])
        else:
            return Fraction(y[(iteration-1) % len(y)])+Fraction(1)/Fraction.infinite_fraction(x, y, max_iter, iteration+1)
