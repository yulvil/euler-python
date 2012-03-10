#/bin/python

# http://projecteuler.net/index.php?section=problems&id=15

from math import factorial
from itertools import permutations,count
import prime

def nexxt():
    for n in count():
        yield n

s = [str(n) for n in range(0,200000)]
s = "".join(s)
print( int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000]) ) # 210

