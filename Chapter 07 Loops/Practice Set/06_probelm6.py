#  Write a program to calculate the factorial of a given rumber using for loop

take_number = int(input('Enter any number: '))


mult = 1

for i in range(1,take_number + 1):
    mult = mult * i
print(f"Factorial of this numbers is {mult}")