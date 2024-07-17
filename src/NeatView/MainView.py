from tkinter import *
from NeatView import *

class MainView(Tk):

    def __init__(self):
        super().__init__()


        left = GenerationView(self)



        left.grid(row=0,column=0)
        