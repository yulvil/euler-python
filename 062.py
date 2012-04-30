#/bin/python

# http://projecteuler.net/problem=62

'''
The cube, 41,063,625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

#from math import factorial
from itertools import permutations,count
#import prime

def is_cube(n):
    x = n**(1/3)
    return x == int(x)

def get_cubes(n):
    l = [p for p in permutations(str(n)) if is_cube(long(''.join(p)))]
    #l = [p for p in permutations(str(n))]
    return l

#g = (n for n in xrange(1,1000) if len(get_cubes(n**3))==3) g = (n for n in xrange(340,350) if len(get_cubes(n**3))==3)

#res = [n for n in g]
#print( res )

cubes = {n**3 for n in range(10000)}

cubes_it = (n**3 for n in count(0))

pre_calculated = {}

for my_cube in cubes_it:
    s = str(my_cube)
    print(s)
    perms = permutations(s, len(s))
    res = [int(''.join(n)) for n in perms]
    #print(list(perms))
    #print(res)
    zcubes = set([n for n in res if n in cubes])
    if len(zcubes) == 5:
        print(zcubes)
        break
    #print(zcubes)
    #break
    #break
    #nb_permutations = [1 for perm in perms if is_cube(int(perm))]
    #print("{} {}".format(my_cube, nb_permutations))

#print( [n for n in permutations(str(1234))])

# unresolved

#print(list(permutations("abc",3)))

#print(is_cube(27))
#print(is_cube(64))
