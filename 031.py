#/bin/python

# http://projecteuler.net/index.php?section=problems&id=31
# http://en.wikipedia.org/wiki/Modular_exponentiation

#from prime import is_prime,prime_factors

import pprint

def total(a,b,c,d,e,f):
    return 100*a + 50*b + 20*c + 5*d + 2*e + 1*f

#res = sum((1 for a in range(0,3) for b in range(0,5) for c in range(0,11) for d in range(0,41) for e in range(0,51) for f in range(0,201) if total(a,b,c,d,e,f)==200))
res = 1+sum((1 for a in range(0,3) for b in range(0,5) for c in range(0,11) for d in range(0,41) for e in range(0,101) for f in range(0,201) if total(a,b,c,d,e,f)==200))
print(res) # 14699

#res = [(a,b,c,d,e,f) for a in range(0,3) for b in range(0,5) for c in range(0,11) for d in range(0,41) for e in range(0,101) for f in range(0,201) if total(a,b,c,d,e,f)==200]
#print( pprint.pprint(res) )
#print( len(set(res)) )

