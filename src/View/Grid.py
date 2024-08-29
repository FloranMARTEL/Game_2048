from tkinter import Frame
from View import *


class Grid(Frame):

    def __init__(self,master,map,w:int=400,h:int=400) -> None:
        super().__init__(master,width=w,height=h)

        self.blockwidth = w/4
        self.blockheight = h/4
        

        self.updateGrid(map)
    
    def updateGrid(self,map):
        
        #retirer tout les élément dans la grid
        block = self.winfo_children()
        for indexElem in reversed(range(len(block))):
            block[indexElem].destroy()
        
        for y in range(4):
            for x in range(4):
                carre = Block(self,map[y][x],self.blockwidth,self.blockheight)
                carre.grid(row=y,column=x,sticky="nesw")