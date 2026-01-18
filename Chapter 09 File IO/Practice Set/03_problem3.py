#  Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

def generatedtables(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {1} = {n*i}\n"
    with open(f"Practice Set/tables/table{n}.txt", "w")as f:
        f.write(table)

for i in range(2,21):
    generatedtables(i)