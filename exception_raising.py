a = int(input("Enter first no.: "))
b = int(input("Enter second no.: "))

if (b==0):
    raise ZeroDivisionError ("Heyyyy our programme doesn't Support that!")
else:
    print(f"The Value of a÷b is {a/b}")
