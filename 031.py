#/bin/python
# -*- coding: iso-8859-15 -*-

# http://projecteuler.net/problem=31
# http://en.wikipedia.org/wiki/Knapsack_problem

'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1£1 + 150p + 220p + 15p + 12p + 31p
How many different ways can £2 be made using any number of coins?
'''

#from prime import is_prime,prime_factors

import pprint

def total(a,b,c,d,e,f):
    return 100*a + 50*b + 20*c + 5*d + 2*e + 1*f

#res = sum((1 for a in range(0,3) for b in range(0,5) for c in range(0,11) for d in range(0,41) for e in range(0,51) for f in range(0,201) if total(a,b,c,d,e,f)==200))
l = list(((a,b,c,d,e,f) for a in range(0,3) for b in range(0,5) for c in range(0,11) for d in range(0,41) for e in range(0,101) for f in range(0,201) if total(a,b,c,d,e,f)==200))
print(l)
res = 1+sum((1 for a in range(0,3) for b in range(0,5) for c in range(0,11) for d in range(0,41) for e in range(0,101) for f in range(0,201) if total(a,b,c,d,e,f)==200))
print(res) # 14699

#res = [(a,b,c,d,e,f) for a in range(0,3) for b in range(0,5) for c in range(0,11) for d in range(0,41) for e in range(0,101) for f in range(0,201) if total(a,b,c,d,e,f)==200]
#print( pprint.pprint(res) )
#print( len(set(res)) )

# unsolved