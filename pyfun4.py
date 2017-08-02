def process_list(l):
    s = ''
    n = 0
    typespresent = set()
    for item in l:
        if isinstance(item, str):
            s += item + ' '
        elif isinstance(item, float) or isinstance(item, int):
            n += item
        typespresent.add(type(item))
    typesmsgstr = 'mixed'
    if len(typespresent) == 1:
        typesmsgstr = typespresent.pop()
    print("The list you entered is of {} type".format(typesmsgstr))
    if s:
        print('string: '+s)
    if n:
        print("sum of nums: "+str(n))


l = ['magical unicorns',19,'hello',98.98,'world']
process_list(l)

l = [2,3,1,7,4,12]
process_list(l)