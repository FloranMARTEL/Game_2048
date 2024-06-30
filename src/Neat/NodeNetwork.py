from Neat import *
from copy import deepcopy
from random import shuffle,random,randint

class NodeNetwork():

    C1 = 1
    C2 = 1
    C3 = 1

    MAXVALUEMUTATION = 100

    ProbabilityTONewConnection = 0.5
    ProbabilityTOEnbeledConnection = 0.3
    ProbabilityTOValueOfConnection = 0.5
    ProbabilityTOValueOfConnectionRandomly = 0.1
    ProbabilityTONewNode = 0.2

    def __init__(self, nodes : list[Node], connections : list[Connection]) -> None:
        self.nodes : list[Node] = nodes
        self.connections : list[Connection] = connections
                    

    @staticmethod
    def NewNodeNetwork(nbinput : int,nboutput : int):
        nodes = []

        for numinputnode in range(nbinput):
            nodes.append(Node(0,numinputnode)) #nodes.append(Node(numinputnode+1,0,numinputnode))
        
        for numoutputnode in range(nboutput):
            nodes.append(Node(1,numoutputnode)) # nodes.append(Node(nbinput+numoutputnode+1,1,numoutputnode))

        return NodeNetwork(nodes,[])
    
    @staticmethod
    def Distance(Nn1, Nn2):
        Nn1 : NodeNetwork
        Nn2 : NodeNetwork

        
        disjoint : int = 0
        excess : int = 0
        value_diff : float = 0
        similar : int = 0

        connectionNn1 = sorted(Nn1.connections,key=lambda connection: connection.innovationNumber)
        connectionNn2 = sorted(Nn2.connections,key=lambda connection: connection.innovationNumber)

        index1 : int = 0
        index2 : int = 0

        while index1 < len(connectionNn1) and index2 < len(connectionNn2):

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

        if similar == 0:
            similar = 1

        value_diff /= similar

        N : int
        if len(connectionNn1) > len(connectionNn2):
            N = len(connectionNn1)
        else:
            N = len(connectionNn2)

        if N < 20:
            N=1

        result = (__class__.C1 * disjoint / N) + (__class__.C2 * excess / N) +( __class__.C3 * value_diff /N)

        return result


    #Nn1 is the nodeNetwork with the best score
    @staticmethod
    def Crossover(Nn1, Nn2):
        Nn1 : NodeNetwork
        Nn2 : NodeNetwork

        ## Nn1 à le meilleur score

        connectionNn1 = sorted(Nn1.connections,key=lambda connection: connection.innovationNumber)
        connectionNn2 = sorted(Nn2.connections,key=lambda connection: connection.innovationNumber)

        newConnections :list[Connection]= []
        newNodes : list[Node] = []

        index1 : int = 0
        index2 : int = 0
        while index1 < len(connectionNn1) and index2 < len(connectionNn2):

            con1 : Connection = connectionNn1[index1]
            con2 : Connection = connectionNn2[index2]
            if con1.innovationNumber == con2.innovationNumber:
                
                if random() > 0.5:
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

        #garder les node d'entrer et de sortie
        for n in Nn1.nodes:
            n : Node
            if n.positionX == 0 or n.positionX == 1:
                newNodes.append(n)

        for con in newConnections:
            if con.nodeSource not in newNodes:
                newNodes.append(con.nodeSource)
            
            if con.nodeDestiantion not in newNodes:
                newNodes.append(con.nodeDestiantion)
        
        return NodeNetwork(newNodes,newConnections)


    def copy(self):
        return NodeNetwork(deepcopy(self.nodes), deepcopy(self.connections))
    
    def mutation(self):

        if __class__.ProbabilityTONewConnection > random():
            self.mutationOfNewConnection()


        thereisConnection = len(self.connections) > 0
    
        if thereisConnection and __class__.ProbabilityTONewNode > random():
            self.MutationOfNewNode()

        if thereisConnection and __class__.ProbabilityTOValueOfConnection > random():
            if __class__.ProbabilityTOValueOfConnectionRandomly > random():
                self.mutationOfValueOfConnectionRandomly()
            else:
                self.mutationOfValueOfConnection()

        if thereisConnection and __class__.ProbabilityTOEnbeledConnection > random():
            self.mutationOfEnbeledConnection()
        

        
        

    def mutationOfNewConnection(self):
        shuffleListNode = deepcopy(self.nodes)
        shuffle(shuffleListNode)

        for nodeA in shuffleListNode:
            for nodeB in shuffleListNode:
                if nodeA.positionX != nodeB.positionX and nodeA.innovationNumber != nodeB.innovationNumber:
                    value = __class__.GETRandomValue()

                    if nodeA.positionX < nodeB.positionX:
                        newconnection = Connection(nodeA,nodeB,value)
                    else:
                        newconnection = Connection(nodeB,nodeA,value)

                    if newconnection not in self.connections:
                        self.connections.append(newconnection)
                        return True
        
        return False

    def mutationOfEnbeledConnection(self):
        
        indexConnection = self.getrandomindexofconnection()
        self.connections[indexConnection].enabel = not self.connections[indexConnection].enabel

    def mutationOfValueOfConnection(self):

        indexConnection = self.getrandomindexofconnection()
        self.connections[indexConnection].value = self.connections[indexConnection].value + __class__.GETRandomValue()

    def mutationOfValueOfConnectionRandomly(self):

        indexConnection = self.getrandomindexofconnection()
        self.connections[indexConnection].value = __class__.GETRandomValue()

    def MutationOfNewNode(self):
        indexConnection = self.getrandomindexofconnection()
        c : Connection = self.connections[indexConnection]


        nodeS = c.nodeSource
        nodeD = c.nodeDestiantion

        newposX = (nodeS.positionX+nodeD.positionX) /2
        newposY = (nodeS.positionX+nodeD.positionX) /2
        newNode = Node(newposX,newposY)

        newConnectionA = Connection(newNode,nodeD,c.value,c.enabel)
        newConnectionB = Connection(nodeD,newNode,1)

        c.enabel = False
        self.nodes.append(newNode)
        self.connections.append(newConnectionA)
        self.connections.append(newConnectionB)


    def Execute(self,inputs):

        ##liste des chouche
        couches : list[list[Node]] = []
        lienConnection : dict[int,(int,list[Connection])]= {}

        for node in self.nodes:
            lienConnection[node.innovationNumber] = [0,[]]
            #trouve ça possition (?dicotomie)
            trouver = False
            aumillieux = False
            pos = 0
            for pos in range(len(couches)):
                if couches[pos][0].positionX == node.positionX:
                    couches[pos].append(node)
                    trouver = True
                    break
                elif couches[pos][0].positionX > node.positionX:
                    aumillieux = True
                    break

            if trouver == False and aumillieux == True:
                couches.insert(pos,[node])
            elif trouver == False and aumillieux == False:
                couches.append([node])
                
        
        ##connection
        for con in self.connections:

            lienConnection[con.nodeSource.innovationNumber][1].append(con)

                
        ##
        for i in range(len(couches[0])):
            lienConnection[couches[0][i].innovationNumber][0] = inputs[i]

        for couhe in couches:
            for i in range(len(couhe)):
                vv = lienConnection[couhe[i].innovationNumber][0]
                for j in range(len(lienConnection[couhe[i].innovationNumber][1])):
                    lienConnection[lienConnection[couhe[i].innovationNumber][1][j].nodeDestiantion.innovationNumber][0] += lienConnection[couhe[i].innovationNumber][1][j].value * vv

        listoutput = {}
        for nn in couches[-1]:
            listoutput[nn.innovationNumber] = lienConnection[nn.innovationNumber][0]



        return listoutput


    
    def getrandomindexofconnection(self):
        if len(self.connections) == 0:
            raise ValueError("il n'y a pas de connection")
        
        return randint(0,len(self.connections)-1)


    def GETRandomValue():
        return (random() *2-1) *  __class__.MAXVALUEMUTATION