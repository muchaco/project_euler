__author__ = 'muchaco'


from time import time
from problems import *

def execute_problem(ith):
    t0 = time()
    try:
        print "The answer is:   " + globals()['problem' + str(ith)]()
        print "Execution time:  " + str(time() - t0) + " sec"
    except KeyError:
        print "This problem hasn't been resolved yet"

if __name__ == "__main__":
    execute_problem(23)
