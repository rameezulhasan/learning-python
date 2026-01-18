#  write a program to caluclate the grade of a student from his marks from the following scheme: 
# 90 - 100 => Ex
# 80 - 90 => A
# 70 - 80 => B
# 60 - 70 => C
# 50 - 60 => D
# <50 => F

take_marks = int(input("Enter Your Marks out of 100: "))

if (take_marks >= 90  and take_marks <=100):
    print("Ex")
elif (take_marks >=80 and take_marks<90):
    print("Your grade is A")
elif (take_marks >=70 and take_marks<80):
    print("Your grade is B")
elif (take_marks >=60 and take_marks<70):
    print("Your grade is C")
elif (take_marks >=50 and take_marks<60):
    print("Your grade is D")
elif (take_marks<50 and take_marks>=0):
    print("Your grade is Fail")
elif (take_marks>100 or take_marks<0):
    print("This is not valid Numbers")