line = "Hy Rameez How are you?"

f = open("writefile.txt", "w")
f.write(line)
f.close()

# Html file make

htmlTag = "<h2>Heading 2</h2>"
f = open("index.html", "w")
f.write(htmlTag)
f.close()