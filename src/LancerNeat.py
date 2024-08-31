from Neat import Neat
from Neat import DAOJson
from Game import Game 
nbpopulation = 1000
n = Neat(16,4,nbpopulation,Game)

n.CreateEmtyGeneration()

#delet source
# for i in range(10):
#     DAOJson.Delete(i)

for i in range(1000):
    print(f"----------------{i}-------------")
    print("a")
    n.classificationOfSpecies()
    print("b")

    #print(n.listOfspecies)
    r = n.PopulationPlay()
    print("c")

    #print(sorted(r,key=lambda i:i.score))
    DAOJson.Creat(i,r)
    print("d")

    n.kill()
    print("e")

    n.reproduction()
    print("f")

    n.mutation()
    print("g")
