f = open("test.txt","w")
f.write("Hello World")
f.close()


f = open("test.txt","r+")
data = f.read()
print("Old Content: ",data)

f.seek(0)
f.write("Hi World")
f.truncate()

f.close()

f = open("test.txt","r")
print(f"New Content: {f.read()}")
f.close()