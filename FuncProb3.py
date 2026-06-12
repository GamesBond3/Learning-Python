def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
        

rows = int(input("Enter No. of rows: "))
pattern(rows)
