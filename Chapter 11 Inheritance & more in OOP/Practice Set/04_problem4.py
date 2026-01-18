# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, num):
        return Complex(self.r + num.r, self.i + num.i)
    
    def __mul__(self, num):
        real_part = self.r * num.r - self.i * num.i
        imaginary_part = self.r * num.r + self.i * num.i
        return Complex(real_part, imaginary_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    def __str__(self):
        return f"{self.r} * {self.i}i"
        

obj1 = Complex(1,2)
obj2 = Complex(3,4)
print(obj1 + obj2)
print(obj1 * obj2)