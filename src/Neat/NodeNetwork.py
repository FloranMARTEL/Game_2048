from Neat import *
from copy import deepcopy
from random import shuffle,random,randint

class NodeNetwork():

    MAXVALUEMUTATION = 100

    ProbabilityTONewConnection = 0.5
    ProbabilityTOEnbeledConnection = 0.3
    ProbabilityTOValueOfConnection = 0.5
    ProbabilityTOValueOfConnectionRandomly = 0.1
    ProbabilityTONewNode = 0.2

    def __init__(self, nodes : list[Node], connections : list[Connection],neat) -> None:
        self.nodes : list[Node] = nodes
        self.connections : list[Connection] = connections
        self.neat = neat

            

    @staticmethod
    def NewNodeNetwork(nbinput : int,nboutput : int,neat):
        nodes = []

        for numinputnode in range(nbinput):
            nodes.append(Node(numinputnode+1,0,numinputnode))
        
        for numoutputnode in range(nboutput):
            nodes.append(Node(nbinput+numoutputnode+1,1,numoutputnode))

        return NodeNetwork(nodes,[],neat)
        
    
    def copy(self):
        return NodeNetwork(deepcopy(self.nodes), deepcopy(self.connections))
    
    def mutation(self):

        if __class__.ProbabilityTONewConnection > random():
            self.mutationOfNewConnection()
        
        if __class__.ProbabilityTOEnbeledConnection > random():
            self.mutationOfEnbeledConnection()

        if __class__.ProbabilityTOValueOfConnection > random():
            if __class__.ProbabilityTOValueOfConnectionRandomly > random():
                self.mutationOfValueOfConnectionRandomly()
            else:
                self.mutationOfValueOfConnection()

        if __class__.ProbabilityTONewNode > random():
            self.MutationOfNewNode()
        

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
        self.connections.append(newConnectionA,newConnectionB)


    
    def getrandomindexofconnection(self):
        return randint(len(self.connections)-1)


    def GETRandomValue():
        return (random() *2-1) *  __class__.MAXVALUEMUTATION