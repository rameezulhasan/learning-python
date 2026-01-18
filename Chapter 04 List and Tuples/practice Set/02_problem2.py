# write a program to accept marks of 6 students and display them in a sorted manner.

marks_list = []

student1 = int(input("Enter Your Marks Out of 100:  "))
marks_list.append(student1)
student2 = int(input("Enter Your Marks Out of 100:  "))
marks_list.append(student2)
student3 = int(input("Enter Your Marks Out of 100:  "))
marks_list.append(student3)
student4 = int(input("Enter Your Marks Out of 100:  "))
marks_list.append(student4)
student5 = int(input("Enter Your Marks Out of 100:  "))
marks_list.append(student5)
student6 = int(input("Enter Your Marks Out of 100:  "))
marks_list.append(student6)

marks_list.sort()
print(marks_list)