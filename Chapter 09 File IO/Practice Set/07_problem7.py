#  Write a program to find out the line number where python is present from ques 6.

word = "python"
with open("Practice Set/log.html") as f:
    data = f.readlines()
    lineno = 1
for lines in data:
    lines = lines.lower()
    
    if(word in lines):
      print("Yes this file contain Python",[lineno])
      break
    lineno+=1
else:
    print(" No python is not present")

