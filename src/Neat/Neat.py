from Neat import *

class Neat():

    def __init__(self,nbinput : int,nboutput : int,nbpopulation : int) -> None:
        self.nbinput = nbinput
        self.nboutput = nboutput
        self.nbpopulation = nbpopulation
        self.listOfPopulation = []

        self.listNode = {}
        self.listConnection = {}

        self.emptyNoraleNetWork : NodeNetwork = NodeNetwork.NewNodeNetwork(nbinput,nboutput)

        for node in self.emptyNoraleNetWork.nodes:
            self.listNode[node.invoationNumber] = node
        
    def CreateEmtyGeneration(self):
        self.listOfPopulation  = [self.emptyNoraleNetWork.copy()]*self.nbpopulation
    
    

        
        


    


