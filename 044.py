#/bin/python

# http://projecteuler.net/index.php?section=problems&id=44

from itertools import count,combinations

def penta(maxn):
    for n in range(1,maxn):
        yield n*(3*n-1)/2

def is_penta(n):
    a,b,c = 3,-1,-2*n
    x = (b*-1 + (b**2-4*a*c)**0.5)/(2*a)
    #y = (b*-1 - (b**2-4*a*c)**0.5)/(2*a)
    #print x, y, x//x, 1.0*x/x
    return x == int(x)
    #return x == long(x)

#for n in penta():
#    print(n)

print( is_penta(69) )
print( is_penta(70) )
print( is_penta(71) )
print( is_penta(92) )
print( is_penta(145) )

l = [n for n in penta(20000)]
#print( l )

c = (n for n in combinations(l,2))
#cc = [n for n in c]
#print(len(c))
#cc = [n for n in c if n[0] in l and n[1] in l and (n[0]+n[1]) in l and (n[1]-n[0]) in l]
#cc = [n for n in c if (n[0]+n[1]) in l and (n[1]-n[0]) in l]
#cc = (n for n in c if (n[0]+n[1]) in l and (n[1]-n[0]) in l)
cc = (n for n in c if is_penta(n[0]+n[1]) and is_penta(n[1]-n[0]))

for n in cc:
    print (n)

