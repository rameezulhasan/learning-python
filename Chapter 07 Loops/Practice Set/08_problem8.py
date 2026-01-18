#  Wirite a program to print the follwing star pattern.
# *
# **
# *** for n=3

take_number = int(input("Enter any number: "))

for i in range(1, take_number+ 1):
    print("*" * (i), end="")
    print('')