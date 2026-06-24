n = int(input("Enter Number: "))

table = [ n*i for i in range(1,11)]
print(table)

with open ("fileprob9.txt", "a")as f:
    f.write (str(table) + "\n")