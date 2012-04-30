#/bin/python

# http://projecteuler.net/problem=15

# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

from math import factorial
from itertools import permutations
import prime

def com(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

def com(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))

b = (0,0)
e = (2,2)

p = [(0,1),(0,1),(1,0),(1,0)]
r = set([pp for pp in permutations(p)])
#print(r)
print(len(r))

# Too big
#p = [(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0),(1,0)]
#r = set([pp for pp in permutations(p)])
#print(r)
#print(len(r))

print( com(52,5) )
print( com(500,5) )
res = com(2,1)*com(10,1)*com(2,1)*com(10,1)*com(2,1)*com(9,1)*com(2,1)*com(9,1)*com(2,1)*com(8,1)*com(2,1)*com(8,1)*com(2,1)*com(7,1)*com(2,1)*com(7,1)*com(2,1)*com(6,1)*com(2,1)*com(6,1)*com(2,1)*com(5,1)*com(2,1)*com(5,1)*com(2,1)*com(4,1)*com(2,1)*com(4,1)*com(2,1)*com(3,1)*com(2,1)*com(3,1)*com(2,1)*com(2,1)*com(2,1)*com(2,1)
print( res )

print( prime.prime_factors(res / 137846528820) )
print( prime.prime_factors(137846528820) )

# unsolved