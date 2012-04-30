#/bin/python

# http://projecteuler.net/problem=206

'''
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each _ is a single digit.
'''

expected = '1234567890'

n = 1929394959697981910
n = 1020304050607080900

def isSeq(n):
    s = str(n)[::2]
    return s == expected

res = [n for n in range(1000000000,1400000000,10) if isSeq(n**2)]
print(res) # 1389019170  0m42s
