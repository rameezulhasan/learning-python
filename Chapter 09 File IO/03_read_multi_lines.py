#      Using readlines()

# lines = open("file.txt")
# data = lines.readlines()
# print(data, type(data))
# lines.close()

#  Using readline()

f = open("file.txt")
# line1= f.readline()
# print(line1)
# line2= f.readline()
# print(line2)
# line3= f.readline()
# print(line3)
# line4= f.readline()
# print(line4)

line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()
f.close()
