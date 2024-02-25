from tkinter import Event
from Game import Game

class InputRestart:

    def __init__(self,MainVue) -> None:
        self.MainVue = MainVue

    def restart(self,e : Event):
        newgame = Game()
        self.MainVue.restart(newgame)

        