#/bin/python

# http://projecteuler.net/index.php?section=problems&id=27

# n**2 + an + b, where |a| < 1000 and |b| < 1000

import prime

r = range(-1000,1001)
#r = range(-10000,10001)

gen = ((a,b) for a in r for b in r)

def calc_len(a,b):
    for n in range(1,1000):
        if not prime.is_prime(n**2+a*n+b):
           return (a,b,n)

mymax = (0,0,0)

for p in gen:
    res = calc_len(*p)
    if res[2] > mymax[2]:
        mymax = (p[0], p[1], res[2])

print( mymax )  # (-61, 971, 71)

print (mymax[0]*mymax[1]) # -59231

