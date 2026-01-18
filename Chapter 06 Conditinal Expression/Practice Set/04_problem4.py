#   Create  a program  to find whether a given username contain less than 10 characters or not.

username = input("Enter Username: ")

if (len(username) == 10):
    print(f"Length of username is equal to 10. Username is: {username}")
elif (len(username) < 10):
    print(f"Length of username is lower than 10. Username is: {username}")
elif (len(username) > 10):
    print(f"Length of username is greater than 10. Username is: {username}")
else:
    print("hjghf")