from tkinter import *

from View import Grid

from NeatView import ConnectionInfoView

from NeatView.Controller.NodeNetworkControleur import NodeNetworkControleur

class IndividuWindow(Toplevel):

    def __init__(self,number : int,rank : int,score : int,race : int,nodes :dict,connections : list,carte : list):
        super().__init__()
        #self.geometry("800x450")
        self.title("individu : "+str(number))

        #var
        self.number : int = number
        self.rank : int = rank
        self.score : int = score
        self.race : int = race

        self.nodes : dict = nodes
        self.connections = connections

        ##view

        #top
        self.generateTopView()

        #midel
        longeur = 800
        hauteur = 400

        self.canvaNodeNetwork = Canvas(self, width=longeur, height=hauteur, bg='ivory')
        self.updateCanva(nodes,connections,longeur,hauteur)
        self.canvaNodeNetwork.pack(side="top",fill="x")

        #midel 2
        self.generateMidel2View()

        # end
        self.generateEndView(carte)

    
    def updateGameStatus(self,action : str,score : int, gameOver):

        self.labelAction.config(text="Action : "+str(action))
        self.labelScore.config(text="Score : "+str(score))
        self.labelGameOver.config(text="GameOver : "+str(gameOver))


    def generateTopView(self):
        infoBar = Frame(self,borderwidth=1, relief="solid")

        textIdentifiant = Label(infoBar , text="individu : "+str(self.number))
        textRank = Label(infoBar , text="rank : "+ str(self.rank))
        textScore = Label(infoBar , text="score : "+ str(self.score))
        textRace = Label(infoBar , text="race : "+ str(self.race))

        padxtext = 2
        textIdentifiant.pack(side="left",padx=padxtext)        
        textRank.pack(side="left",padx=padxtext)
        textScore.pack(side="left",padx=padxtext)
        textRace.pack(side="right", padx=padxtext)
        
        infoBar.pack(side="top",fill="x")


    def generateMidel2View(self):
        gamebar = Frame(self,borderwidth=1, relief="solid")

        self.buttonStart = Button(gamebar , text="Start") ##not make
        self.buttonNext = Button(gamebar , text=">")

        padxtext = 2
        self.buttonStart.pack(side="left",padx=padxtext)        
        self.buttonNext.pack(side="left",padx=padxtext)
        
        gamebar.pack(side="top",fill="x")

    
    def generateEndView(self,carte):
        gameFrame = Frame(self)

        self.gameview = Grid(gameFrame,carte,200,200)

        infoGame = Frame(gameFrame)
        
        self.labelAction = Label(infoGame,text="Action : ?")
        self.labelScore = Label(infoGame,text="Score : 0")
        self.labelGameOver = Label(infoGame,text="GameOver : false")

        self.labelAction.pack(side="top")
        self.labelScore.pack(side="top")
        self.labelGameOver.pack(side="top")

        infoGame.pack(side="right",fill="both")
        self.gameview.pack(side="left")
        

        gameFrame.pack(side="top")




    def updateCanva(self,nodes,connections,longeur,hauteur):

        marging = 30

        tailleCercle = 20
        moitierCercle = tailleCercle/2
        

        #Dimenstion / posstion
        # if len(node) > 0

        firstNode = nodes[next(iter(nodes))]

        minH = firstNode["y"]
        maxH = firstNode["y"]
        minL = firstNode["x"]
        maxL = firstNode["x"]
        for key, node in nodes.items():
            if node["y"] > maxH:
                maxH = node["y"]
            if node["y"] < minH:
                minH = node["y"]

            if node["x"] > maxL:
                maxL = node["x"]
            if node["x"] < minL:
                minL = node["x"]

        if (maxH - minH) == 0:
            multiH = 1
        else:
            multiH = (hauteur-(marging*2)) /(maxH - minH)


        if (maxL - minL) == 0:
            multiL = 1
        else:
            multiL = (longeur-(marging*2)) /(maxL - minL)

        
        

        #color Connections
        if len(connections) != 0:
            maxValueConnection = connections[0]["value"]
            minValueConnection = connections[0]["value"]
            for connection in connections:
                if connection["value"] > maxValueConnection:
                    maxValueConnection = connection["value"]
                
                if connection["value"] < minValueConnection:
                    minValueConnection = connection["value"]
            
            if (maxValueConnection - minValueConnection) == 0:
                coefCouler = 1
            else:
                coefCouler = 255/(maxValueConnection - minValueConnection)
            


            for connection in connections:
                
                sx = nodes[connection["source"]]["x"] * multiL + marging
                sy = nodes[connection["source"]]["y"] * multiH + marging

                dx = nodes[connection["destination"]]["x"] * multiL + marging
                dy = nodes[connection["destination"]]["y"] * multiH + marging

                color = "#C8C8C8"
                if connection["enabel"]:
                    redcolor = int((connection["value"]-minValueConnection) * coefCouler)
                    bluecolor = 255 - redcolor

                    color = f"#{format(redcolor, '02x')}00{format(bluecolor, '02x')}"

                idconnection = self.canvaNodeNetwork.create_line(sx,sy,dx,dy, width=1, fill=color)

                #bind connetion
                connectionInfo = ConnectionInfoView(self,connection["num"],connection["value"],connection["enabel"])

                nodeNetworkControleur = NodeNetworkControleur(connectionInfo)
                self.canvaNodeNetwork.tag_bind(idconnection,'<Enter>', nodeNetworkControleur.onEnter)


            
        for key, node in nodes.items():
            x = node["x"] * multiL + marging - moitierCercle
            y = node["y"] * multiH + marging - moitierCercle

            xText = x+moitierCercle
            yText = y+moitierCercle

            self.canvaNodeNetwork.create_oval(x,y,x+tailleCercle,y+tailleCercle,width=1,outline="#000000",fill="white")
            self.canvaNodeNetwork.create_text(xText,yText,text=str(key))

        


