from tkinter import *
from NeatView import *

from typing import TYPE_CHECKING


class IndividuView(Button):#(Frame):

    def __init__(self,master,generation: int,number : int,score : int):

        super().__init__(master,text=str(number)+"\nS = "+str(score))

        from NeatView.Controller import IndividuControleur


        self.bind("<Button-1>", lambda event: IndividuControleur.LunchIndivuduWindow(generation,number))


