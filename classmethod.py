class Employee:
    a = 20
    @classmethod #writing this means, even if we change the value later the original value won't be affected
    def half(cls):
        print(f"Half of what was entered is {(cls.a)/2}")

s = Employee()
s.a = 10 #changed here, but output would still be 10 due to class method
s.half()