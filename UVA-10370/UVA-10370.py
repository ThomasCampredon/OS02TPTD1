import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]

    lines[0] = int(lines[0])
    nbAccept = 0
    for i in range(1,lines[0]+1) :
        tab = list(map(int, lines[i].split()))
        nbNote = tab[0]
        sommeNote = 0
        for i in range(1,nbNote+1) :
            sommeNote+=tab[i]
        moyenne = sommeNote / nbNote
        nbEtuSupMoy=0
        for j in range(1,nbNote+1) :
            if tab[j]>moyenne :
                nbEtuSupMoy+=1
        
        pourcentageSupMoy = float(nbEtuSupMoy) / nbNote * 100
        print (str("{0:.3f}".format(pourcentageSupMoy))+ '%')
