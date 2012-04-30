#/bin/python

# http://projecteuler.net/problem=40

'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000
'''

from math import factorial
from itertools import permutations,count
import prime

def nexxt():
    for n in count():
        yield n

s = [str(n) for n in range(0,200000)]
s = "".join(s)
print( int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000]) ) # 210
