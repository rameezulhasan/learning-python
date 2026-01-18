class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
        print(f"{self.name} {self.age} {self.grade}")
student_1 = Student("Rameez",100,"A+")
student_2 = Student("Ali",85,'A')

"""
       Types Of Constructor
       1-  Default Constructor  (self)
       2-  Parameterized Constructor (self, name, age)
       3-  Constructor with default values (self, name="unknown", age=0)
"""
