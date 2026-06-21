try:
    a = int(input("Enter Number: "))
    print (a)

except Exception as e:
    print(e)

except ValueError as v:
    print(v)

except ZeroDivisionError as z:
    print(z)