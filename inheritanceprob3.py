class Complex():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def show(self):
        print(f"The Complex No. is {self.real} + {self.imaginary}i")

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary+ other.imaginary)
    
    def __mul__(self, other):
        return Complex(self.real ** 2 - other.imaginary**2, 2*self.imaginary * other.imaginary)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    
c1 = Complex(3,4)
c2 = Complex(2,5)

print(c1+c2)
print(c1*c2)