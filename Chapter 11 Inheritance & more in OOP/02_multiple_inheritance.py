
class Employee:
    name="Rameez"
    age = 21
    def details(self):
        print(f"The name is of this empoyee is {self.name} and his age is {self.age}")
class Coder:
    language = "Python"
    def printLanguages (self):
        print(f"Out of the all language here is your language {self.language}")
class Programmer (Employee,Coder):
    def show_all_detail(self):
        print(f"This is programmer class {self.language}")
     
     
a = Employee()
b = Programmer()
b.details()
b.show_all_detail()
b.printLanguages()