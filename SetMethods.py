s = {"Devansh", 1, 21, 19, 5, 5, 5} #This is a set
e = set() #This is an empty set
d = {} #This is an empty dictionary
print(s)
s.add("Anshuman")
print(s)
s.remove(5)
print(s, len(s))
e.add(1)
e.add("Devansh") 
e.add(218)
print(e.union(s))
print(e.intersection(s))