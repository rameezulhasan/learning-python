with open("withfile.txt","w") as f:
    print(f.write("This is with Keyword"))
    
with open("withfile.txt") as f:
    print(f.read())