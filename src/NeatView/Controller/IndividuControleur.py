from Neat import DAOJson,Individual
from NeatView import *
from NeatView import IndividuView
from Game import Game

from NeatView.Controller import *

class IndividuControleur():

    @staticmethod
    def LunchIndivuduWindow(generation : int, numberIndividu : int):



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

        population = DAOJson.Read(generation)

        populationView = [None]*len(population)
        for index, indi in enumerate(population):
            
            populationView[index] = IndividuView(master,generation,indi["individualMember"])

        return populationView