#  Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names Are unique.

dict = {}
friend_name = input("Enter Friends Name: ")
take_lang = input("Enter Your Favorite Language: ")
dict.update({friend_name:take_lang})
friend_name = input("Enter Friends Name: ")
take_lang = input("Enter Your Favorite Language: ")
dict.update({friend_name:take_lang})
friend_name = input("Enter Friends Name: ")
take_lang = input("Enter Your Favorite Language: ")
dict.update({friend_name:take_lang})
friend_name = input("Enter Friends Name: ")
take_lang = input("Enter Your Favorite Language: ")
dict.update({friend_name:take_lang})

print(dict)