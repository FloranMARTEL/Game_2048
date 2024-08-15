from tkinter import *
from NeatView import *

class MainView(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("650x400")
        self.title("ViewNeat")


        left = GenerationView(self)

        right = SettingsView(self)

        self.grid_columnconfigure(0, weight=1)

        left.grid(row=0,column=0,sticky="nsew")
        right.grid(row=0,column=1,sticky="ns")
        