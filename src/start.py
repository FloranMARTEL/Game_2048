
map = [ [None for j in range(4)] for i in range(4)]

map[2][0] = 2
map[3][0] = 4

####reversed
def showMap(map):
    for ligne in map:
        print(ligne)

def moveCandidate(map,posLibre,pos,ReverseSense,vertical):
    longeurCoterMap = len(map)

    caseValue = map[pos[1]][pos[0]]
    if posLibre != (None,None): ##ylibre != None and xlibre != None:##
        #deplace le numero/valeur
        map[pos[1]][pos[0]] = None
        map[posLibre[1]][posLibre[0]] = caseValue
        #affecte les possition du nouveaux candidat
        posCandidate = posLibre
        if vertical:
            #parcoure sur le l'axe vertical

            if ReverseSense:
                sansparcoureligne = range(posCandidate[0],-1,-1)
            else:
                sansparcoureligne = range(posCandidate[0]+1,longeurCoterMap)

            #on cherche la premier case vide 
            for xx in sansparcoureligne:
                if map[pos[1]][xx] == None:
                    posLibre = (xx,pos[1])
                    break
        else:
            #parcoure sur le l'axe horizontal

            if ReverseSense:
                sansparcoureligne = range(posCandidate[1],-1,-1)
            else:
                sansparcoureligne = range(posCandidate[1]+1,longeurCoterMap)

            #on cherche la premier case vide 
            for yy in sansparcoureligne:
                if map[yy][pos[0]] == None:
                    posLibre = (pos[0],yy)
                    break

    else:
        #affecte la possition du nouveau candidate
        posCandidate = pos
    
    return map,posLibre,posCandidate

def fussion(map : list, direction):
    
    
    longeurCoterMap = len(map)
    
    ##valeur pour connêtre le sans de baleillange dans la grille
    vertical = direction == "Right" or direction == "Left"
    ReverseSense = direction == "Down" or direction == "Right"

    #parcoure la carte ligne par ligne ou colonne par colonne
    for x in range(longeurCoterMap):

        #inisiation des valeurs avant le parcoure
        #valeur de la case Candidates à la promution
        promotionCandidates = None
        #position de la case Candidates
        posCandidate = (None,None)
        #position du premier espace libre
        posLibre = (None,None)

        #sens du parcoure de la ligne ou colonne 
        sensparcoure = range(longeurCoterMap)
        if ReverseSense:
            sensparcoure = reversed(sensparcoure)
            
        for y in sensparcoure:
            #si on baleille en vertical on échange les valeur de x et y
            if vertical :
                #lastx enregistre la valeur de basse de x
                lastx = x
                x = y
                y = lastx

            CaseValue = map[y][x]

            
            if CaseValue != None:
                #is il ne peut pas avoire de promotion/fusion
                if promotionCandidates == None:
                    
                    
                    map,posLibre,posCandidate = moveCandidate(map,posLibre,(x,y),ReverseSense,vertical)

                    #affecte la vouleur du nouveau Candidate à la promotion/fusion
                    promotionCandidates = CaseValue
                    

                else:

                    if CaseValue == promotionCandidates:
                        #fussion la case Value avec le candidat
                        map[posCandidate[1]][posCandidate[0]] = CaseValue*2
                        map[y][x] = None
                        promotionCandidates = None
                        
                        #undique un espace libre si il n'y en avais pas
                        if posLibre == (None,None):##ylibre==None:
                            posLibre = (x,y)

                    else:
                        #la fussion n'est pas possible
                        map,posLibre,posCandidate = moveCandidate(map,posLibre,(x,y),ReverseSense,vertical)

                        #affecte la vouleur du nouveau Candidate à la promotion/fusion
                        promotionCandidates = CaseValue
                        


            # si il n'y avais pas d'espace libre on indique qu'il existe ce lui là
            elif posLibre == (None,None):
                posLibre = (x,y)
            
            if vertical:
                #remet la valeur de x
                x = lastx
    
    return map



                        




showMap(map)
while True:
    entre = input("choisie l'action\n")

    match entre:
        case "Z":
            map = fussion(map,"Top")
        case "S":
            map = fussion(map,"Down")
        case "Q":
            map = fussion(map,"Left")
        case "D":
            map = fussion(map,"Right")

    showMap(map)