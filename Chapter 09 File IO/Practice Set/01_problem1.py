#  Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

# with open("poems.txt", "w") as f:
#     write_text = f.write("""
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
#             """)
    
with open("Practice Set/poems.txt") as f:
    read_text = f.read()
    if("twinkle" in read_text or "Twinkle" in read_text):
        print("Yes this poem have twinkle word")
    else:
        print("This poem doesn't have twinkle word")
    
    