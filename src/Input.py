from tkinter import Event,Frame
from Game import Game

class Input:

    def __init__(self,vue,grid: Frame,game : Game) -> None:
        self.vue = vue
        self.grid = grid
        self.game = game

    def OnKeyPressed(self,e : Event):
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
            self.vue.gameover()
            
        # c'est la fin
        
        self.grid.updateGrid(self.game.map)
        
        
                