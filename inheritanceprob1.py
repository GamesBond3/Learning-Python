class TwoDVector():
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2D Vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The 3D Vector is {self.i}i + {self.j}j + {self.k}k")
A = TwoDVector(1,2)
B = ThreeDVector(4,5,6)

A.show()
B.show()