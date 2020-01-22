import sys

while True:
    lines = sys.stdin.readlines()
    del lines[0]
    while lines[-1] == '\n':
        del lines[-1]

    dico = {}
    finDuDico = False
    for line in lines :
        if (not finDuDico) :
            tab = list(map(str, line.split()))
            if (tab[1]=='') :
                finDuDico = True
        
        #pourcentageSupMoy = float(nbEtuSupMoy) / nbNote * 100
        #print (str("{0:.3f}".format(pourcentageSupMoy))+ '%')
