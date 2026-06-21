def main():
    try:
        a = int(input("Enter Number: "))
        print (a)
        return

    except Exception as e:
        print(e)
        return
    
    finally:            #Finally works even if the func fails to execute
        print("Working")
    
    
main()