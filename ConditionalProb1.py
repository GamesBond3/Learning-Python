a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d= int(input("Enter a number: "))
if (a>b and a>c and a>d):
    print("a is greatest")
elif (b>a and b>c and b>d):
    print("b is greatest")
elif (c>a and c>b and c>d): 
    print("c is greatest")
elif (d>a and d>b and d>c):
    print("d is greatest")
else:
    print("All numbers are equal")