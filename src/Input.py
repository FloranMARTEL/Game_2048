class Input:

    def __init__(self,grid,game) -> None:
        self.grid = grid
        self.game = game

    def OnKeyPressed(self,e):
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
        
        self.grid.updateGrid()
        
        
                