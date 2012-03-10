#/bin/python

# http://projecteuler.net/index.php?section=problems&id=32

import prime

def is_pandigital(n,s):
    #print(n,s)
    #s = str(s)
    if len(s) != n:
        return False
    res = [m for m in range(1,n+1) if s.find(str(m)) != -1]
    #print res
    return len(s) == len(res)

print( is_pandigital(5,'54321') )
print( is_pandigital(5,'54821') )
print( is_pandigital(5,'12345') )
print( is_pandigital(5,'54123') )
print( is_pandigital(9,'541238796') )
print( is_pandigital(9,'541238794') )

res = [n*m for n in range(1,101) for m in range(1,10001) if is_pandigital(9,(str(n)+str(m)+str(n*m)))]
#res = [n*m for n in range(1,101) for m in range(1,101)] print( sum(set(res)) )

res = [n*m for n in range(1,1001) for m in range(1,10001) if is_pandigital(9,(str(n)+str(m)+str(n*m)))]
#res = [n*m for n in range(1,101) for m in range(1,101)]
print( sum(set(res)) ) # 45228
