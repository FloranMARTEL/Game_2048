from tkinter import Event,Frame
from Game import Game

class Input:

    def __init__(self,vue,grid: Frame,game : Game) -> None:
        self.vue = vue
        self.grid = grid
        self.game = game

    def OnKeyPressed(self,e : Event):
        key = e.char

        if key not in ("z","s","q","d"):
            return
        
        dirrection = ""
        match key:
            case "z":
                dirrection = "Top"
            case "s":
                dirrection = "Down"
            case "q":
                dirrection = "Left"
            case "d":
                dirrection = "Right"
            
        #joue le trourd
        gameover = self.game.doTurn(dirrection)
            
        # c'est la fin
        
        if gameover:
            self.game.status = "GameOver"
            self.vue.gameover()
            
        # c'est la fin
        
        self.grid.updateGrid(self.game.map)
        
        
                