#/bin/python

# http://projecteuler.net/index.php?section=problems&id=25

import fib
#from itertools import takewhile

def find_sum_longer_than(mylen):
    for i,n in enumerate(fib.fib2(),1):
        #print i,n
        if len(str(n)) > mylen:
            return i

print( find_sum_longer_than(999) ) # 4782
