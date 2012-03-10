#/bin/python

def it_sequence(n):
    seq = [n]
    while n!=1:
        if n%2==0: n=n//2
        else: n=n*3+1
        seq.append(n)
    return seq

def it_sequence_len(n):
    seqlen = 0
    while n!=1:
        if n%2==0: n=n//2
        else: n=n*3+1
        seqlen+=1
    return seqlen

#print( it_sequence(13) )

#seqs = [(n,len(it_sequence(n))) for n in range(1,1000001)]

#for n in range(1,1000001):
#    print n, it_sequence_len(n)

# 837799

mynum = 0
mymax = 0
for n in range(1,1000000):
    mylen = it_sequence_len(n)
    if mylen > mymax:
        mymax,mynum = mylen,n
 
#for n in range(1,1000000):
#    seq = it_sequence(n)
#		mylen = len(seq)
#    if mylen > mymax:
#        mymax = mylen
#        mynum = n

print( mynum, mymax )
