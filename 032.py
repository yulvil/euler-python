#/bin/python

# http://projecteuler.net/problem=32

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

digits = "123456789"
digits_arr = [set(digits[0:n]) for n in range(0,10)]

def is_pandigital(n,s):
    return len(s) == n and set(s) == digits_arr[n]
    
def is_pandigital2(n,s):
    if len(s) != n:
        return False
    res = [m for m in range(1,n+1) if s.find(str(m)) != -1]
    return len(s) == len(res)

#print( is_pandigital(5,'54321') )
#print( is_pandigital(5,'54821') )
#print( is_pandigital(5,'12345') )
#print( is_pandigital(5,'54123') )
#print( is_pandigital(9,'541238796') )
#print( is_pandigital(9,'541238794') )

#res = [n*m for n in range(1,101) for m in range(1,10001) if is_pandigital(9,(str(n)+str(m)+str(n*m)))]
#res = [n*m for n in range(1,101) for m in range(1,101)] print( sum(set(res)) )

res = [n*m for n in range(1,1001) for m in range(1,10001) if is_pandigital(9,(str(n)+str(m)+str(n*m)))]
#res = [n*m for n in range(1,101) for m in range(1,101)]
print( sum(set(res)) ) # 45228
