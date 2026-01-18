#  A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". write a program to detect these spams.

keyword_one = "Make a lot of money"
keyword_two = "buy now"
keyword_three = "subscribe this"
keyword_four = "click this"

comment = input(" Enter a Comment: ")

if((keyword_one in comment) or (keyword_two in comment) or (keyword_three in comment) or (keyword_four in comment)):
    print("Print This is spamm comment")
    
else:
    print("This is correct comment")