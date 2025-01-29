#3  |   Define a class named Rectangle which inherits from Shape
from t2 import Shape 
class Rectangle(Shape):
    def __init(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def computeArea(self):
        return self.length * self.width
    
