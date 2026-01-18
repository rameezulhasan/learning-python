#  Repeat program 4 for a list of such words to be censored.


words = ["Donkey","Dog","Monkey","Bad","Animal","abcd"]

with open("Practice Set/file.txt") as f:
    readContent = f.read()
    lower_text = readContent.lower()
    print(lower_text)
for word in words:
   lower_words= word.lower()
   lower_text = lower_text.replace(lower_words,"#" * len(lower_words)) 
with open("Practice Set/file.txt","w") as f:
    print(f.write(lower_text))