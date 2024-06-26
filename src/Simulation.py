from Neat import *
from Game import *
from copy import deepcopy

class Simulation:

    def __init__(self) -> None:
        self.neat = Neat(16,4,1)
    

    def lunchGeneration(self):
        if self.neat.listOfPopulation == []:
            print("il n'y a personne !!")
        
        for individue in self.neat.listOfPopulation:
            self.lunchindividue(individue)


    def lunchindividue(self,individue : NodeNetwork):
        game = Game()


        gameover = False


        while gameover == False:

            oldmap = deepcopy(game.map)

            map = game.map
            inputt = []
            for ligne in map:
                for elem in ligne:
                    if elem == None:
                        inputt.append(0)
                    else:
                        inputt.append(elem)
            
            
            res = individue.Execute(inputt)

            idmax = list(res.keys())[0]
            for id in res:
                if res[id] > res[idmax]:
                    idmax = id
            
            dirrection = ""
            match idmax:
                case 17:
                    dirrection = "Top"
                case 18:
                    dirrection = "Down"
                case 19:
                    dirrection = "Left"
                case 20:
                    dirrection = "Right"


            gameover = game.doTurn(dirrection)

            if oldmap == game.map:
                gameover = True

            game.showMap()



if __name__ == "__main__":
    s = Simulation()
    s.neat.CreateEmtyGeneration()
    s.lunchGeneration()

        