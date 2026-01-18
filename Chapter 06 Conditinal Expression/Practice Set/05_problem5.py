#  Write a program which finds out whether a given name is present in a list or not. 

name_list = ["Ali","Rameez",'Ahmad',"Haseeb"]
take_name = input("Enter Any name: ")

if (take_name in name_list):
    print(f"Yes {take_name} name is present in list")
else:
    print(f"{take_name} name is not present in list")