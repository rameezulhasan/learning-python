#  recursion

take_number = int(input("Enter any number: "))

def factroial(number):
    if(number==1 or number==0):
        return 1
    return number * factroial(number-1)
print(f"The factorial of this {take_number} is {factroial(take_number)}")