# 2  |   Define a class named Shape and its subclass Square
class Shape:
    def __init__(self):
        self.area = 0
    def __init__(self, area):
        self.area = area  #just, overloading
    
    def area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2
    
