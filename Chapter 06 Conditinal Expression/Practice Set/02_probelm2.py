#    write a program to find out whether a student has passed or fail if it requires a total of 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

paper1 = int(input("Enter Your Marks on Subject 1 from 100:  "))
paper2 = int(input("Enter Your Marks on Subject 2 from 100:  "))
paper3 = int(input("Enter Your Marks on Subject 3 from 100:  "))

take_percentage_paper1 = (paper1/100)*100
take_percentage_paper2 = (paper2/100)*100
take_percentage_paper3 = (paper3/100)*100
total_marks = paper1+ paper2 + paper3
take_percentage_total_marks = (total_marks/300)*100

if (take_percentage_total_marks >= 40 and take_percentage_paper1>=33 and take_percentage_paper2>=33 and take_percentage_paper3>=33):
    print(f"Congratulations! You are pass. Your Total Percentage is {take_percentage_total_marks56}")

else:
    print("Unfortunately! You are Failed")