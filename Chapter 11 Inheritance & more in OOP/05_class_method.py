class test:
     a = 2
     @classmethod
     def data (self):
          print(f"value of a is {self.a}")
b = test()
b.a = 10

b.data()