#/bin/python

# http://projecteuler.net/index.php?section=problems&id=44

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

#g = (n for n in count(3) if sumfact(n)==n)
g = (n for n in range(3,10000000) if sumfact2(n)==n)

print( sum(g) )
#for n in g:
#    print n
