#/bin/python

# http://projecteuler.net/problem=97
# http://en.wikipedia.org/wiki/Modular_exponentiation

#from prime import is_prime,prime_factors

#n = 28433 * 2**7830457 + 1
#print( str(n)[-10:] )

#print( [str(n)[-10:] for n in [28433**i+1 for i in range(100,1000)]] ) #print( is_prime(28433) )  # True #print( is_prime(27830457) )  # False #print( prime_factors(27830457) ) # [3, 3, 61, 163, 311]

#n = 28433**(3*3*61*163*311)+1

def modular_pow(base, exponent, modulus):
    c = 1
    for e_prime in range(1,exponent+1):
        c = (c * base) % modulus
    return c

n = modular_pow(2,7830457,100000000000000000000)
print( str(28433*n+1)[-10:] ) # 8739992577
