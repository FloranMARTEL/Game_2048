from Neat import Individual
from Game import Game
from NeatView import IndividuWindow

class GameControleur():

    def __init__(self,individu : Individual,game : Game ,individuWindow : IndividuWindow) -> None:

        self.individu : Individual = individu
        self.game : Game = game
        self.individuWindow : IndividuWindow = individuWindow

    def nextAction(self,event):

        data = self.game.getinput()
        result = self.individu.Execute(data)

        idmax = list(result.keys())[0]
        for id in result:
            if result[id] > result[idmax]:
                idmax = id
        
        direction = ""
        match idmax:
            case 17:
                direction = "Top"
            case 18:
                direction = "Down"
            case 19:
                direction = "Left"
            case 20:
                direction = "Right"

        gameOver = self.game.playAction(direction)
        self.individuWindow.gameview.updateGrid(self.game.map)
        self.individuWindow.updateGameStatus(direction,self.game.getscore(),gameOver)

    def restart(self,event):

        self.game = Game()

        self.individuWindow.gameview.updateGrid(self.game.map)
        self.individuWindow.updateGameStatus("?",0,False)



        

        
