from Neat import Neat
from Game import Game 

n = Neat(16,4,1000,Game)

n.CreateEmtyGeneration()

for i in range(1000):
    print(f"----------------{i}-------------")
    n.classificationOfSpecies()
    #print(n.listOfspecies)
    r = n.PopulationPlay()
    print(sorted(r,key=lambda i:i.score))
    n.kill()
    n.reproduction()
    n.mutation()
