#  Write a python program using function to convert Celsius to Fahrenheit

take_number = int(input("Enter any number to convert celsius to fahrenheit:  "))

def convertCtoF(number):
    return(f"{number} Celsius to {number *(9/5) + 32} Fahrenheit")
print(convertCtoF(take_number))