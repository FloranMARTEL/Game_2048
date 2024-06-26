from Neat import *

class Neat():

    def __init__(self,nbinput : int,nboutput : int,nbpopulation : int,Game : type) -> None:
        self.nbinput = nbinput
        self.nboutput = nboutput
        self.nbpopulation = nbpopulation
        self.listOfPopulation = []

        self.listNode = {}
        self.listConnection = {}

        self.emptyNoraleNetWork : NodeNetwork = NodeNetwork.NewNodeNetwork(nbinput,nboutput)

        for node in self.emptyNoraleNetWork.nodes:
            self.listNode[node.innovationNumber] = node

        self.Game = Game
        
    def CreateEmtyGeneration(self):
        self.listOfPopulation  = [self.emptyNoraleNetWork.copy()]*self.nbpopulation

    def PopulationPlay(self):
        for individu in self.listOfPopulation:
            curentgame : NeatGame = self.Game()
            input = curentgame.getinput()
            individu





    
    

        
        


    


