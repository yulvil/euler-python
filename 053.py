#/bin/python

# http://projecteuler.net/problem=53

'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n! / r!(nr)!
,where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
'''

from math import factorial
from itertools import permutations,count
import prime

def com(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

pairs = ((n,k) for n in range(1,101) for k in range(1,n))

res = (com(n[0],n[1]) for n in pairs if com(n[0],n[1])>1000000)

print( len(list(res)) ) # 4075
