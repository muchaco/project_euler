__author__ = 'muchaco'

from unittest import TestCase
from problems import *


class UnitTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(UnitTest, self).__init__(*args, **kwargs)

    def test_regression(self):
        self.assertEquals(problem1(), "233168")
        self.assertEquals(problem2(), "4613732")
        self.assertEquals(problem3(), "6857")
        self.assertEquals(problem4(), "906609")
        #self.assertEquals(problem5(), "232792560")
        #self.assertEquals(problem6(), "25164150")
        self.assertEquals(problem7(), "104743")
        self.assertEquals(problem8(), "23514624000")
        self.assertEquals(problem9(), "31875000")
        #self.assertEquals(problem10(), "142913828922")
        self.assertEquals(problem11(), "70600674")
        self.assertEquals(problem12(), "76576500")
        self.assertEquals(problem13(), "5537376230")
        self.assertEquals(problem14(), "837799")
        self.assertEquals(problem15(), "137846528820")
        self.assertEquals(problem16(), "1366")
        self.assertEquals(problem17(), "21124")
        self.assertEquals(problem18(), "1074")
        self.assertEquals(problem19(), "171")
        #self.assertEquals(problem20(), "648")
        self.assertEquals(problem21(), "31626")
        self.assertEquals(problem22(), "871198282")
        self.assertEquals(problem23(), "4179871")
        self.assertEquals(problem24(), "2783915460")
        self.assertEquals(problem25(), "4782")
        self.assertEquals(problem67(), "7273")
        #self.assertEquals(problem26(), "983")

if __name__ == "__main__":
    pass