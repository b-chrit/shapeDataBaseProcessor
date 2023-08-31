import math
pi=math.pi
class Shape:
    id=1
    def __init__(self):
        self.id=Shape.id
        Shape.id=Shape.id+1
    def area(self):
        return "undefined"
    def perimeter(self):
        return "undefined"
    def print(self):
        print(str(self.id)+":",self.__class__.__name__,",perimeter:",self.perimeter(),",area:",self.area())

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius    
    def perimeter(self):
        return 2*pi*self.radius
    def area(self):
        return pi*(self.radius**2)
    def print(self):
        super().print()
    
class Ellipse(Shape):
    def __init__(self,a,b):
        super().__init__()
        self.a=max(a,b)
        self.b=min(a,b)
    def perimeter(self):
        a="undefined"
        return a
    def area(self):
        return pi*self.a*self.b
    def eccintricity(self):
        c=math.sqrt((self.a**2)-(self.b**2))
        return c
    def print(self):
        print(str(self.id)+":",self.__class__.__name__,",perimeter:",self.perimeter(),",area:",self.area(),"linear eccentricity:",self.eccintricity())

class Rhombus(Shape):
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b
    def perimeter(self):
        c = 2 * math.sqrt((self.a**2) + (self.b**2))
        return c
    def area(self):
       c=(self.a*self.b)/2
       return c
    def side(self):
        c=math.sqrt(self.a**2+self.b**2)/2
        return c
    def inradius(self):
        c=(self.a*self.b)/(2*math.sqrt(self.a**2 + self.b**2))
        return c
    def print(self):
        print(str(self.id)+":",self.__class__.__name__,",perimeter:",self.perimeter(),",area:",self.area(),"in-radius:",self.inradius())
