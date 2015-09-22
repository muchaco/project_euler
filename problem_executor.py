__author__ = 'muchaco'

from time import time
from problems import *
import sys


def execute_problem(ith):
    t0 = time()
    try:
        print "The answer is:   " + str(globals()['problem' + str(ith)]())
        print "Execution time:  " + str(time() - t0) + " sec"
    except KeyError:
        print "This problem hasn't been resolved yet"

if __name__ == "__main__":
    #if len(sys.argv) == 2:
    #    execute_problem(sys.argv[1])
    #else:
    #    execute_problem(5)
    print Fraction((1,2)).subtract_with(Fraction((1,8))).get()