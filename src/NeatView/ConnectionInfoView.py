from tkinter import *

class ConnectionInfoView(Frame):

    def __init__(self,master,numInovation : int,valeur : int, enable : int):
        super().__init__(master)

        textnuminovation = Label(self,text="numéro d'inovation : " + str(numInovation))
        textvaleur = Label(self,text="valeur : " + str(valeur))
        textenable = Label(self,text="enable : " + str(enable))

        textnuminovation.pack()
        textvaleur.pack()
        textenable.pack()


