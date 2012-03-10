#/bin/python

def sum_digits(n):
    total = 0
    s = str(n)
    for c in s:
        total+=int(c)
    return total

print( sum_digits(2**1000) )  # 1366
