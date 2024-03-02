from tkinter import *

from Game import Game
from Grid import Grid
from Input import Input
from InputRestart import InputRestart

class MainView:

    def __init__(self) -> None:

        self.window = Tk()

        self.textGameOver = None

        game = Game()
        self.grid = Grid(self.window,game.map)
        
        self.grid.pack(expand=1)

        interaction = Input(self,self.grid,game)
        self.window.bind("<KeyPress>", interaction.OnKeyPressed)


    def gameover(self):
        self.window.unbind("<KeyPress>")
        self.textGameOver = Label(self.window,text="GameOver")
        self.textGameOver.pack(expand=1)

        interaction = InputRestart(self)
        self.window.bind("<Return>",interaction.restart)

    def restart(self,game : Game):
        self.window.unbind("<Return>")
        self.textGameOver.pack_forget()

        self.grid.updateGrid(game.map)



        interaction = Input(self,self.grid,game)
        self.window.bind("<KeyPress>", interaction.OnKeyPressed)
        

        
    def show(self):
        self.window.mainloop()


if __name__ == "__main__":
    vue = MainView()
    vue.show()