from Neat import *
from Game import *
import random

class Neat():

    def __init__(self,nbinput : int,nboutput : int,nbpopulation : int) -> None:
        self.nbinput = nbinput
        self.nboutput = nboutput
        self.nbpopulation = nbpopulation
        self.listOfPopulation = []

        self.listNode = {}
        self.listConnection = {}

        self.emptyNoraleNetWork : NodeNetwork = NodeNetwork.NewNodeNetwork(nbinput,nboutput)

        for node in self.emptyNoraleNetWork.nodes:
            self.listNode[node.innovationNumber] = node
        

        self.c1 = 1
        self.c2 = 1
        self.c3 = 1
        
    def CreateEmtyGeneration(self):
        self.listOfPopulation  = [self.emptyNoraleNetWork.copy()]*self.nbpopulation



    def distance(self,Nn1 : NodeNetwork, Nn2: NodeNetwork):
        
        disjoint : int = 0
        excess : int = 0
        value_diff : float = 0
        similar : int = 0

        connectionNn1 = Nn1.connections.sort(key=lambda connection: connection.innovationNumber)
        connectionNn2 = Nn2.connections.sort(key=lambda connection: connection.innovationNumber)

        
        index1 : int = 0
        index2 : int = 0

        while index1 <= len(connectionNn1) and index2 <= len(connectionNn2):

            con1 : Connection = connectionNn1[index1]
            con2 : Connection = connectionNn2[index2]

            if con1.innovationNumber == con2.innovationNumber:
                # similaire
                similar +=1
                #différence de valeur
                value_diff += abs(con1.value - con2.value)

                index1 += 1
                index2 += 1
            elif con1.innovationNumber < con2.innovationNumber:
                #disjoint de 2
                disjoint += 1

                index1 += 1
            else:
                #disjoint de 1
                disjoint += 1

                index1 += 1

        if index1 == 0:
            excess = len(connectionNn2) - index2
        else:
            excess = len(connectionNn1) - index1

        value_diff /= similar

        N : int
        if len(connectionNn1) > len(connectionNn2):
            N = len(connectionNn1)
        else:
            N = len(connectionNn2)

        if N < 20:
            N=1

        result = (self.c1 * disjoint / N) + (self.c2 * excess / N) +( self.c3 * value_diff /N)

        return result


    def crossover(self,Nn1 : NodeNetwork, Nn2: NodeNetwork):

        ## Nn1 à le meilleur score

        connectionNn1 = Nn1.connections.sort(key=lambda connection: connection.innovationNumber)
        connectionNn2 = Nn2.connections.sort(key=lambda connection: connection.innovationNumber)

        newConnections :list[Connection]= []
        newNodes : list[Node] = []

        index1 : int = 0
        index2 : int = 0
        while index1 <= len(connectionNn1) and index2 <= len(connectionNn2)

            con1 : Connection = connectionNn1[index1]
            con2 : Connection = connectionNn2[index2]
            if con1.innovationNumber == con2.innovationNumber:
                
                if random.random() > 0.5:
                    newConnections.append(con1)
                else:
                    newConnections.append(con2)
                
                index1 += 1
                index2 += 1
            
            elif con1.innovationNumber < con2.innovationNumber:
                ##prend les inovation disjointe
                newConnections.append(con1)
                index1 += 1
            else:
                newConnections.append(con2)
                index2 += 1

        
        for con in newConnections:
            if con.nodeSource not in newNodes:
                newNodes.append(con.nodeSource)
            
            if con.nodeDestiantion not in newNodes:
                newNodes.append(con.nodeDestiantion)
        
        return NodeNetwork(newNodes,newConnections)

    
    

        
        


    


