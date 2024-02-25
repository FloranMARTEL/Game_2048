
from random import randint


class Game:

    def __init__(self) -> None:
        self.map = [ [None for j in range(4)] for i in range(4)]
        self.longeurCoterMap = len(self.map)

        self.newNumberSpawne()
        self.showMap()

        


    def showMap(self):
        for ligne in self.map:
            print(ligne)

    def moveCandidate(self,posLibre,pos,ReverseSense,vertical):

        caseValue = self.map[pos[1]][pos[0]]
        if posLibre != (None,None): ##ylibre != None and xlibre != None:##
            #deplace le numero/valeur
            self.map[pos[1]][pos[0]] = None
            self.map[posLibre[1]][posLibre[0]] = caseValue
            #affecte les possition du nouveaux candidat
            posCandidate = posLibre
            if vertical:
                #parcoure sur le l'axe vertical

                if ReverseSense:
                    sansparcoureligne = range(posCandidate[0],-1,-1)
                else:
                    sansparcoureligne = range(posCandidate[0]+1,self.longeurCoterMap)

                #on cherche la premier case vide 
                for xx in sansparcoureligne:
                    if self.map[pos[1]][xx] == None:
                        posLibre = (xx,pos[1])
                        break
            else:
                #parcoure sur le l'axe horizontal

                if ReverseSense:
                    sansparcoureligne = range(posCandidate[1],-1,-1)
                else:
                    sansparcoureligne = range(posCandidate[1]+1,self.longeurCoterMap)

                #on cherche la premier case vide 
                for yy in sansparcoureligne:
                    if self.map[yy][pos[0]] == None:
                        posLibre = (pos[0],yy)
                        break

        else:
            #affecte la possition du nouveau candidate
            posCandidate = pos
        
        return posLibre,posCandidate


    def fussion(self, direction):
        
        
        ##valeur pour connêtre le sans de baleillange dans la grille
        vertical = direction == "Right" or direction == "Left"
        ReverseSense = direction == "Down" or direction == "Right"

        #parcoure la carte ligne par ligne ou colonne par colonne
        for x in range(self.longeurCoterMap):

            #inisiation des valeurs avant le parcoure
            #valeur de la case Candidates à la promution
            promotionCandidates = None
            #position de la case Candidates
            posCandidate = (None,None)
            #position du premier espace libre
            posLibre = (None,None)

            #sens du parcoure de la ligne ou colonne 
            sensparcoure = range(self.longeurCoterMap)
            if ReverseSense:
                sensparcoure = reversed(sensparcoure)
                
            for y in sensparcoure:
                #si on baleille en vertical on échange les valeur de x et y
                if vertical :
                    #lastx enregistre la valeur de basse de x
                    lastx = x
                    x = y
                    y = lastx

                CaseValue = self.map[y][x]

                
                if CaseValue != None:
                    #is il ne peut pas avoire de promotion/fusion
                    if promotionCandidates == None:
                        
                        
                        posLibre,posCandidate = self.moveCandidate(posLibre,(x,y),ReverseSense,vertical)

                        #affecte la vouleur du nouveau Candidate à la promotion/fusion
                        promotionCandidates = CaseValue
                        

                    else:

                        if CaseValue == promotionCandidates:
                            #fussion la case Value avec le candidat
                            self.map[posCandidate[1]][posCandidate[0]] = CaseValue*2
                            self.map[y][x] = None
                            promotionCandidates = None
                            
                            #undique un espace libre si il n'y en avais pas
                            if posLibre == (None,None):##ylibre==None:
                                posLibre = (x,y)

                        else:
                            #la fussion n'est pas possible
                            posLibre,posCandidate = self.moveCandidate(posLibre,(x,y),ReverseSense,vertical)

                            #affecte la vouleur du nouveau Candidate à la promotion/fusion
                            promotionCandidates = CaseValue
                            


                # si il n'y avais pas d'espace libre on indique qu'il existe ce lui là
                elif posLibre == (None,None):
                    posLibre = (x,y)
                
                if vertical:
                    #remet la valeur de x
                    x = lastx
        

    def newNumberSpawne(self):


        ##avoire une avriavle à la place
        #compter le nombre de casse vide
        nbNone = 0
        for x in range(self.longeurCoterMap):
            for y in range(self.longeurCoterMap):
                if self.map[y][x] == None:
                    nbNone += 1
        
        #place le nouveau nombre
        numcase = randint(0,nbNone)
        for x in range(self.longeurCoterMap):
            for y in range(self.longeurCoterMap):
                if self.map[y][x] == None:
                    numcase -= 1
                    if numcase == 0:
                        if randint(0,10) < 1:
                            self.map[y][x] = 4
                        else:
                            self.map[y][x] = 2
                        
                        break

            if numcase == 0:
                break
        
    def doTurn(self,entre : str):

        match entre:
            case "Z":
                self.fussion("Top")
            case "S":
                self.fussion("Down")
            case "Q":
                self.fussion("Left")
            case "D":
                self.fussion("Right")
        
        self.newNumberSpawne()
        self.showMap()

    

           



if __name__ == "__main__":
    g = Game()
    while True:
        entre = input("choisie l'action\n")
        g.doTurn(entre)
    