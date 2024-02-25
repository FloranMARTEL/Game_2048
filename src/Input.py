from tkinter import Event
from Game import Game

class Input:

    def __init__(self,grid,game : Game) -> None:
        self.grid = grid
        self.game = game

    def OnKeyPressed(self,e : Event):
        print(type(e))
        key = e.char
        
        match key:
            case "z":
                self.game.fussion("Top")
            case "s":
                self.game.fussion("Down")
            case "q":
                self.game.fussion("Left")
            case "d":
                self.game.fussion("Right")
            
        itCan = self.game.newNumberSpawne()

        if itCan == False:
            self.game.status = "GameOver"
            pass
        # c'est la fin
        
        self.grid.updateGrid(self.game.map)
        
        
                