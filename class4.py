class Class :
    language = "C Programming Language"
    company = "Microsoft"
    def __init__ (self): #This is Dunder Method and init runs when a new object is added
        print ("A new object has been added.")

@staticmethod
def Greet():
    print("Thanks!")

Devansh = Class()
Devansh.name = "Devansh"
print(f"Student name is {Devansh.name}\nFluent in {Devansh.language}\nPlaced in {Devansh.company}")

Greet()