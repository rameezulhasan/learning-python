#  write a program to find out whether a given post is talkng about "Rameez" or not

post = input("Enter post: ")

if("rameez" in post.lower()):
    print("This post is talking about Rameez")
else:
    print("This post is not talking about Rameez")
