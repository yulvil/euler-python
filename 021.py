#/bin/python

# http://projecteuler.net/problem=21
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import prime

def is_amical(n):
    sum1 = sum(prime.get_divisors(n)-set([n]))
    sum2 = sum(prime.get_divisors(sum1)-set([sum1]))
    #print( n, sum1, sum2 )
    return n == sum2 and n != sum1

#print( is_amical(219) )
#print( is_amical(220) )
#print( is_amical(221) )

mylist = [n for n in range(2,10000) if is_amical(n)]
#print( mylist )
mysum = sum(mylist)
print( mysum ) # 31626

