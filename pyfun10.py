from random import randrange

def toss5K():
    l = [randrange(2) for _ in range(5000)]
    headcount = 0
    for idx, result in enumerate(l):
        sidename = 'tail'
        headcount += result
        if result:
            sidename = 'head'
        print("Attempt #{}: Throwing a coin... It's a {}... got {} heads and {} tails so far".format(idx+1, sidename, headcount, idx-headcount))


if __name__ == '__main__':
    toss5K()