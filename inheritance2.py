class Employee():
    Company = "Google"
    def show (self):
        print(f"The Company is {self.Company}")


class Name():
    Name = input("Enter your name ")
    def showName (self):
        print (f"The Name you've entered is {self.Name}")



class Programmer(Name, Employee): 
    Language = "python"
    def showLanguage(self):
        print(f"The Language is {self.Language}")

Devansh = Programmer()

Devansh.showName()
Devansh.show()
Devansh.showLanguage()
