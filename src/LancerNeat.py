from Neat import Neat
from Game import Game 

n = Neat(16,4,2,Game)

n.CreateEmtyGeneration()
r= n.PopulationPlay()
print(r)