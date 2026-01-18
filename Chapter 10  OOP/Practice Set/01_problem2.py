#  Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer: 
    salary = 1100000
    time = "Full Time"

    def PrintDetails(self):
        self.name = "Rameez"
        print(self.name,self.salary,self.time)
        self.name = "Ali"
        print(self.name,self.salary,self.time)
dataObj = Programmer()
dataObj.PrintDetails()