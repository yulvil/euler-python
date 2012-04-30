#/bin/python

# http://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
#print( is_palindrome('900009') )
#print( is_palindrome('900029') )

r = range(1,1000)
#mult = [x*y for (x,y) in zip(r,r)]
mult = (x*y for x in r for y in r)

pals = (n for n in mult if is_palindrome(n)==True)

print( max(pals) )  # 906609
