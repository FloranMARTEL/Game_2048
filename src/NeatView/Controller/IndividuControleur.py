from Neat import DAOJson
from NeatView import *

class IndividuControleur():

    def __init__(self):
        pass

    def getindividuView(master, generation : int):

        population = DAOJson.Read(generation)

        populationView = [None]*len(population)
        for index, indi in enumerate(population):
            
            populationView[index] = individuView(master,indi["individualMember"])

        return populationView