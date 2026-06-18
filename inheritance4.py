class Name():
    Name = input("Enter your name ")
    def showName (self):
        print (f"The Name you've entered is {self.Name}")


class Employee(Name):
    Company = "Google"
    def __init__(self):
        print("Employee init initiated")
    def show (self):
        print(f"The Company is {self.Company}")



class Programmer(Employee): 
    Language = "python"
    def __init__(self):
        # super().__init__()
        print("Programmer init initiated")
    def showLanguage(self):
        print(f"The Language is {self.Language}")

Devansh = Programmer()

Devansh.showName()
Devansh.show()
Devansh.showLanguage()
