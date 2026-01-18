# String Functions


name = "Rameez are"

print(len(name))
print(name.endswith("eez")) # true aye ga qu ke end eez  se hi ho rha hai .
print(name.startswith("Ra"))
print(name.capitalize()) #ye pehle word ke pehle character ko capital bna de ga

print(name.count("e")) # count characters in variable
print(name.find("are"))

# a = "hello world"
# print(a.upper())     # ye saray characters ko bara kar deta hai

# a = "I love Javascript"
# print(a.replace("Javascript","Pyhton"))     # ye change kar deta word ko jis word se karwana ho to

# a = "a,b,c,d,e,f"
# print(a.split(","))   # ye string ko list ya array main kar deta hai.

# items = ["apples","banana","grapes"]
# print(", ".join(items))    #list ko string main kar deta hai

# a = "my name is rameez ul hassan"
# print(a.title())    # har word ke pehle character ko bra kar deta hai