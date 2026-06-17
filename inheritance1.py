class Employee():
    Company = "Google"
    def show (self):
        print(f"The Company is {self.Company}\n")

class Programmer(Employee):
    ''' def show (self):
       print(f"The Company is {self.Company}")'''       
    #As Company was already defined in employee class and we inherit programmer class from it we don't need to mention it again
    def showLanguage(self):
        Language = "python"
        print(f"The Language is {self.Language}")

Devansh = Programmer()

print(Devansh.Company)