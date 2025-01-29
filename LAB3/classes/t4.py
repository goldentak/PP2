#4  |   Write the definition of a Point class
import math
class Point:
    def __init__(self, pointA = 0, pointB = 0):
        self.pointA = pointA
        self.pointB = pointB

    def show(self):
        print(f"({self.pointA}, {self.pointB})")
    
    def move(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def dist(self):
        print(abs(self.pointA - self.pointB))


point = Point()
point.show()
point.move(1, 4)
point.show()
point.dist()
point.move(4, 1)
point.dist()
