age = int(input("Enter your age:"))

if(age>18):
    print("You are above the age of consent")
elif(age>17 and age<19):
    print("You are about to reach the age of consent")
elif(age==18):
    print("You just reached the age of consent")
else:
    print("You are below the age of consent") 