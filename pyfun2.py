#odd nums from 1 1000
for n in range(1, 1000, 2):
    print(n)

#multiples of 5 from 5 to 1000000    
for n in range(5, 1000000, 5):
    print(n)

def sumlist1(arr):
    res = 0
    for elem in arr:
        res += elem
    return res

def sumlist2(arr):
    return sum(arr)  #but this is cheating isn't it? ;)

def averagelist(arr):
    return float(sum(arr))/len(arr)