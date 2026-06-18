class Student:
    rollno = 21
    @classmethod
    def rollno(cls):
        print(f"The roll no is {cls.rollno}")
    
    @property
    def name (self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Student()

e.name = input("Enter your name: ")
print(f"First name is {e.fname}")
print(f"Last name is {e.lname}")