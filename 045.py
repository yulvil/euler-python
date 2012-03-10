#/bin/python

# http://projecteuler.net/index.php?section=problems&id=44

from itertools import count,combinations

#def penta(maxn):
#    for n in range(1,maxn):
#        yield n*(3*n-1)/2

def is_penta(n):
    a,b,c = 3,-1,-2*n
    x = (b*-1 + (b**2-4*a*c)**0.5)/(2*a)
    #y = (b*-1 - (b**2-4*a*c)**0.5)/(2*a)
    #print x, y, x//x, 1.0*x/x
    return x == int(x)
    #return x == long(x)

def is_hexa(n):
    a,b,c = 2,-1,-n
    x = (b*-1 + (b**2-4*a*c)**0.5)/(2*a)
    y = (b*-1 - (b**2-4*a*c)**0.5)/(2*a)
    #return x == long(x) or y == long(y)
    return x == int(x)

def hexa(n):
    return n*(2*n-1)

def is_tri(n):
    a,b,c = 1,1,-2*n
    x = (b*-1 + (b**2-4*a*c)**0.5)/(2*a)
    return x == int(x)

#q = [n for n in xrange(1,10000) if is_tri(n)] #w = [n for n in xrange(1,10000) if is_penta(n)] #e = [n for n in xrange(1,10000) if is_hexa(n)]

gen = (hexa(n) for n in count(2))

def calc():
    for n in gen:
        if is_penta(n) and is_tri(n):
            yield n

calc() #.next()
print(list(calc())) # 1533776805
