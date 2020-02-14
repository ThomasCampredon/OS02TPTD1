import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]
    
    dico = {}
    finDuDico = False
    somme = 0.00
    for line in lines :
        tab = line.split()
        if (not finDuDico) :
            if line=="\n" :
                finDuDico = True
            else:
                dico[tab[0]] = float(tab[1])
        else :
            somme = somme + dico[tab[1]]*int(tab[0])

    print("%.2f" % somme)

