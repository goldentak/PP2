# 1  |   Define a class which has at least two methods
class class1:
        
    def getString(self):
        self.String = input("imput the string value:: ")
    
    def printString(self):
        print(self.String.upper())
#declaring the object
newClass = class1()

newClass.getString()
newClass.printString()
