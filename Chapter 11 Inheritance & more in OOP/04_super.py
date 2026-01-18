class Employee:
    def __init__(self):
        print("This is Employee Constructor")
    a = 1
    
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("This is Programmer Constructor")
    b = 2
    
class Manager(Programmer):
    def __init__(self):
        super().__init__()  # ye use hota hai apne parent ka constructor chalanay ke liye. jaise Manager ka parent is time Programmer hai.
        print("This is Manager Constructor")
    c = 3



o = Manager()
print(o.a)
print(o.a,o.b)
print(o.a,o.b, o.c)