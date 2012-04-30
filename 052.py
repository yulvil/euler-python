#/bin/python

# http://projecteuler.net/problem=52

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from math import factorial
from itertools import permutations,count
import prime

def same_digits(i2,i3,i4,i5,i6):
    #s2 = str(i2)
    #s3 = str(i3)
    #s4 = str(i4)
    #s5 = str(i5)
    #s6 = str(i6)
    #return sorted(s2) == sorted(s3) == sorted(s4) == sorted(s5) == sorted(s6)
    return sorted(str(i2)) == sorted(str(i3)) == sorted(str(i4)) == sorted(str(i5)) == sorted(str(i6))

res = [n for n in range(1,10000000) if same_digits(2*n,3*n,4*n,5*n,6*n)] #res = [n for n in xrange(1,10) if same_digits(2*n,3*n,4*n,5*n,6*n)]

print( min(res) ) # 142857
