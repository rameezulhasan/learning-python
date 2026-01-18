#  Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Two_DVector: 
    def __init__(self, i,j):
          self.i = i
          self.j = j
    
    def ShowDetails(self):
            print(f"The 2D Vector is {self.i}i + {self.j}j")
    

class Three_DVector(Two_DVector):
        def __init__(self, i, j, k):
              super().__init__(i, j)
              self.k = k
        
        def Show(self):
            print(f"The 3D Vector is {self.i}i + {self.j}j + {self.k}k")
        
        
a = Three_DVector(5,2,8)
a.ShowDetails()
a.Show()