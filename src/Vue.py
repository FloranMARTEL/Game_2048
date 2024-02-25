from tkinter import *

from Game import Game
from Grid import Grid

class MainView:

    def __init__(self) -> None:

        self.window = Tk()


        self.game = Game()

        grid = Grid(self.window)

        grid.pack(expand=1)

        self.window.bind("<KeyPress>", lambda e : print(e.char))



        
    def show(self):
        self.window.mainloop()


if __name__ == "__main__":
    vue = MainView()
    vue.show()