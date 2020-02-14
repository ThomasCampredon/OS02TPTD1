import sys

stop = False
while not stop:
    lines = sys.stdin.readlines()
    
    dico = {}
    finDuDico = False
    somme = 0.00
    panierok = True
    for line in lines :
        tab = line.split()
        if (not finDuDico) :
            if line=="\n" :
                finDuDico = True
            else:
                dico[tab[0]] = float(tab[1])
        else :
            if (tab[1] not in dico):
                panierok = False
            else:
                somme = somme + dico[tab[1]]*float(tab[0])

    if (panierok):
        print("%.2f" % somme)
    else:
        print("Panier invalide")
    stop = True

