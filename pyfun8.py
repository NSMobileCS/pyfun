#!/usr/bin/python2
def odd_even(n=2000):
    for i in range(1,n):
        evenness = 'even'
        if i % 2 != 0:
            evenness = 'odd'
        print i, "This is an {} number.".format(evenness)

def multiply(arr, val):
    return [n * val for n in arr]

def layered_multiples(seq):
    l = []
    for n in seq:
        l.append([1 for i in range(n)])
    return l

l = layered_multiples(multiply([2,4,5],3))
print(l)