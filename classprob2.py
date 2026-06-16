class Calculator():
    def __init__(self, n):
        self.n = n

    def square(self):
        print (f"Square of the number is {self.n*self.n}")
    def cube(self):
        print (f"Cube of the number is {self.n*self.n*self.n}")
    def squareroot(self):
        print (f"Squareroot of the number is {self.n**1/2}")
    

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
