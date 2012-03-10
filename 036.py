#/bin/python

# http://projecteuler.net/index.php?section=problems&id=36

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

r = range(1,1000001)
pals = [n for n in r if is_palindrome(n) and is_palindrome(bin(n)[2:])]
print(pals)
print(sum(pals))  # 872187

