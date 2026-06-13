f = open("file2text.txt")
# line1 = f.readline()
# print(line1)
# line1 = f.readline()
# print(line1)
# line1 = f.readline()
# print(line1)
line = f.readline()

while (line != ""):
    print(line)
    line = f.readline()
f.close 