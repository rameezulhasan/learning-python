#  Write a program to print the folluwing Stax fulilen+
# ***
# * *  for n = 3
# ***

take_number = int(input("Enter any number: "))

for i in range (1, take_number + 1):
    if(i==1 or i==take_number):
        print("*" * take_number, end="")
    else: 
        print("*", end="")
        print(" " * (take_number-2), end="")
        print("*", end="")
    print("")

    