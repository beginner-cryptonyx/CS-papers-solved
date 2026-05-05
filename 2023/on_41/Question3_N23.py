# a i
class Character:
    # private Name as String
    # private XPosition as Integer
    # private YPosition as Integer
    def __init__(self, PName, PXPosition, PYPosition) -> None:
        self.__Name:str = PName # private String
        self.__XPosition:int = PXPosition # private Integer
        self.__YPosition:int = PYPosition # private Integer
    
    # a ii
    def GetYPosition(self):
        return self.__YPosition
    def GetXPosition(self):
        return self.__XPosition
    
    # a iii
    
    def SetXPosition(self,)