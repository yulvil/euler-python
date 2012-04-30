#/bin/python

# http://projecteuler.net/problem=71

'''
Consider the fraction, n/d, where n and d are positive integers. If nd and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d  1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''

from pprint import pprint
from math import factorial
from itertools import permutations,count #import prime

# 69 363600 1454 169 363601 (1454)

def getNext(n):
   #if n > 1000000: print n
   return sum(map(factorial,map(int,list(iter(str(n))))))

cache = dict()

def getChain(n):
   #print(n)
   s = [n]
   m = getNext(n)
   while m not in s:
      s.append(m)
      m = getNext(m)
   s.append(m)
   #cache[m] = s[s.index(m):]
   return s

#def getChainWithCache(n):
#   if n in cache:
#      return cache[n]
#   s = [n]
#   #s.append(getChainWithCache(getNext(n)))
#   #return s
#   return s + getChainWithCache(getNext(n))

#def is_repeating_chain(n):
#   s = {n}
#   m = getNext(n)
#   while m not in s:
#      s.add(m)
#      m = getNext(m)
#   return n == m

#print( getChain(69) )
#print( getChain(1454) )
#print( getChain(169) )

r = (1 for n in range(1,1000001) if len(getChain(n)) == 61)
print( sum(r) ) # 402 in 4m33

#r = (getChain(n) for n in range(1,100000)) #for l in r:
#   x=1
#print( list(r) )
#r = (getChainWithCache(n) for n in range(60,70)) #print( list(r) )

#for n in xrange(1,101):
#   print(getChain(n))
