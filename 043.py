#/bin/python

# http://projecteuler.net/index.php?section=problems&id=44

from itertools import count,permutations
import math
import array

c = permutations('1234567890')

def has_props(n):
    s = n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8] + n[9]
    if int(s[1:4])%2==0 and int(s[2:5])%3==0 and int(s[3:6])%5==0 and int(s[4:7])%7==0 and int(s[5:8])%11==0 and int(s[6:9])%13==0 and int(s[7:10])%17==0:
        return True
    return False

res = (int(n[0] + n[1] + n[2] + n[3] + n[4] + n[5] + n[6] + n[7] + n[8] + n[9]) for n in c if has_props(n) )

print(sum(res)) # 16695334890

