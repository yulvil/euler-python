#/bin/python

# http://projecteuler.net/problem=27

'''
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n**2  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

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

