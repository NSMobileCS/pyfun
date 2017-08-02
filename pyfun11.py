def draw_stars(l):
    for n in l:
        print("*"*n)

def draw_stars2(l):
    sym = '*'
    for n in l:
        if isinstance(n, str):
            n, sym = len(n), n[0]
        print(sym*n)

x = [4, 6, 1, 3, 5, 7, 25]
y = [4, 6, 'xylophone', 3, 5, 'seven', 25]
draw_stars(x)
draw_stars2(x)
draw_stars2(y)