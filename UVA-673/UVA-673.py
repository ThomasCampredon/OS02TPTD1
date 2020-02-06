import sys

while True:
    lines = sys.stdin.readlines()
    while lines[-1] == '\n':
        del lines[-1]

    for line in lines :
        compteurParOuv = 0
        compteurParFer = 0
        compteurCroOuv = 0
        compteurCroFer = 0

        parOpenNow = 0
        croOpenNow = 0
        
        estYes = True

        String = list(str(line))

        m=0

        if (String[m] == "\n"):
            print("Yes")
        else:  
            caracEnCours = String[m]
            finDeChaine = String[len(String)-2] 

            if caracEnCours == ")" or caracEnCours == "]" or finDeChaine == "(" or finDeChaine == "[":
                print("No")
            else:
                if (caracEnCours == "("):
                    compteurParOuv += 1
                    parOpenNow += 1
                    
                if (caracEnCours == "["):
                    compteurCroOuv += 1
                    croOpenNow+=1

                dernierCaractere = caracEnCours

                i = 1    
                while (i<len(String)) and (estYes):
                    caracEnCours = String[i]
                    if caracEnCours == "(":
                        compteurParOuv+=1
                        parOpenNow+=1

                    if caracEnCours == "[":
                        compteurCroOuv+=1
                        croOpenNow += 1

                    if caracEnCours == ")":
                        if dernierCaractere == "[":
                            estYes = False
                        else:
                            compteurParFer+=1
                            parOpenNow-=1

                    if caracEnCours == "]":
                        if dernierCaractere == "(":
                            estYes = False
                        else:
                            compteurCroFer+=1
                            croOpenNow -= 1

                    if parOpenNow < 0 or croOpenNow<0:
                        estYes = False
                    dernierCaractere = caracEnCours
                    i+=1

                if (not estYes) or (compteurCroFer != compteurCroOuv or compteurParFer != compteurParOuv):
                    print("No")
                else:
                    print("Yes")
            
                
                
