from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from NeatView import GenerationView

    
from Neat import DAOJson

from NeatView.Controller import *
from tkinter import Entry,messagebox

class NavigationControleur:

    GENERATIONView : "GenerationView" = None
    
    @staticmethod
    def Inisialisation(generationView : "GenerationView"):
        __class__.GENERATIONView = generationView


    @staticmethod
    def Next(curentGeneration,event):
        __class__.Goto(curentGeneration+1,event)


    @staticmethod
    def Previous(curentGeneration,event):
        __class__.Goto(curentGeneration-1,event)
    

    @staticmethod
    def TryGoTo(entryGeneration : Entry ,event):

        value : str = entryGeneration.get()
        if not value.isdigit():
            messagebox.showerror('Value Error', 'Error: La valeur n\'est pas un nombre positife')
            return
        
        intValue = int(value)

        if not DAOJson.GenerationExist(intValue):
            messagebox.showerror('Value Error', 'Error: Le génération n\'existe pas')
            return
        
        entryGeneration.delete(0, 'end')

        __class__.Goto(intValue,event)
        

    @staticmethod
    def Goto(generationNumber : int,event = None):
        #check if it is possible
        haveNext = DAOJson.GenerationExist(generationNumber+1)
        havePrevious = DAOJson.GenerationExist(generationNumber-1)
        __class__.GENERATIONView.updateView(generationNumber,haveNext,havePrevious)




