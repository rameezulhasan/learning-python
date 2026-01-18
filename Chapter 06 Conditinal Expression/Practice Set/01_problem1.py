#  write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

if (num1>num2 and num1>num3 and num1>num4):
    print("Num1 is greater")
elif(num2>num1 and num2>num3 and num2>num4):
    print("Num2 is greater")
elif(num3>num1 and num3>num2 and num3>num4):
    print("Num3 is greater")
elif(num4>num1 and num4>num2 and num4>num3):
    print("Num4 is greater")
elif(num1==num2 and num2==num3 and num3==num4):
    print("These are all same numbers")
else:
    print("Please Enter Correct Numbers")