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
 
def divby5(n):
    if(n%5==0):
        return True
    return False

scannedList = filter(divby5,l)
print(list(scannedList))