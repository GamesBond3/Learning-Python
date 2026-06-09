list = []
inputname = input("Enter name: ")
list.append(inputname)
inputname = input("Enter name: ")
list.append(inputname)
inputname = input("Enter name: ")
list.append(inputname)

name = input("Enter name to find: ")
if (name in list):
    print("Name is present in the list \n" ,(list))
else:
    print("Name is not present in the list \n" ,(list))