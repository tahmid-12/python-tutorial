import math

class Calculator:
    
    def __init__(self,number):
        self.number = number

    def square(self):
        return self.number * self.number
    
    def cube(self):
        return self.number * self.number * self.number

    def squareRoot(self):
        return math.sqrt(self.number)

three = Calculator(3)
print(three.number)    
print(three.square())
print(three.cube())
print(three.squareRoot())