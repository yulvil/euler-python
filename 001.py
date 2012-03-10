#/bin/python

# Add all the natural numbers below 1000 that are multiples of 3 or 5.

#mylist = [n for n in range(1,1000) if n%3==0 or n%5==0]
mylist = (n for n in range(1,1000) if n%3==0 or n%5==0)
print( sum(mylist) ) # 233168
