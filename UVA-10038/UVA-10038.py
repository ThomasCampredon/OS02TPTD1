import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]
    
    for line in lines :
        estJolly = True
        tab = list(map(int, line.split()))
        nbInt = tab[0]
        listeNombre = []
        listeDifference = []

        for i in range (1, nbInt):
            listeNombre.append(i)
        for j in range (1, nbInt):
            listeDifference.append(abs(tab[j]-tab[j+1]))
        for k in range(0, len(listeDifference)):
            if not listeDifference[k] in listeNombre:
                 estJolly=False
        for l in range(0, len(listeNombre)):                
            if not listeNombre[l] in listeDifference:
                estJolly=False
        if estJolly:
            print("Jolly")
        else:
            print("Not jolly")