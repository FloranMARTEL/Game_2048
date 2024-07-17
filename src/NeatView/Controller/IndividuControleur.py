from Neat import DAOJson
from NeatView import *

class IndividuControleur():

    def __init__(self):
        pass

    def getindividuView(master, generation : int):

        population = DAOJson.Read(generation)

        populationView = []*len(population)
        for index, indi in enumerate(population):
            
            population[index] = individuView(master,indi["individualMember"])

        return populationView