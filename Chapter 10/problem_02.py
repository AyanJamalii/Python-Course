# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Train no {self.trainNo} is Booked from {fro} to {to}")
    def trainStatus(self):
        print(f"Train no {self.trainNo} is on Time.")
    def trainFare(self, fro, to):
        print(f"The fare of Train no {self.trainNo} from {fro} to {to} is {randint(220, 2200)}")

t = Train(12412)
t.book("Karachi", "Lahore")
t.trainStatus()
t.trainFare("karachi", "Lahore")
