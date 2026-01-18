class details:
    name = "Rameez"
    age = 21
    degree = "BSCS"
    
    def __init__(self,name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
        print("I am Constructor") #dunder method which is automatically called
        
    
    def getInfo(self):
        print(f"The name of student is {self.name} and age is {self.age} and degree is {self.degree}")
        
    @staticmethod  #static is se phir self object add karne ki zaroorat nahi hoti
    def greet():
        print("Good Morning")

studentDetails = details("Ahmed",30,"BSSE")   #Object
studentDetails.greet()
studentDetails.getInfo()