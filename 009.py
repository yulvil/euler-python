#/bin/python

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
