from Neat import *

class Individual:

    CptIndividu = 0 

    def __init__(self,nodeNetwork : NodeNetwork,numindividu : int|None = None, score : int|None = None) -> None:

        if numindividu == None:
            self.numindividu = __class__.CptIndividu
            __class__.CptIndividu += 1

            self.score = None
        else:
            self.numindividu = numindividu
            self.score = score

        self.nodeNetwork : NodeNetwork = nodeNetwork
        self.vivant = True

        

    def mutation(self):
        self.nodeNetwork.mutation()


    def Execute(self,inputs):
        return self.nodeNetwork.Execute(inputs)
    
    def __str__(self):
        return f"individu [{self.numindividu}] :{'{'} score = {self.score} {'}'}"
    
    
    def __repr__(self) -> str:
        return self.__str__()