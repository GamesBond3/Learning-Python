class Employee():
    Salary = 100000
    increment = 5

    @property
    def salaryAfterIncrement(self):
        return (self.Salary + (self.Salary*self.increment)/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, Salary):
        self.increment = ((Salary/self.Salary) - 1)*100


a = Employee()

print(a.salaryAfterIncrement)

b = Employee()
b.salaryAfterIncrement = 105000
print(b.increment)
