f= open("fileprob1.txt")
word = input("Enter word for search: ")
content = f.read()

if(word in content ):
    print(f"{word} has been found!")
else:
    print(f"{word} is not in existing text")

