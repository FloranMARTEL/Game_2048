from Neat import *
from math import ceil,floor
import random

class Species:

    CoefCorespondance = 4

    def __init__(self,individuRéférent : Individual) -> None:
        self.nodeNetworkRéférent = individuRéférent.nodeNetwork.copy()
        self.individus = [individuRéférent]
    
    def isMemberofSpecies(self,individu: Individual) -> bool:
        return NodeNetwork.Distance(self.nodeNetworkRéférent,individu.nodeNetwork) < __class__.CoefCorespondance


    def addIndividu(self,individu):
        self.individus.append(individu)

    def clear(self):
        self.individus = []

    def bornNewIndividual(self):
        
        parent1: Individual = random.choice(self.individus)
        parent2: Individual = random.choice(self.individus)

        if parent1.score < parent2.score:
            vartemporaire = parent1
            parent1 = parent2
            parent2 = vartemporaire

        newNodeNetwork = NodeNetwork.Crossover(parent1.nodeNetwork,parent2.nodeNetwork)

        newIndividu = Individual(newNodeNetwork)

        return newIndividu


    def kill(self,pourcentage = 0.2):

        if pourcentage == 0:
            raise ValueError

        individuSorted = sorted(self.individus,key = lambda ind : ind.score)

        killnumber = floor(len(self.individus)*pourcentage)

        for index in range(killnumber):
            individuSorted[index].vivant = False

        self.individus = individuSorted[killnumber:]

    
    def scoreMoyen(self):

        totalscore = 0
        for indi in self.individus:
            totalscore += indi.score

        return totalscore / len(self.individus)


    def __str__(self) -> str:
        text = ""

        for i in self.individus:
            text += f" individu [{i.numindividu}];"
        
        return f"Species { '{' }{text} { '}' }"
    
    def __repr__(self) -> str:
        return self.__str__()
    

    