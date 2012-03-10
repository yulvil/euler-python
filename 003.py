#/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.  What is the largest prime factor of the number 600851475143?

import prime

fact = prime.prime_factors(600851475143)
print( fact )       # [71, 839, 1471, 6857]
print( max(fact) )  # 6857
