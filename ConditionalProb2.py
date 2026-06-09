p1 = "Buy 1 Get 1 Free"
p2 = "Buy 1 Get 50% Off"
p3 = "Subscribe"
p4 = "free"

input = input("Enter you message:")

if((p1 in input)or (p2 in input)or (p3 in input)or (p4 in input)):
    print("This is a promotional message")
else:
    print("This is not a promotional message")