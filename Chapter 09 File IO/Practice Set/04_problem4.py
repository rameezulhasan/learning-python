#    A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 
word = "Donkey"

with open("Practice Set/file.txt") as f:
    content = f.read()
contnetNew = content.replace(word, "#####")
with open("Practice Set/file.txt", "w")as f:
    f.write(contnetNew)
