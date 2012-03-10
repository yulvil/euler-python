#/bin/python

import operator
def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__

    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2

    while op(num1, num2):
        yield num1
        num1 += step

prime_cache = [2,3,5,7,11,13,17,19]

#def is_prime(n, prime_cache = [2,3,5,7,11,13,17,19]):
def is_prime(n):
    #low_primes = [2,3,5,7,11,13,17,19]
    #if n==1 or n%2==0 or n%3==0 or n%5==0 or n%7==0:
    #    return False
    #if n == 2:
    #    return True
    if n in prime_cache:
        return True
    if n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%11==0 or n<2: return False
    for i in range(13,int((n**0.5))+1,2):
        if (n%i)==0:
            return False
    #prime_cache.append(n)
    return True

# All the primes under n
def prime_it(max_n):
    for i in lrange(1,max_n):
        if is_prime(i):
            yield i

#mylist = [n for n in prime_it(100000)]
#print( mylist )

def prime_factors_slow(n):
    factors = []
    for i in lrange(n//2+1):
        #print( i )
        while is_prime(i) and n%i==0:
            factors.append(i)
            n=n//i
    return factors

def prime_factors(n):
    factors = []
    for i in lrange(2,n//2+1):
        if n==1: break
        while n%i==0: # and n>1:
            factors.append(i)
            n=n//i
            #print( "{} {} {}".format(n, i,factors) )
    return factors

def prime_num(nb,max_prime=1000000):
    for i,n in enumerate(prime_it(max_prime)):
        if (i+1)==nb:
            return n


#print( prime_factors(4480) ) # [2, 2, 2, 2, 2, 2, 2, 5, 7] #print( prime_factors(600851475143) )


def get_divisors(n):
    divisors=[1]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            divisors.append(n//i)
    return set(divisors)
