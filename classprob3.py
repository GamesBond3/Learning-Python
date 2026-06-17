from random import randint

class train ():
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def bookingstatus (self, to, fro):             #from can't be used as a variable in python as it is reserved
        print(f"Train no. {self.trainNo} is booked for you, to {to} from {fro}")

    def getStatus(self):
        print (f"Train No. {self.trainNo} is running on time")

    def getFare(self):
        print (f"The fare is {randint(1111,2222)}")

t = train(12099)
t.bookingstatus("Pilani", "Jaipur")
t.getStatus()
t.getFare()