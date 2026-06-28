from functools import reduce
l = []
n = int(input("Enter Number: "))
l.append(n)
n = int(input("Enter Number: "))
l.append(n)
n = int(input("Enter Number: "))
l.append(n)
n = int(input("Enter Number: "))
l.append(n)
n = int(input("Enter Number: "))
l.append(n)

def greater(a,b):
    if (a>b):
        return a
    return b

scannedlist = reduce(greater,l)
print(scannedlist)