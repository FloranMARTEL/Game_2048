from tkinter import *

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


        self.buttonNewGeneration.pack(side="top")#.grid(row=0,column=0,sticky="ew")
        navigation.pack(side="top")#.grid(row=1,column=0)