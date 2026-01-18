#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ fromv ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animal:
    print("This is Animals")

class Pets(Animal):
    print("This is Pets")

class Dog(Pets):
    def bark(self):
        print("The Dogs are barking")


a = Dog()
a.bark()