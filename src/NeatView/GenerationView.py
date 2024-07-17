from tkinter import *


class GenerationView(Frame):

    def __init__(self,master):
        super().__init__(master)

        top = Frame(self)

        self.leftarrow = Button(top,text="<")
        self.textGenerationNumber = Label(top,text="Generation X")
        self.rightarrow = Button(top,text=">")

        self.leftarrow.grid(row=0,column=0)
        self.textGenerationNumber.grid(row=0,column=1)
        self.rightarrow.grid(row=0,column=2)


        self.center = Frame(self)

        
        top.grid(row=1, column=0)
        self.center.grid(row=1, column=0)


        