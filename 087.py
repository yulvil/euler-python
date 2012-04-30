#/bin/python

# http://projecteuler.net/problem=87

'''
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''

from prime import prime_it
from pprint import pprint

num = 50
num = 50000000 # 0.687s

r1 = int(num**0.5)+1
r2 = int(num**(1.0/3))+1
r3 = int(num**0.25)+1
primes1 = list(prime_it(r1))
primes2 = list(prime_it(r2))
primes3 = list(prime_it(r3))
#pprint( primes )
#print( len(primes) )

#n = sum(1 for a in primes1 for b in primes2 for c in primes3 if a**2 + b**3 + c**4 <num) #print( n ) # 1139575

g = (a**2 + b**3 + c**4 for a in primes1 for b in primes2 for c in primes3 if a**2 + b**3 + c**4 <num)
print( len(set(g)) )  # 1,097,343 unique   1.385s
