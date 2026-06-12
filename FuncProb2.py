def SumofFirstNnums(n):
    sum = n
    if (n==1 or n==0):
        return sum
    else:
        sum = n + SumofFirstNnums(n-1)
        return sum
num = int(input("Enter the number "))
print(f"The sum of first {num} natural nums is {SumofFirstNnums(num)}")