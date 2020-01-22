import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]

    lines[0] = int(lines[0])
    nbAccept = 0
    for i in range(1,lines[0]+1) :
        tab = list(map(float, lines[i].split()))
        if tab[3]<=7.00 and ((tab[0]+tab[1]+tab[2] <= 125.00) or (tab[0]<=56.00 and tab[1]<=45.00 and tab[2]<=25.00)) :
            print(1)
            nbAccept += 1
        else :
            print (0)
    print (nbAccept)