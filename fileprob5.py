with open ("fileprob5.html") as f:
   content = f.read()

if ("Python" in content):
   print("Word found")

else:
   print("Word not found")