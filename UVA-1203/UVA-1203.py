import sys
from operator import attrgetter, itemgetter

def getFactors(n):    
    result = []
    for i in range (1, n+1):
        if n%i==0:
            result.append(i)
    return result

class Registre:
    def __init__(self, nom, temps):
        self.nom = nom
        self.temps = temps

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]
    
    nbRequeteMax=0
    tempsEcoule=0
    registres = []
    finRegistre = False
    for line in lines :
        
        tab = line.split()
        if (tab[0] != '#'):
            if (finRegistre):
                nbRequeteMax = int(tab[0])
            else:
                registres.insert(tempsEcoule,Registre(int(tab[1]), int(tab[2])))
                tempsEcoule=tempsEcoule+1
        else:
            finRegistre = True
    
    nombreDeRequeteAffichee=0
    nbRegistre = len(registres)
    registres.sort(key = lambda Registre: Registre.temps)
    tempsEcoule = 0
    
    while nombreDeRequeteAffichee<nbRequeteMax :
        for k in range(0, nbRegistre):
            if nombreDeRequeteAffichee<nbRequeteMax :
                if registres[k].temps in getFactors(tempsEcoule):
                    nombreDeRequeteAffichee+=1
                    print(registres[k].nom)
        tempsEcoule=tempsEcoule+1       
                
                
               
        
       
    

            
        