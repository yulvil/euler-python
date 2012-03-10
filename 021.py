#/bin/python

import prime

def is_amical(n):
    sum1 = sum(prime.get_divisors(n)-set([n]))
    sum2 = sum(prime.get_divisors(sum1)-set([sum1]))
    print( n, sum1, sum2 )
    return n == sum2 and n != sum1

print( is_amical(219) )
print( is_amical(220) )
print( is_amical(221) )

mylist = [n for n in range(2,10000) if is_amical(n)]
print( mylist )
mysum = sum(mylist)
print( mysum ) # 31626

