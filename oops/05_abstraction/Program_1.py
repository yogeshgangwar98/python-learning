from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width  = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*(self.radius**2)
    
    def perimeter(self):
        return 2*3.14*self.radius
    
rectangle = Rectangle(3,4)
circle = Circle(4)

print(rectangle.area())
print(rectangle.perimeter())
print(circle.area())
print(circle.perimeter())
    