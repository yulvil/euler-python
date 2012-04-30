#/bin/python

# http://projecteuler.net/problem=50

'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import pprint
#pp = pprint.PrettyPrinter(indent=1)
pp = pprint.PrettyPrinter()

import prime

#primes = [n for n in prime.prime_it(1000000)][::-1] primes = [n for n in prime.prime_it(1000000)] nbprimes = len(primes) #primes = [n for n in prime.prime_it(5000)][::-1] #print( primes )

primes = list(prime.prime_it(1000000))
print(primes)

def sum_equal(l,n):
    return sum(l)==n

def has_prime_seq(myprime):
    p = [m for m in primes if m<myprime//2] # primes lower than myprime
    nbprimes = len(p)
    print( nbprimes )
    subs = (p[i:nbprimes-j] for i in range(0,nbprimes) for j in range(0,nbprimes-i))
    #pp.pprint( subs )
    res = [(len(zz),zz,sum(zz)) for zz in subs if sum(zz)==myprime]
    print( res )
    return res

def has_prime_seq2(myprime):
    p = [m for m in primes if m<myprime] # primes lower than myprime
    nbprimes = len(p)
    #print( nbprimes )
    subs = ((i,j) for i in range(0,nbprimes) for j in range(0,nbprimes-i))
    #print( len(subs) )
    #res = [(len(pp),pp,sum(pp)) for pp in map(lambda(i,j): (p[i:j],subs)) if len(pp)>20 and sum(pp)==myprime]
    #subs = [p[i:nbprimes-j] for i in range(0,nbprimes) for j in range(0,nbprimes-i)]
    #print( len(subs) )
    #pp.pprint( subs )
    #res = [(len(zz),zz,sum(zz)) for zz in subs if len(zz)>20 and sum(zz)==myprime]
    return res

def sum_n_primes(n):
    return (n,sum(primes[0:n]))

def get_max_len(n):
    for i in range(0,len(primes)):
        if sum(primes[0:i]) > n:
            return i

def zz(maxlen):
    for currlen in range(maxlen,1,-1):
        #l = [p[i:j] for i in xrange(0,nbprimes-mylen) for j in xrange(mylen]
        l = (primes[i-currlen:i] for i in range(currlen,nbprimes))
        #print( l )
        for sub in l:
            mylist,mysum,mylen = sub,sum(sub),len(sub)
            if(prime.is_prime(mysum) and mysum<1000000):
               return(mylist,mysum,mylen)
        #ll = filter(lambda n: prime.is_prime(n) and n<1000000, map(sum,l))
        #print( ll )

ml = get_max_len(1000000)
print(ml)
print(zz(ml))

#nbprimes = len(primes)
#res = [sum_n_primes(m) for m in range(nbprimes) if sum_n_primes(m) < 1000000]
#print(res)

#res = [has_prime_seq(x) for x in primes if len(has_prime_seq(x))>0] #res = [has_prime_seq(x) for x in primes] #res = [has_prime_seq(x) for x in primes[0:1000]] #res = [has_prime_seq2(x) for x in primes[::-1]] #print res

#print( sum(primes[0:200]) )
#print( sum(primes[0:500]) )
#print( sum(primes[0:550]) )
#print( sum(primes[0:560]) )
#print( sum(primes[0:570]) )
#print( sum(primes[0:580]) )
#print( sum(primes[0:1000]) )
#print( sum(primes[0:2000]) )
#print( sum(primes[0:3000]) )

#sorted(student_tuples, key=lambda student: student[2])   # sort by age

#print( res )
#print( sorted(res, key=lambda t: t[2]) ) #print( max(sorted(res)) )

#print( has_prime_seq(100) )
#print( has_prime_seq(41) )
