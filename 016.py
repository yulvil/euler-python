#/bin/python

# http://projecteuler.net/problem=16

# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?


def sum_digits(n):
    total = 0
    s = str(n)
    for c in s:
        total+=int(c)
    return total

print( sum_digits(2**1000) )  # 1366
