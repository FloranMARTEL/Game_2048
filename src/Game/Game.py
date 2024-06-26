
from random import randint
from copy import deepcopy

from Neat import NeatGame


class Game(NeatGame):

    def __init__(self) -> None:
        self.status = "run"
        self.map = [ [None for j in range(4)] for i in range(4)]
        self.longeurCoterMap = len(self.map)
        self.newNumberSpawne()


    def showMap(self):
        for ligne in self.map:
            print(ligne)

    def moveCandidate(self,map ,posLibre,pos,ReverseSense,vertical):
        longeurCoterMap = len(map)

        caseValue = map[pos[1]][pos[0]]
        if posLibre != (None,None):
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
                    if self.map[yy][pos[0]] == None:
                        posLibre = (pos[0],yy)
                        break
            modification = True

        else:
            #affecte la possition du nouveau candidate
            posCandidate = pos
            modification = False
        
        return map, posLibre,posCandidate, modification


    def fussion(self,map, direction):
        
        longeurCoterMap = len(map)
        ##valeur pour connêtre le sans de baleillange dans la grille
        vertical = direction == "Right" or direction == "Left"
        ReverseSense = direction == "Down" or direction == "Right"

        modification = False

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
                        
                        
                        map, posLibre,posCandidate,modifi = self.moveCandidate(map, posLibre,(x,y),ReverseSense,vertical)
                        modification = modification or modifi
                        #affecte la vouleur du nouveau Candidate à la promotion/fusion
                        promotionCandidates = CaseValue
                        

                    else:

                        if CaseValue == promotionCandidates:
                            #fussion la case Value avec le candidat
                            map[posCandidate[1]][posCandidate[0]] = CaseValue*2
                            map[y][x] = None
                            promotionCandidates = None
                            modification = True
                            
                            #undique un espace libre si il n'y en avais pas
                            if posLibre == (None,None):
                                posLibre = (x,y)

                        else:
                            #la fussion n'est pas possible
                            map, posLibre,posCandidate,modifi = self.moveCandidate(map,posLibre,(x,y),ReverseSense,vertical)
                            modification = modification or modifi
                            #affecte la vouleur du nouveau Candidate à la promotion/fusion
                            promotionCandidates = CaseValue
                            


                # si il n'y avais pas d'espace libre on indique qu'il existe ce lui là
                elif posLibre == (None,None):
                    posLibre = (x,y)
                
                if vertical:
                    #remet la valeur de x
                    x = lastx
        
        return map, modification
        

    def newNumberSpawne(self):

        ##avoire une avriavle à la place
        nbNone = self.nbZoneLibre()
        
         
        #place le nouveau nombre
        numcase = randint(1,nbNone)
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
            
    def nbZoneLibre(self):
        #compter le nombre de casse vide
        nbNone = 0
        for x in range(self.longeurCoterMap):
            for y in range(self.longeurCoterMap):
                if self.map[y][x] == None:
                    nbNone += 1
        return nbNone

    def getpoint(self):
        point = 0
        for ligne in self.map:
            for element in ligne:
                if element != None:
                    point += element
        
        return point
    
    def checkGameOver(self):
        nbZoneLibre = self.nbZoneLibre()
        if nbZoneLibre == 0:

            dirrection = ("Top","Down","Left","Right")
            for d in dirrection:
                _,modif = self.fussion(deepcopy(self.map),d)
                if modif == True:
                    return False
            
            return True
        
        return False
        
    def doTurn(self,action : str):
        if action not in ("Top","Down","Left","Right"):
            raise ValueError

        
        self.map,thereIsModification = self.fussion(self.map, action)
        
        if thereIsModification:
            amap = deepcopy(self.map)
            self.newNumberSpawne()

    
        return self.checkGameOver()
        
    def playAction(self, action):
        self.doTurn(action)

    def getinput(self):
        return  [j for sub in self.map for j in sub]

    

           



if __name__ == "__main__":

    g = Game()
    g.map = [ [None for j in range(4)] for i in range(4)]
    g.map[1][3] = 2
    g.map[0][3] = 4
    g.map[0][2] = 2
    g.map[0][1] = 4
    g.map[2][0] = 2
    g.showMap()
    while True:
        entre = input("choisie l'action\n")
        g.doTurn(entre)
        g.showMap()
    