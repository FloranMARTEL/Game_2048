from tkinter import *
from NeatView import *

class MainView(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("650x400")
        self.title("ViewNeat")

        #left
        self.generationView :GenerationView = GenerationView(self)

        #right
        self.settingsView : SettingsView = SettingsView(self)

        self.grid_columnconfigure(0, weight=1)

        self.generationView.grid(row=0,column=0,sticky="nsew")
        self.settingsView.grid(row=0,column=1,sticky="ns")
        