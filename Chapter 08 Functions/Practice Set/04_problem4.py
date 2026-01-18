#  Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *


take_number = int(input("Enter any number: "))

def print_stars(number):
    if (number ==0):
        return ""
    print(number * "*")
    print_stars(number-1)
    
print_stars(take_number)