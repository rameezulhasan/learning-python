
class Employee:
    name="Rameez"
    age = 21
    def details(self):
        print(f"The name is of this empoyee is {self.name} and his age is {self.age}")
        
class Programmer (Employee):
    def showDetails(self):
        print("This is Programmer Class")
     
     
a = Employee()
b = Programmer()
b.details()
b.showDetails()