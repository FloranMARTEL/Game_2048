from tkinter import *
from NeatView import *

class individuView(Frame):

    def __init__(self,master,number : int):

        super().__init__(master)

        textNumber : Label= Label(self,text=str(number))

        textNumber.pack()