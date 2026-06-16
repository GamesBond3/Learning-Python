class Class :
    language = "C Programming Language"
    company = "Microsoft"
    def __init__ (self, name, language, company): #This is Dunder Method and init runs when a new object is added
        self.name = name
        self.language = language
        self.company = company
        print ("A new object has been added.")
        #If we do the above we have to pass the values of name, lang and company everytime we create an object
@staticmethod
def Greet():
    print("Thanks!")

Devansh = Class()               #Here Devansh is an object.
Devansh.name = "Devansh"
print(f"Student name is {Devansh.name}\nFluent in {Devansh.language}\nPlaced in {Devansh.company}")

Rohan = Class("Rohan", "Javascript", "Amazon")
print(f"Student name is {Rohan.name}\nFluent in {Rohan.language}\nPlaced in {Rohan.company}")
Greet()