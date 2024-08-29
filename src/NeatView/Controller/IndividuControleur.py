from Neat import DAOJson,Individual
from Game import Game

from NeatView.Controller import *
#from NeatView.IndividuWindow import IndividuWindow


class IndividuControleur():

    @staticmethod
    def LunchIndivuduWindow(generation : int, numberIndividu : int):

        from NeatView.IndividuWindow import IndividuWindow

        #Model Game
        modelG = Game()
        map = modelG.map        

        #data

        individuData = DAOJson.ReadIndividu(generation,numberIndividu)


        individu = DAOJson.DictToIndividu(individuData)


        
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

        indiWin = IndividuWindow(number,rank,score,race,nodes,connections,map)

        #bind button
        gameControleur = GameControleur(individu,modelG,indiWin)
        indiWin.buttonNext.bind("<Button-1>", gameControleur.nextAction)
        indiWin.buttonStart.bind("<Button-1>", gameControleur.restart)


        indiWin.mainloop()
        #indiWin.focus_force()


    @staticmethod
    def GetindividuView(master, generation : int):
        from NeatView import IndividuView


        population = DAOJson.Read(generation)

        populationView = [None]*len(population)
        for index, indi in enumerate(population):
            
            populationView[index] = IndividuView(master,generation,indi["individualMember"])

        return populationView