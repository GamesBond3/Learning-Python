import random

def game():
    print("Game has begun")
    score = random.randint(1,100)
    #fecthing score
    with open ("fileprob2hiscore.txt")as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Your score = {score}")
    if(score>hiscore):
        #writing in hiscore file
        with open("fileprob2hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()