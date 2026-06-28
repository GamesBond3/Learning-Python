n = int(input("Enter num: "))
table = [str(n*i) for i in range(1,11)]

p = "\n".join(table)
print(p)