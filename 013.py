#/bin/python

# http://projecteuler.net/problem=13

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

#import sys
#lines = sys.stdin.read().split('\n')

def readAllLinesFromFile(filename):
    with open(filename) as myFile:
        return myFile.readlines();  # returns a list of string

lines = readAllLinesFromFile('013.dat')

mysum = sum(map(int,lines))
print( str(mysum)[0:10] )  # 5537376230
