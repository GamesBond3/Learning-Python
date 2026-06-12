def remove(l, word):
    n =[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

l = []
list = input("Enter your string: ")
l.append(list)
list = input("Enter your string: ")
l.append(list)
list = input("Enter your string: ")
l.append(list)
word = input("Enter your word to strip: ")

print(remove(l, word))