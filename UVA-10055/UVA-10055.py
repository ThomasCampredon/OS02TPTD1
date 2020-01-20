import sys
while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]

    for line in lines :
        tab = list(map(int, line.split()))
        print(abs(tab[1]-tab[0]))