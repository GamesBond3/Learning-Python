with open ("fileprob4.txt") as f:
    content1 = f.read()

with open("fileprob7.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Files are identical")

else:
    print("files are not identical")