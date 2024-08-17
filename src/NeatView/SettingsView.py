from tkinter import *
from NeatView.Controller import *


class SettingsView(Frame):

    def __init__(self,master) -> None:
        super().__init__(master,borderwidth=2, relief="solid")

        #new
        self.buttonNewGeneration = Button(self,text="New")


        #goto
        navigation = Frame(self)
    
        textGoTo = Label(navigation,text="Go to")
        self.entryGoTo = Entry(navigation)
        self.buttonGoTo = Button(navigation,text="➩")

        textGoTo.grid(row=0,column=0)
        self.entryGoTo.grid(row=0,column=1)
        self.buttonGoTo.grid(row=0,column=2)


        self.buttonNewGeneration.pack(side="top")
        navigation.pack(side="top")

        self.buttonGoTo.bind("<Button-1>",lambda event: NavigationControleur.TryGoTo(self.entryGoTo,event))


