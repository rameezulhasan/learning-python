#  Write a program to find the Sum of first n natural numbers using while loop!

take_number = int(input('Enter any number: '))

i = 1
sum = 0

while (i<=take_number):
    sum = sum + i
    i+=1
print(f"Sum of all numbers is {sum}")