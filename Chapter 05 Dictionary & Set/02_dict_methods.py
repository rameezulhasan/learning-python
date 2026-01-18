student = {
    "name": "Ali",
    "age": 20,
    "grades": [88, 92, 85]
}

#          1. get(key, default=None)
# Safely get a value without crashing if key doesn’t exist.

# print(student.get("grades"))

#            2. keys()
# Returns a view of all the keys.

# print(student.keys())

#             3. values()
# Returns a view of all the values.

# print(student.values())

#              4. items()
# Returns all key-value pairs as tuples.

# print(student.items())

#              5. update()
# Add or update key-value pairs from another dict.

# student.update({"age":21, "gender":"male"})
# print(student)

#              6. pop(key, default)
# Removes a key and returns its value.

# print(student.pop("age"))

#              7. popitem()
# Removes and returns the last inserted item.

# print(student.popitem())

# 8. clear()
# Empties the entire dictionary.

# print(student.clear())

#              10. fromkeys(keys, value)
# Creates a new dictionary with given keys and same default value.

# print(student.fromkeys(["gender","class"]))


#              Bonus Tips
# You can check if a key exists using:

# if "name" in student:
#  print("yes")


# You can loop through keys or values directly:

for key in student:
    print(key)

for value in student.values():
    print(value)  
