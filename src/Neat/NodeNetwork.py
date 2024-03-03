from Neat import *

class NodeNetwork():

    def __init__(self, nodes : list[Node], connections : list[Connection]) -> None:
        self.nodes : list[Node] = nodes
        self.connections : list[Connection] = connections

    
    