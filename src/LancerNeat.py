from Neat import Neat
from Neat import DAOJson
from Game import Game 

n = Neat(16,4,10,Game)

n.CreateEmtyGeneration()

for i in range(10):
    print(f"----------------{i}-------------")
    n.classificationOfSpecies()
    #print(n.listOfspecies)
    r = n.PopulationPlay()
    print(sorted(r,key=lambda i:i.score))
    DAOJson.Creat(i,r)
    n.kill()
    n.reproduction()
    n.mutation()
