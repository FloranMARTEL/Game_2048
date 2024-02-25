from tkinter import Frame
from Block import Block


class Grid(Frame):

    def __init__(self,master) -> None:
        super().__init__(master,width=100,height=100)

        for y in range(4):
            for x in range(4):
                carre = Block(self,[ [None for j in range(4)] for i in range(4)])
                carre.grid(row=y,column=x,sticky="nesw")
    
    def updateGrid(self,map):
        
        #retirer tout les élément dans la grid
        block = self.children
        for indexElem in block:
            block[indexElem].grid_forget()
        
        for y in range(4):
            for x in range(4):
                carre = Block(self,map[y][x])
                carre.grid(row=y,column=x,sticky="nesw")