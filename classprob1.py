class Programmer():
    Company = "Microsoft"
    def __init__(self, name, salary, city):
        self.name = name
        self.salary = salary
        self.city = city

d = Programmer("Devansh", "1 Million", "Jaipur")
print (d.name, d.Company, d.salary, d.city)