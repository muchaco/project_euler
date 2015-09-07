__author__ = 'muchaco'

from unittest import TestCase
from problems import *


class UnitTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(UnitTest, self).__init__(*args, **kwargs)

    def test_problem001(self):
        self.assertEquals(problem1(), 233168)
    def test_problem002(self):
        self.assertEquals(problem2(), 4613732)
    def test_problem003(self):
        self.assertEquals(problem3(), 6857)
    def test_problem004(self):
        self.assertEquals(problem4(), 906609)
    def test_problem005(self):
        self.assertEquals(problem5(), 232792560)
    def test_problem006(self):
        self.assertEquals(problem6(), 25164150)
    def test_problem007(self):
        self.assertEquals(problem7(), 104743)
    def test_problem008(self):
        self.assertEquals(problem8(), 23514624000)
    def test_problem009(self):
        self.assertEquals(problem9(), 31875000)
    def test_problem010(self):
        self.assertEquals(problem10(), 142913828922)
    def test_problem011(self):
        self.assertEquals(problem11(), 70600674)
    def test_problem012(self):
        self.assertEquals(problem12(), 76576500)
    def test_problem013(self):
        self.assertEquals(problem13(), 5537376230)
    def test_problem014(self):
        self.assertEquals(problem14(), 837799)
    def test_problem015(self):
        self.assertEquals(problem15(), 137846528820)
    def test_problem016(self):
        self.assertEquals(problem16(), 1366)
    def test_problem017(self):
        self.assertEquals(problem17(), 21124)
    def test_problem018(self):
        self.assertEquals(problem18(), 1074)
    def test_problem019(self):
        self.assertEquals(problem19(), 171)
    def test_problem020(self):
        self.assertEquals(problem20(), 648)
    def test_problem021(self):
        self.assertEquals(problem21(), 31626)
    def test_problem022(self):
        self.assertEquals(problem22(), 871198282)
    def test_problem023(self):
        self.assertEquals(problem23(), 4179871)
    def test_problem024(self):
        self.assertEquals(problem24(), 2783915460)
    def test_problem025(self):
        self.assertEquals(problem25(), 4782)
    def test_problem026(self):
        self.assertEquals(problem26(), 983)
    def test_problem027(self):
        self.assertEquals(problem27(), -59231)
    def test_problem028(self):
        self.assertEquals(problem28(), 669171001)
    def test_problem029(self):
        self.assertEquals(problem29(), 9183)
    def test_problem030(self):
        self.assertEquals(problem30(), 443839)
    def test_problem031(self):
        self.assertEquals(problem31(), 73682)
    def test_problem032(self):
        self.assertEquals(problem32(), 45228)
    def test_problem033(self):
        self.assertEquals(problem33(), 100)
    def test_problem034(self):
        self.assertEquals(problem34(), 40730)
    def test_problem035(self):
        self.assertEquals(problem35(), 55)
    def test_problem036(self):
        self.assertEquals(problem36(), 872187)
    def test_problem037(self):
        self.assertEquals(problem37(), 748317)
    def test_problem041(self):
        self.assertEquals(problem41(), 7652413)
    def test_problem067(self):
        self.assertEquals(problem67(), 7273)

if __name__ == "__main__":
    pass