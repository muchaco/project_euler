from time import time
from problems import *
import sys

__author__ = 'muchaco'


def execute_problem(ith):
    t0 = time()
    try:
        print("The answer is:   " + str(globals()['problem' + str(ith)]()))
        print("Execution time:  " + str(time() - t0) + " sec")
    except KeyError:
        print("This problem hasn't been resolved yet")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        execute_problem(sys.argv[1])
    else:
        print('usage: "python problem_executor.py n" where n is the index of the problem')
