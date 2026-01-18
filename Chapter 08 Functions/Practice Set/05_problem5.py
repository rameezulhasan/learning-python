#  Write a python function which converts inches to cms.

take_number = int(input("Enter any number: "))

def inch_to_cm (number):
    return (f"{number} in is equal to {number*2.54} cm")
print(inch_to_cm(take_number))