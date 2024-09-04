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

        couche, connection = self.individu.CreateCouchesAndConnections()
        result = self.individu.Execute(data,couche, connection)

        gameOver = self.game.playAction(result)
        self.individuWindow.gameview.updateGrid(self.game.map)
        self.individuWindow.updateGameStatus(result,self.game.getscore(),gameOver)

    def restart(self,event):

        self.game = Game()

        self.individuWindow.gameview.updateGrid(self.game.map)
        self.individuWindow.updateGameStatus("?",0,False)



        

        
