from typing import TYPE_CHECKING

from tkinter import *
from math import sqrt,ceil

# from NeatView.Controller import *
from NeatView.Controller.IndividuControleur import IndividuControleur
from NeatView.Controller.NavigationControleur import NavigationControleur
#if TYPE_CHECKING: from NeatView.Controller.IndividuControleur import IndividuControleur
from NeatView import *


class GenerationView(Frame):

    def __init__(self,master):
        super().__init__(master)


        #top
        top = Frame(self)

        self.leftarrow = Button(top,text="<")
        self.textGenerationNumber = Label(top,text="Generation 1")
        self.rightarrow = Button(top,text=">")

        self.leftarrow.pack(side="left")
        self.textGenerationNumber.pack(side="left")
        self.rightarrow.pack(side="left")

        #centre
        self.center = Frame(self)
        ## inisialisation Controleur
        NavigationControleur.Inisialisation(self)
        NavigationControleur.Goto(0)

        top.pack()
        self.center.pack(side="left")

        self.fixbutton(1,True,False)
        

    
    def updateView(self,generationNumber,haveNext,havePrevious) -> None:

        self.textGenerationNumber.config(text="Generation "+str(generationNumber))

        for key in self.center.children:
            self.center.children[key].grid_remove()

        population : list[IndividuView] = IndividuControleur.GetindividuView(self.center,generationNumber)

        nbIndividuLigne = 20#ceil(sqrt(len(population)))
        for index,indi in enumerate(population):
            indi.grid(row=index//nbIndividuLigne,column=index%nbIndividuLigne,padx=2,pady=2)

        
        self.fixbutton(generationNumber,haveNext,havePrevious)
        

    def fixbutton(self,generationNumber,haveNext,havePrevious):
        # désacrivation Bouton
        if haveNext:
            self.rightarrow.config(state=NORMAL)
            self.rightarrow.bind("<Button-1>",lambda event: NavigationControleur.Next(generationNumber,event))
        else:
            self.rightarrow.config(state=DISABLED)


        if havePrevious:
            self.leftarrow.config(state=NORMAL)
            self.leftarrow.bind("<Button-1>",lambda event: NavigationControleur.Previous(generationNumber,event))
        else:
            self.leftarrow.config(state=DISABLED)


        