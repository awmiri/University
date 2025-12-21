from abc import ABC , abstractmethod
import math
class Shape (ABC):
    def __init__(self ,):
        pass
    @abstractmethod
    def Shapes_area(self):
        pass
    @abstractmethod
    def Shapes_perimeter(self):
        pass

class Rectangle (Shape):
    def __init__(self , width , height , name):
        super().__init__()
        if width >= 0:
            self._width = width
        else:
            print("value width is not valid !!!!!")    
            self._width = 0
            
        if height >= 0:
            self._height = height
        else:
            print("value height is not valid !!!!!")    
            self._height = 0
        self.name = name
    def Shapes_area(self):
        return self._width * self._height
    def Shapes_perimeter(self):
        return (self._height + self._width) * 2
class Circle(Shape):
    def __init__(self , radius , name):
        super().__init__()
        if radius >=0 :
            self._radius = radius
        else:
            print("not valid number for the reduce")
            self._radius = 0
        self.name = name
    def Shapes_area(self):
        return pow(self._radius , 2 ) * math.pi
    def Shapes_perimeter(self):
        return self._radius * math.pi * 2

width = int(input("enter your width number : "))
height = int(input("enter your height number : "))
radius = int(input("enter your reduce number : "))
r1= Rectangle(width,height ,"rectangle")
c1 = Circle(radius ,"circle")
allShape = [r1 , c1]


for shape in allShape:
    print(f"the shape with this {shape.name} name, have the {shape.Shapes_area()} masahat also have {shape.Shapes_perimeter()} mohit")
    print("-"*25)