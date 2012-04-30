#/bin/python

def fibonacci(n):
  a,b = 0,1
  for i in range(0,n):
    a,b, = b,a+b

def fib(n):
    a,b = 0,1
    for i in range(0,n):
        a,b, = b,a+b
        yield a

#mylist = [n for n in fib(100)]
#print( mylist )

def fib2():
    a,b = 0,1
    while True:
        (a, b) = (b, a+b)
        yield a
