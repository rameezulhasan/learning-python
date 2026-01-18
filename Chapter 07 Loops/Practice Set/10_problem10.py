#  Write a program to print multiplication table of n using  for loop in reversed order

take_number = int(input("Enter any number: "))

for i in range (1, 11):
    print(f"{take_number} x {11-i} = {take_number * (11-i)}")