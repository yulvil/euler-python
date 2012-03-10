#/bin/python

import sys

lines = sys.stdin.read().split('\n')
lines = lines[:-1]

mysum = sum(map(int,lines))
print( str(mysum)[0:10] )  # 5537376230
