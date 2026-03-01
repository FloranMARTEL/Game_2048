from Neat import Neat
from Neat import DAOJson
from Game import Game 
nbpopulation = 100
n = Neat(16,4,nbpopulation,Game)

n.CreateEmtyGeneration()

#delet source
# for i in range(10):
#     DAOJson.Delete(i)

for i in range(200):
    print(f"---------------{i}--------------")
    #print("a")
    n.classificationOfSpecies()
    #print("b")

    r = n.PopulationPlay()
    #print("c")

    DAOJson.Creat(i,r)
    #print("d")

    n.kill()
    #print("e")

    n.reproduction()
    #print("f")

    n.mutation()
    #print("g")
