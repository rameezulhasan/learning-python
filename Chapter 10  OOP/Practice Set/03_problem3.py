#  Add a static method in problem 2, to greet the user with hello.


import math
class Calculator:
    number = 49
    
    def finding_itms (self):
        
        print(f"Square of {self.number} is equal to {self.number**2}")
        print(f"Cube of {self.number} is equal to {self.number**3}")
        print(f"Square Root of {self.number} is equal to {self.number**0.5}")
    @staticmethod
    def greet():
        print("Welcome")

objCalculator = Calculator()
objCalculator.greet()
objCalculator.finding_itms()