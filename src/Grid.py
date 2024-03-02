from tkinter import Frame
from Block import Block


class Grid(Frame):

    def __init__(self,master,map) -> None:
        super().__init__(master,width=400,height=400)
        

        self.updateGrid(map)
    
    def updateGrid(self,map):
        
        #retirer tout les élément dans la grid
        block = self.winfo_children()
        for indexElem in reversed(range(len(block))):
            block[indexElem].destroy()
        
        for y in range(4):
            for x in range(4):
                carre = Block(self,map[y][x])
                carre.grid(row=y,column=x,sticky="nesw")