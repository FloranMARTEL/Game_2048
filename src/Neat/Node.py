class Node():

    NODE : int = 0

    def __init__(self,positionX : float ,positionY: float ) -> None:
        
        __class__.NODE += 1
        self.innovationNumber : int = __class__.NODE
        self.positionX : float = positionX
        self.positionY : float = positionY


    def __eq__(self, __value: object) -> bool:
        if not (type(__value) is __class__):
            return False
        
        if __value.innovationNumber != self.innovationNumber:
            raise False
        
        return True