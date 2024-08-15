from tkinter import *
from math import sqrt,ceil

from NeatView.Controller import *
from NeatView import *


class GenerationView(Frame):

    def __init__(self,master):
        super().__init__(master)

        #top
        top = Frame(self)

        self.leftarrow = Button(top,text="<")
        self.textGenerationNumber = Label(top,text="Generation X")
        self.rightarrow = Button(top,text=">")

        self.leftarrow.grid(row=0,column=0)
        self.textGenerationNumber.grid(row=0,column=1)
        self.rightarrow.grid(row=0,column=2)

        #centre
        self.center = Frame(self)
        population : list[individuView] = IndividuControleur.getindividuView(self.center,1)

        nbIndividuLigne = ceil(sqrt(len(population)))
        for index,indi in enumerate(population):
            indi.grid(row=index//nbIndividuLigne,column=index%nbIndividuLigne,padx=2,pady=2)

       
        top.grid(row=0, column=0)
        self.center.grid(row=1, column=0)


        