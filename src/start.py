
map = [ [None for j in range(4)] for i in range(4)]

map[1][0] = 2
map[3][0] = 2

####reversed
def showMap(map):
    for ligne in map:
        print(ligne)

def fussionZ(map):
    #parcoure la carte ligne par ligne
    for x in range(len(map)):
        promotionCandidates = None
        ycandidate = None
        ylibre = None
        for y in range(len(map)):

            CaseValue = map[y][x]
            # quand il y a un nombre
            if CaseValue != None:

                if promotionCandidates == None:
                    if ylibre != None:
                        #deplace le numero
                        map[y][x] = None
                        map[ylibre][x] = CaseValue
                        ycandidate = ylibre
                        ylibre = y
                    else:
                        ycandidate = y
                        
                    #on selection le candidate
                    promotionCandidates = CaseValue

                else:
                    if CaseValue == promotionCandidates:
                        map[ycandidate][x] = CaseValue*2
                        map[y][x] = None
                        promotionCandidates = None
                        
                        if ylibre==None:
                            ylibre = y
                    else:
                        if ylibre != None:
                            #deplace le numero
                            map[y][x] = None
                            map[ylibre][x] = CaseValue
                            ycandidate = ylibre
                            ylibre = y
                        else:
                            ycandidate = y
                        
                        promotionCandidates = CaseValue
            elif ylibre == None:
                ylibre = y


                        




showMap(map)
while True:
    entre = input("choisie l'action\n")

    match entre:
        case "Z":
            fussionZ(map)
        case "S":
            pass
        case "Q":
            pass
        case "D":
            pass

    showMap(map)