from tkinter import Frame
from Block import Block


class Grid(Frame):

    def __init__(self,master) -> None:
        super().__init__(master,width=400,height=400)
        

        for y in range(4):
            for x in range(4):
                carre = Block(self,None)
                carre.grid(row=y,column=x,sticky="nesw")
    
    def updateGrid(self,map):
        
        #retirer tout les élément dans la grid
        block = self.winfo_children()
        for indexElem in reversed(range(len(block))):
            block[indexElem].destroy()
        
        for y in range(4):
            for x in range(4):
                carre = Block(self,map[y][x])
                carre.grid(row=y,column=x,sticky="nesw")