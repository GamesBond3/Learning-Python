with open ("fileprob5.html") as f:
   content = f.readlines()

line_no = 1
for line in content:
    if ("modi" in line):
        print(f"Word found in {line_no}")
        break
    line_no+=1

else:
   print("Word not found")