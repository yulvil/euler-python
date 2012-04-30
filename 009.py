#/bin/python

# http://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.


# a**2 + b**2 = c**2
# a + b + c = 1000
# a<b<c
# a*b*c=?

#def triplet():
#    for a in r for b in r for c in r:
#        yield (a,b,c)

r = range(1001)
l = [(a,b,1000-a-b) for a in r for b in r if a**2+b**2-(1000-a-b)**2==0 and a<b and b<(1000-a-b)]
print( l ) # [(200, 375, 425)]
print( [x*y*z for (x,y,z) in l] )  # [31875000]
