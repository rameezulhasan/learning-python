# Write a program to fill in a letter template given below with name and date
# letter = '''
# Dear <|NAME|>
# You are selected!
# <| DATEI|>
# '''

take_name = input("Enter Your Name: ")
date= input("Enter Today Date in this form  DD/MM/YY: ")

letter = f'''
 Dear {take_name}
 You are selected!
 {date}
'''

print(letter)



 # Method 2
letter2 = '''
Dear <|NAME|>
You are selected!
<|DATEI|>
'''
print(letter2.replace("<|NAME|>","Rameez").replace("<| DATEI|>","30-07-2025"))