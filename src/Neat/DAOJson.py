import json


from Node import Node
from Connection import Connection
from Individual import Individual



class DAOJson():

    DATAFile = "src\\Neat\\data"
    PREFIX = "Generation_"

    @staticmethod
    def Read(GenerationNumber : int):
        file = open(__class__.DATAFile+"\\"+__class__.PREFIX+str(GenerationNumber)+".json","r")
        json_str = file.read()
        json_dict = json.loads(json_str)
        return json_dict

    def ReadIndividu(GenerationNumber : int,individualNumber : int):
        json_dict = __class__.Read(GenerationNumber)
        return json_dict[individualNumber]

# @staticmethod
# def Update(GenerationNumber : int):
#     pass

# @staticmethod
# def UpdateIndividu(GenerationNumber : int,individualNumber : int):
#     pass

    @staticmethod
    def Delete(GenerationNumber : int):
        pass

    @staticmethod
    def Creat(GenerationNumber : int,Population : list[Individual]):
        
        json_dict = [__class__.__IndividualTODict(individual) for individual in Population]

        
    
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
                "nodeSource" : connection.nodeSource,
                "nodeDestiantion" : connection.nodeDestiantion,
                "value" : connection.value,
                "enabel" : connection.enabel,
                }




if __name__ == "__main__":
    print(DAOJson.Getdata(1))