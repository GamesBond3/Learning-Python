from functools import reduce
l = [1,2,3,4,5]

def addi(m,n):
    return m + n

print(reduce(addi,l))