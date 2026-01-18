#  Write a program using functions to find greatest of three numbers.

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

def findGreatestNumber(num1, num2, num3):
    if(num1>num2 and num1>num3):
        print("Number 1 is Greatest Number ",num1)
    elif(num2>num1 and num2>num3):
        print("Number 2 is Greatest Number ",num2)
    elif(num3>num1 and num3>num2):
        print("Number 3 is greatest number ",num3)
findGreatestNumber(number1,number2,number3)