class Node():

    NODE : int = 1

    def __init__(self,positionX : float ,positionY: float, innovationNumber: int|None = None ) -> None:
        
        if innovationNumber == None:
        
            self.innovationNumber : int = __class__.NODE
            __class__.NODE += 1
        else :
            self.innovationNumber = innovationNumber

        self.positionX : float = positionX
        self.positionY : float = positionY


    def __eq__(self, __value: object) -> bool:
        if not (type(__value) is __class__):
            return False
        
        if __value.innovationNumber != self.innovationNumber:
            return False
        
        return True
    
    def __str__(self):
        return f"innovationNumber : [{self.innovationNumber}]; x : {self.positionX}; y : {self.positionY}"
    
    
    def __repr__(self) -> str:
        return self.__str__()