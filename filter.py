l =[1,2,3,4,5,6,7,8,9,10]

def even(n):
    if(n%2==0):
        return True
    return False

evenList = filter(even,l)
print(list(evenList))