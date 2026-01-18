#  Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary

class Employee:
    
    
    @property
    def salaryAfterIncrement (self):
        return self.salaryAfterIncrement
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement (self,value):
        self.salary = value
a = Employee()

a.salary = 1300000
a.increment = 20000