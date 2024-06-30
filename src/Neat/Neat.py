from Neat import *

from copy import deepcopy
import random
from math import ceil,floor

class Neat():

    def __init__(self,nbinput : int,nboutput : int,nbpopulation : int,Game : type) -> None:
        self.nbinput = nbinput
        self.nboutput = nboutput
        self.nbpopulation = nbpopulation
        self.listOfPopulation : list[Individual] = []

        self.listOfspecies : list[Species] = []

        self.listNode = {}
        self.listConnection = {}

        self.emptyNoraleNetWork : NodeNetwork = NodeNetwork.NewNodeNetwork(nbinput,nboutput)

        for node in self.emptyNoraleNetWork.nodes:
            self.listNode[node.innovationNumber] = node

        self.Game = Game


        
    def CreateEmtyGeneration(self):
        self.listOfPopulation  = [Individual(self.emptyNoraleNetWork.copy()) for i in range(self.nbpopulation)]

    def clearAllSpecies(self):
        for species in self.listOfspecies:
            species.clear()

    def classificationOfSpecies(self):

        self.clearAllSpecies()

        for individu in self.listOfPopulation:

            findSpecies = False
            random.shuffle(self.listOfspecies)
            for species in self.listOfspecies:
                species : Species

                if species.isMemberofSpecies(individu):
                    findSpecies = True
                    species.addIndividu(individu)
                    break
            
            if not findSpecies:
                self.listOfspecies.append(Species(individu))





    


    def PopulationPlay(self):
        if self.listOfPopulation == []:
            print("il n'y a personne !!")

        for individu in self.listOfPopulation:
            curentgame : NeatGame = self.Game()
            individu.score = None #facultatife


            gameover = False
            while gameover == False:
                input : list[int]= curentgame.getinput()
                resultat : str = individu.Execute(input)
                
                idmax = list(resultat.keys())[0]
                for id in resultat:
                    if resultat[id] > resultat[idmax]:
                        idmax = id
                
                dirrection = ""
                match idmax:
                    case 17:
                        dirrection = "Top"
                    case 18:
                        dirrection = "Down"
                    case 19:
                        dirrection = "Left"
                    case 20:
                        dirrection = "Right"
                
                gameover = curentgame.playAction(dirrection)
                
            individu.score = curentgame.getscore()


        return self.listOfPopulation
    
    def kill(self,pourcentage = 0.2):

        for species in self.listOfspecies:
            species.kill(pourcentage)
        
        #kill individu
        index = 0
        while index < len(self.listOfPopulation):
            if self.listOfPopulation[index].vivant == False:
                del self.listOfPopulation[index]
            else:
                index += 1
        
        #kill species
        index = 0
        while index < len(self.listOfspecies):
            if len(self.listOfspecies[index].individus) <= 0:
                del self.listOfspecies[index]
            else:
                index += 1
    
    def reproduction(self):

        

        nbNouveauxEnfants = self.nbpopulation - len(self.listOfPopulation)

        total = 0

        for s in self.listOfspecies:
            total += s.scoreMoyen()

    
        listOfspeciesSorted = sorted(self.listOfspecies,key= lambda s: s.scoreMoyen(),reverse=True )

        for s in listOfspeciesSorted:
            nbEnfant = (s.scoreMoyen()/total)*nbNouveauxEnfants
            if s != listOfspeciesSorted[-1]:
                nbEnfant = ceil(nbEnfant)
            else:
                nbEnfant = floor(nbEnfant)
            
            for numEnfant in range(nbEnfant):
                nouvelenfant = s.bornNewIndividual()
                self.listOfPopulation.append(nouvelenfant)

    def mutation(self):

        for individu in self.listOfPopulation:
            individu.mutation()







        
