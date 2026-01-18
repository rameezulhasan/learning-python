#  Write a class “Calculator” capable of finding square, cube and square root of a number.
import math
class Calculator:
    number = 49
    
    def finding_itms (self):
        
        print(f"Square of {self.number} is equal to {self.number**2}")
        print(f"Cube of {self.number} is equal to {self.number**3}")
        print(f"Square Root of {self.number} is equal to {self.number**0.5}")

objCalculator = Calculator()
objCalculator.finding_itms()