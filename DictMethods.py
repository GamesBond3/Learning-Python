Marks = {
    "Devansh": 100,
    "Anshuman": 90,
    "Annant": 80   
}
# print(Marks, type(Marks))
# print(Marks.items())
# print(Marks.keys())
Marks.update({"Devansh": 99})
print(Marks)
print(Marks.get("Devansh2")) #prints none if key is not found
# print(Marks["Devansh2"]) #throws error if key is not found