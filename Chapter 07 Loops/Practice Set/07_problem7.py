#  Write a progrom to print the following star patterrn
# *
# ***
# ***** for n=3
# star = ""
take_number = int(input("Enter any number: "))

for i in range(1, take_number+1):
    print(" " * (take_number-i), end="")
    print("*" * (2*i-1), end='')
    print("")

    