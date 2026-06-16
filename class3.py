class Employee:
    language = "English"
    Salary = "$120K"
    #These are class attributes
    @staticmethod #Using static method removes the need of "self attribute"
    def greeting():
        print("Hello Sir,")
    def getInfo(self):
        print(f"The language is {self.language} and Salary is {self.Salary}")
Devansh = Employee()
Devansh.name = "Devansh" #this is instance/object attribute
Devansh.language = "Python"
print(Devansh.name, "\n", Devansh.language, Devansh.Salary)
Devansh.greeting()
Devansh.getInfo() # this converts into Employee.getInfo(Devansh) this means there is an argument so we use Self
# Employee.getInfo(Devansh) this can also be used
