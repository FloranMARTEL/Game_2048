from Neat import DAOJson
from NeatView import *
from NeatView import IndividuView

class IndividuControleur():

    @staticmethod
    def LunchIndivuduWindow(generation : int, numberIndividu : int):
        
        individuData = DAOJson.ReadIndividu(generation,numberIndividu)
        
        number : int = individuData["individualMember"]
        rank : int = 0
        score : int = individuData["score"]
        race : int = 0
        
        nodes = {}
        for node in individuData["nodeNetwork"]["nodes"]:
            nodes[node["innovationNumber"]] = {
                                            "x":node["positionX"],
                                            "y" : node["positionY"]
                                            }

        connections = [{
                        "num" : node["innovationNumber"],
                        "source":node["nodeSource"],
                        "destination":node["nodeDestiantion"],
                        "value":node["value"],
                        "enabel" : node["enabel"]
                        } for node in individuData["nodeNetwork"]["connections"] ]

        indiWin = IndividuWindow(number,rank,score,race,nodes,connections)
        indiWin.mainloop()
        #indiWin.focus_force()


    @staticmethod
    def GetindividuView(master, generation : int):

        population = DAOJson.Read(generation)

        populationView = [None]*len(population)
        for index, indi in enumerate(population):
            
            populationView[index] = IndividuView(master,generation,indi["individualMember"])

        return populationView