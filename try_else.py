try:
    a = int(input("Enter Number: "))
    print (a)

except Exception as e:
    print(e)

else:               #Code can only work if try succesfully executed
    print ("Else part working")