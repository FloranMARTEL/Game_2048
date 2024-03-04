from Neat import Node

class Connection():

    CONNECTION : list = {}

    def __init__(self,nodeSource : Node, nodeDestiantion: Node,value : float,enabel : bool = True) -> None:
        self.nodeSource : Node = nodeSource
        self.nodeDestiantion : Node = nodeDestiantion
        self.value : float = value

        self.enabel : bool = enabel

        numinovation = __class__.CONNECTION[self.HashCode()]
        if numinovation == None:
            numinovation = len(__class__.CONNECTION)+1
            __class__.CONNECTION[self.HashCode()] = self
            
        self.innovationNumber : int = numinovation


    def HashCode(self):
        return self.nodeSource.innovationNumber + float("0."+(reversed(str(self.nodeDestiantion.innovationNumber))))

    def changeValue(self,value: float):
        self.value = value

    def __eq__(self, __value: object) -> bool:
        if not (type(__value) is __class__):
            return False

        if __value.nodeSource != self.nodeSource:
            return False

        if __value.nodeDestiantion != self.nodeDestiantion:
            return False

        return True
    
    copyright
