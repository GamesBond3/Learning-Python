name = input("Enter your name: ")

print(f"Hello Good Evening, {name}")

date = input("Enter the date: ")

Letter = f''' Dear {name}
You are selected for the job. 
{date} '''
print(Letter)
# Strings are immutable in Python, which means that once a string is created, it cannot be changed. However, you can create a new string by concatenating or modifying the existing string.