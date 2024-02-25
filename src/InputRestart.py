from tkinter import Event
from Game import Game

class InputRestart:

    def __init__(self,window) -> None:
        self.window = window

    def restart(self):
        newgame = Game()
        