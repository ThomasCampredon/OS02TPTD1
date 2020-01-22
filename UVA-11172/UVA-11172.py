import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]

    for line in lines :
        tab = list(map(int, line.split()))
        if tab[1]:
            if tab[0]==tab[1]:
                print('=')
            if tab[0]<tab[1]:
                print("<")
            else :
                print(">")