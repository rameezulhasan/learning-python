#  Write a program to mine a log file and find out whether it contains ‘python’
word = "python"
with open("Practice Set/log.html") as f:
    data = f.read()
    lower_data = data.lower()
    print(lower_data)
if(word in lower_data):
    print("Yes this file contain Python")
else:
    print("This file doesn't contain Python")

