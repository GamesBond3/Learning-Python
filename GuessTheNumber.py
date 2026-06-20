import random
Num = random.randint(1,101)
i = 1
guess = -1
while (guess != Num):
    guess = int(input("Enter your guess: "))
    if (guess>Num):
        print("Lower")
        i+=1
    elif (guess<Num):
        print("Higher")
        i+=1

print(f"You guessed the {Num} in {i} tries")