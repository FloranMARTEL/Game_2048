from Neat import *

class Individual:

    CptIndividu = 0 

    def __init__(self,nodeNetwork : NodeNetwork) -> None:

        self.numindividu = __class__.CptIndividu
        __class__.CptIndividu += 1

        self.nodeNetwork : NodeNetwork = nodeNetwork
        self.score = None
        self.vivant = True

    def mutation(self):
        self.nodeNetwork.mutation()


    def Execute(self,inputs):
        return self.nodeNetwork.Execute(inputs)
    
    def __str__(self):
        return f"individu [{self.numindividu}] :{'{'} score = {self.score} {'}'}"
    
    
    def __repr__(self) -> str:
        return self.__str__()