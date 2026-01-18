class details:
    name = "Rameez"
    age = 21
    degree = "BSCS"
    
    def getInfo(self):
        print(f"The name of student is {self.name} and age is {self.age} and degree is {self.degree}")
        
    @staticmethod  #static is se phir self object add karne ki zaroorat nahi hoti
    def greet():
        print("Good Morning")

studentDetails = details()   #Object
studentDetails.greet()
studentDetails.getInfo()