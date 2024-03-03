from Neat import Node

class Connection():

    def __init__(self,node1 : Node, node2: Node,value : float) -> None:
        self.node1 : Node = node1
        self.node2 : Node = node2
        self.value : float = value

    def changeValue(self,value: float):
        self.value = value