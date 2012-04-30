#/bin/python

# http://projecteuler.net/problem=36

'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

r = range(1,1000001)
pals = [n for n in r if is_palindrome(n) and is_palindrome(bin(n)[2:])]
print(pals)
print(sum(pals))  # 872187

