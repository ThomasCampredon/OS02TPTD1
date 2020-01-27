import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]

    dico = {}
    finDuDico = False
    for line in lines :
        tab = line.split()
        if (not finDuDico) :
            if line=="\n" :
                finDuDico = True
            else:
                dico[tab[1]] = tab[0]
        else :
            if tab[0] in dico:
               print (dico[tab[0]])
            else:
                print("eh")