a = 89
def fun():
    global a            #makes the variable permanent globally
    a = 3
    print(a)

fun()
print(a)

#Output: 3
#        3