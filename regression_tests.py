__author__ = 'muchaco'

from unittest import TestCase
from problems import *


class UnitTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(UnitTest, self).__init__(*args, **kwargs)

    def test_problem1(self):
        self.assertEquals(problem1(), 233168)
    def test_problem2(self):
        self.assertEquals(problem2(), 4613732)
    def test_problem3(self):
        self.assertEquals(problem3(), 6857)
    def test_problem4(self):
        self.assertEquals(problem4(), 906609)
    def test_problem5(self):
        self.assertEquals(problem5(), 232792560)
    def test_problem6(self):
        self.assertEquals(problem6(), 25164150)
    def test_problem7(self):
        self.assertEquals(problem7(), 104743)
    def test_problem8(self):
        self.assertEquals(problem8(), 23514624000)
    def test_problem9(self):
        self.assertEquals(problem9(), 31875000)
    def test_problem10(self):
        self.assertEquals(problem10(), 142913828922)
    def test_problem11(self):
        self.assertEquals(problem11(), 70600674)
    def test_problem12(self):
        self.assertEquals(problem12(), 76576500)
    def test_problem13(self):
        self.assertEquals(problem13(), 5537376230)
    def test_problem14(self):
        self.assertEquals(problem14(), 837799)
    def test_problem15(self):
        self.assertEquals(problem15(), 137846528820)
    def test_problem16(self):
        self.assertEquals(problem16(), 1366)
    def test_problem17(self):
        self.assertEquals(problem17(), 21124)
    def test_problem18(self):
        self.assertEquals(problem18(), 1074)
    def test_problem19(self):
        self.assertEquals(problem19(), 171)
    def test_problem20(self):
        self.assertEquals(problem20(), 648)
    def test_problem21(self):
        self.assertEquals(problem21(), 31626)
    def test_problem22(self):
        self.assertEquals(problem22(), 871198282)
    def test_problem23(self):
        self.assertEquals(problem23(), 4179871)
    def test_problem24(self):
        self.assertEquals(problem24(), 2783915460)
    def test_problem251(self):
        self.assertEquals(problem25(), 4782)
    def test_problem26(self):
        self.assertEquals(problem26(), 983)
    def test_problem27(self):
        self.assertEquals(problem27(), -59231)
    def test_problem28(self):
        self.assertEquals(problem28(), 669171001)
    def test_problem29(self):
        self.assertEquals(problem29(), 9183)
    def test_problem30(self):
        self.assertEquals(problem30(), 443839)
    def test_problem31(self):
        self.assertEquals(problem31(), 73682)
    def test_problem32(self):
        self.assertEquals(problem32(), 45228)
    def test_problem41(self):
        self.assertEquals(problem41(), 7652413)
    def test_problem67(self):
        self.assertEquals(problem67(), 7273)

if __name__ == "__main__":
    pass