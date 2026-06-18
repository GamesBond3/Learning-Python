class Calculator():
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num):
        return self.n + num.n
    
    def __mul__(self, num):
        return self.n/num.n
    
    def __truediv__(self, other):
        return self.n*other.n
# n = int(input("Enter first number: "))
# m = int(input("Enter second number: "))
# print (n+m)

a= 4
b = 2
print(a/b)

x= 4
y=5
print(x*y)
