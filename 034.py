#/bin/python

# http://projecteuler.net/problem=34

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from itertools import count,combinations #from math import factorial
import math

def sumfact(n):
    tot=0
    s = str(n)
    for c in s:
        tot+=math.factorial(int(c))
    return tot

fact = [math.factorial(n) for n in range(0,10)]
def sumfact2(n):
    tot=0
    s = str(n)
    for c in s:
        tot+=fact[int(c)]
    return tot

# slowest
#def sumfact3(n):
#    return sum(map(math.factorial,map(int,str(n))))

g = (n for n in range(3,100000) if sumfact2(n)==n)

print( sum(g) ) # 40730