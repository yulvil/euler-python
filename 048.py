#/bin/python

# http://projecteuler.net/problem=45

# Last 10 digits of 1**1 + 2**2 + ... + 1000**1000

#tot = sum([n**n for n in range(1,11)])
#print(tot)

tot = sum([n**n for n in range(1,1001)])
#print(tot)
s = str(tot)
print(s[len(s)-10:]) # 9110846700
