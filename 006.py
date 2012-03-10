#/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

#sumsq = sum([n*n for n in range(1,11)])
#sqsum = sum([n for n in range(1,11)])**2
#print( sumsq )
#print( sqsum )

sumsq = sum([n*n for n in range(1,101)])
sqsum = sum([n for n in range(1,101)])**2
#print( sumsq )
#print( sqsum )
print( sqsum-sumsq ) # 25164150
