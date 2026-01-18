#  Attempt problem 1 using while loop

take_number = int(input("Enter any number: "))
end_number = int(input("Enter Ending number: "))

i = 1

while (i<=end_number):
    print(f"{take_number} x {i} = {take_number * i}")
    i+=1