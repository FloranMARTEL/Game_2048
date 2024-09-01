from Neat import Node

class Connection():

    CONNECTION : dict = {}

    def __init__(self,nodeSource : Node, nodeDestiantion: Node,value : float,enabel : bool = True, innovationNumber: int|None = None) -> None:
        self.nodeSource : Node = nodeSource
        self.nodeDestiantion : Node = nodeDestiantion
        self.value : float = value

        self.enabel : bool = enabel

        if innovationNumber == None:
            if self.HashCode() in __class__.CONNECTION.keys():
                numinovation = __class__.CONNECTION[self.HashCode()].innovationNumber
            else:
                numinovation = len(__class__.CONNECTION)+1
                __class__.CONNECTION[self.HashCode()] = self
        else:
            numinovation = innovationNumber

            
        self.innovationNumber : int = numinovation


    def HashCode(self):
        return float(str(self.nodeSource.innovationNumber) + "0."+(str(self.nodeDestiantion.innovationNumber))[::-1])

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
    
    def __str__(self):
        return f"HashCode : [{self.HashCode()}]; value : {self.value}; enabel : {self.enabel}"
    
    
    def __repr__(self) -> str:
        return self.__str__()

