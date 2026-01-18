#  Write a recursive function to calculate the sum of first n natural numbers.

take_number = int(input("Enter any number: "))

def sum_Natural_Numbers (number):
    if(number == 1):
        return 1
    return number + sum_Natural_Numbers(number-1)
print(sum_Natural_Numbers(take_number))