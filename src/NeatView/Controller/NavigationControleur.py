from NeatView import GenerationView
from Neat import DAOJson

from NeatView.Controller import *

class NavigationControleur:

    def __init__(self,generationView : GenerationView) -> None:

        self.generationView : GenerationView = generationView


    def next(self,curentGeneration,event):
        self.goto(curentGeneration+1,event)

    def previous(self,curentGeneration,event):
        self.goto(curentGeneration-1,event)

    def goto(self,generationNumber : int,event = None):
        #check if it is possible
        haveNext = DAOJson.GenerationExist(generationNumber+1)
        havePrevious = DAOJson.GenerationExist(generationNumber-1)
        self.generationView.updateView(generationNumber,haveNext,havePrevious)




