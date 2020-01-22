import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]

    lines[0] = int(lines[0])

    for i in range(1,lines[0]+1) :
        tab = list(map(int, lines[i].split()))
        if tab[0]==tab[1]:
            print('=')
        else :
            if tab[0]<tab[1]:
                print("<")
            else :
                print(">")