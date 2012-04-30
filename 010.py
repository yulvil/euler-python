#/bin/python

# http://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import prime

l = (n for n in prime.prime_it(2000000))
print( sum(l) )  # 142913828922
