#  White a program to find whether a given number is prime or not

take_number = int(input("Enter any number: "))

for i in range(2, take_number):
    if (take_number%i == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")
    