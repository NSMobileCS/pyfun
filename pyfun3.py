def main(x):
    """
    does checking and performs required action
    """
    print('checking type of', x)
    if isinstance(x, int):
        if x > 99:
            print("that's a big number")
        else:
            print("that's a small number")
    elif isinstance(x, str):
        if len(x) > 49:
            print("Long sentence")
        else:
            print("short sentence")
    elif isinstance(x, list):
        if len(x) > 9:
            print("long list")
        else:
            print('short list')
    else:
        print("unknown type,", type(x))


#test cases
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


testvarslist = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]
for n, testvalue in enumerate(testvarslist):
    print(n)
    print('test value', testvalue)
    main(testvalue)