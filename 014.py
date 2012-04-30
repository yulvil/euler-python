#/bin/python

# http://projecteuler.net/problem=14

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence: 13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

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

cache = {1:1}
def it_seq_len_recursive(n):
    if n in cache: return cache[n]
    elif n%2 == 0: cache[n] = 1 + it_seq_len_recursive(n//2)
    else: cache[n] = 1 + it_seq_len_recursive(n*3+1)
    return cache[n]

def main():
    mynum = 0
    mymax = 0
    for n in range(1,1000000):
        mylen = it_seq_len_recursive(n)
        if mylen > mymax:
            mymax,mynum = mylen,n

    print( mynum, mymax ) # 837799

if __name__ == "__main__":
    main()
