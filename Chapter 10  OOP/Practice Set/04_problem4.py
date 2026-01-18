#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint
class Train:
    
    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def book_ticket(self, fro, to):
        print(f"Ticket is booked and your train No is {self.trainNo} and train path is {fro} to {to}")
    
    def get_status(self):
        print(f"Train no {self.trainNo} is run on timely")
    
    def fare_information(self, fro, to):
        print(f"Ticket fare in train No is {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
        
t = Train(1534)
t.book_ticket("Lahore","Faisalabad")
t.get_status()
t.fare_information("Lahore","Faisalabad")