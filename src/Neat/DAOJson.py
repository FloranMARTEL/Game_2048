import json
import os

from Neat import Node,Connection,Individual,NodeNetwork



class DAOJson():

    DATAFile = "src\\Neat\\data"
    PREFIX = "Generation_"

    @staticmethod
    def Read(generationNumber : int) -> dict:
        file = open(__class__.DATAFile+"\\"+__class__.PREFIX+str(generationNumber)+".json","r")
        json_str = file.read()
        json_dict = json.loads(json_str)
        return json_dict

    @staticmethod
    def ReadIndividu(generationNumber : int,individualNumber : int):
        json_dict = __class__.Read(generationNumber)
        for element in json_dict:
            if element["individualMember"] == individualNumber:
                return element
        
        raise ValueError("l'individu n'existe pas")
    
    @staticmethod
    def DictToIndividu(data : dict):

        #node network
        listNodes = [ __class__.__DictToNode(datanode) for datanode in data["nodeNetwork"]["nodes"]]
        lisConnections = [ __class__.__DictToConnection(dataConnection,listNodes) for dataConnection in data["nodeNetwork"]["connections"]]

        nodeNetwork = NodeNetwork(listNodes,lisConnections)


        individu = Individual(nodeNetwork,data["individualMember"],data["score"])

        return individu
        




    def __DictToNode(data: dict) -> Node:

        node = Node(data["positionX"],data["positionY"],data["innovationNumber"])

        return node
    
    def __DictToConnection(data: dict,nodes : list[Node]) -> Node:

        nodesource = None
        nodedestination = None

        for node in nodes:
            if node.innovationNumber == data["nodeSource"]:
                nodesource = node
            if node.innovationNumber == data["nodeDestiantion"]:
                nodedestination = node
            
            if nodesource != None and nodedestination != None:
                break
        
        if nodesource == None or nodedestination == None:
            raise ValueError()
        
        connection = Connection(nodesource,nodedestination,data["value"],data["enabel"],data["innovationNumber"])

        return connection



        
        

    @staticmethod
    def Delete(generationNumber : int):
        os.remove(__class__.DATAFile+"\\"+__class__.PREFIX+str(generationNumber)+".json")
        

    @staticmethod
    def Creat(generationNumber : int,Population : list[Individual]):
        #print("1")
        json_dict = [__class__.__IndividualTODict(individual) for individual in Population]
        #print("2")

        json_str = json.dumps(json_dict)#,indent=2
        #print("3")

        open(__class__.DATAFile+"\\"+__class__.PREFIX+str(generationNumber)+".json","w").write(json_str)

        #print("4")
        
    
    def __IndividualTODict(individual : Individual) -> dict:

        individualDict = {}
        individualDict["individualMember"] = individual.numindividu
        individualDict["score"] = individual.score

        nodes = [__class__.__NodeTODict(node) for node in individual.nodeNetwork.nodes]
        connections = [__class__.__ConnectionTODict(connection) for connection in individual.nodeNetwork.connections]

        nodeNetwork = {"nodes" : nodes ,"connections" : connections}

        individualDict["nodeNetwork"] = nodeNetwork

        return individualDict

    
    def __NodeTODict(node : Node) -> dict:

        return {
                "innovationNumber" : node.innovationNumber,
                "positionX" : node.positionX,
                "positionY" : node.positionY
                }
    
    def __ConnectionTODict(connection : Connection) -> dict:

        return {
                "innovationNumber" : connection.innovationNumber,
                "nodeSource" : connection.nodeSource.innovationNumber,
                "nodeDestiantion" : connection.nodeDestiantion.innovationNumber,
                "value" : connection.value,
                "enabel" : connection.enabel,
                }
    
    @staticmethod
    def GenerationExist(generationNumber):
        return os.path.isfile(__class__.DATAFile+"\\"+__class__.PREFIX+str(generationNumber)+".json")




