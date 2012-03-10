#/bin/python

# http://projecteuler.net/index.php?section=problems&id=32

def gcd(n,m):
    if n<m:
        return gcd(m,n)
    if m<=0:
        return n
    return gcd(m,n%m)

def reduce_fraction(f):
    d=gcd(f[0],f[1])
    return (f[0]/d,f[1]/d)

def add_fractions(f1,f2):
    return (f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1])

def mul_fractions(f1,f2):
    return (f1[0] * f2[1] * f2[0] * f1[1], f1[1] * f2[1])

def is_weird_fraction(n,m):
    res = 1.0*n/m
    if res <= 0.0 or res >= 1.0:
        return False
    nn=str(n)
    mm=str(m)
    if m%10==0:
        return False
    #print("{} {} {} {}".format(n//10,m%10,1.0*(n//10)/(m%10),res))
    if 1.0*(n//10)/(m%10) == res and ((n%10)==(m//10)):
        return True
    return False

#print( is_weird_fraction(49,98) )

res = [(n,m) for n in range(10,100) for m in range(10,100) if is_weird_fraction(n,m)] # print( res ) # [(16, 64), (19, 95), (26, 65), (49, 98)]

from functools import reduce
tot = reduce_fraction(reduce(mul_fractions,res))

print( tot )

#print( add_fractions((1,2),(1,4)) )
#print( add_fractions((1,2),(1,8)) )

#print( gcd(4,8) )
#print( gcd(8,4) )
#print( reduce_fraction((10,16)) )
#print( reduce_fraction((20,32)) )
#print( reduce_fraction((40,64)) )

import fractions
res = [fractions.Fraction(m,n) for n in range(10,100) for m in range(10,100) if is_weird_fraction(n,m)]
#res = [(n,m) for n in range(10,100) for m in range(10,100) if is_weird_fraction(n,m)]
print( res )

tot = reduce(lambda x,y: x*y, res)
print( tot ) 
