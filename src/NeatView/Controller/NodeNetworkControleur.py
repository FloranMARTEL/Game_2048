from tkinter import *
import time

from NeatView import ConnectionInfoView

class NodeNetworkControleur():

    def __init__(self,connectioninfoView : ConnectionInfoView) -> None:
        self.connectioninfoView = connectioninfoView
        self.show = False
        
        self.connectioninfoView.bind('<Leave>', self.onLeave)


    def onEnter(self,event):

        if not self.show:

            self.connectioninfoView.place(x=event.x-20,y=event.y-20)
            self.show = True


    def onLeave(self,event):

        if self.show:
            self.connectioninfoView.place_forget()
            self.show = False

