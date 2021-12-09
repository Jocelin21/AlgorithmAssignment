class Circle:
    def __init__(self, radius:float = 1.0, color:str = "red") -> None:
        self.__radius = radius
        self.__color = color
        self.__getarea = self.getArea()
    
    def Circle(self):
        pass

    def Circle(radius:float):
        pass

    def Circle(radius:float, color:str):
        pass

    def getRadius(self) -> float:
        return self.__radius

    def setRadius(self, radius:float) -> None:
        self.__radius = radius

    def getColor(self) -> str:
        return self.__color
    
    def setColor(self, color:str) -> None:
        self.__color = color

    def toString(self) -> str:
        pass

    def getArea(self) -> float:
        #Area = pi x r**2
        self.__getarea =  (22/7) * self.__radius**2
        return self.__getarea
    

class Cylinder(Circle):
    def __init__(self, radius, color, height):
        super().__init__(radius, color)
        self.__height = height
        self.__getVolume = self.getVolume()

    def Cylinder(self):
        pass

    def Cylinder(height:float):
        pass

    def Cylinder(height:float, radius:float):
        pass

    def Cylinder(height:float, radius:float, Color:str):
        pass

    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height:float) -> None:
        self.__height = height

    def toString(self) -> str:
        pass

    def getVolume(self) -> float:
        #Cylinder volume = area(pi x r**2) x height
        self.__volume = Circle.getArea(self) * self.__height
        return self.__volume

