words = ["Donkey", "is", "Devansh", "Hardworking"]

with open ("fileprob4.txt") as f:
    content = f.read()

for word in words:
        content = content.replace(word, "#"* len(word))

with open ("fileprob4.txt", "w") as f:
    f.write(content)