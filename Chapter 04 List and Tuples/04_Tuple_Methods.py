#  Tuple Methods

#           1. count(value)
# Returns how many times a value appears

# data_list = (2, False, 5.89, "Rameez", "mango")
# print(data_list.count(2))

#            2. index(value)
# Returns the first index where the value is found

# data_list = (2, False, 5.89, "Rameez", "mango")
# print(data_list.index(5.89))
        #    - - - - - - -  - - - -  -
# Tuple unpacking

# data_list = (2, False, 5.89, "Rameez", "mango")
# a,b,c,d,e = data_list
# print(a,b,c,d,e)
        #    - - - - - - - - - - - -  -
# in keyword
# Check if value exists in a tuple

# data_list = (2, False, 5.89, "Rameez", "mango")
# print(True in data_list)

            #   - - - - - - - - - - - -

# sum(), min(), max() — for numeric tuples

numbers = (2,  5.89, 5, 2.69, 1.98,8)
print(min(numbers))
print(sum(numbers))
print(max(numbers))