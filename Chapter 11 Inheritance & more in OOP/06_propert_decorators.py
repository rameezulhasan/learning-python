class test:
     a = 2
     @classmethod
     def data (self):
          print(f"value of a is {self.a}")
     @property    
     def name (self):
        return f"{self.fname} {self.mname} {self.lname}"
    
     @name.setter
     def name (self,value):
          self.fname = value.split(" ")[0]  
          self.mname = value.split(" ")[1]
          self.lname = value.split(" ")[2]
            
b = test()
b.a = 10

b.name = "Rameez Ul Hassan"
print(b.name)

b.data()