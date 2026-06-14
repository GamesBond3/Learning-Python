word = "Donkey"

with open ("fileprob3.txt") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open ("fileprob3.txt", "w")as f:
    f.write(contentNew)

