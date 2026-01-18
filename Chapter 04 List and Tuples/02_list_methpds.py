#   List Methods

#           1. append()
# Add an element to the end of the list

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# friends.append("Ali") 
# print(friends)

#           2. insert(index, value)
# Insert element at a specific position

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# friends.insert(1,"Banana")  #
# print(friends)

#            3. extend(iterable)
# Add multiple elements at once

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# friends.extend(["Ahmad","Ali"])
# print(friends)

#            4. pop(index)
# Remove and return element from a position
# If no index is given, it removes from the end.

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# friends.pop(3)
# print(friends)

#            5. remove(value)
# Remove first occurrence of a value

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# friends.remove(5)
# print(friends)

#             6. clear()
# Remove all elements from list

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# friends.clear()
# print(friends)

#             7. sort()
# Sort the list in ascending order (modifies original list)

# numbers = [5,3,1,4,2]
# numbers.sort(reverse=True)
# print(numbers)

# For descending: nums.sort(reverse=True)

#            8. sorted()
# Returns a new sorted list (doesn’t change original)

# numbers = [5,3,1,4,2]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)

#             9. reverse()
# Reverse the list (in-place)

# numbers = [5,3,1,4,2]
# numbers.reverse()
# print(numbers)

#          10. index(value)
# Return index of first match

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# print(friends.index(False))


#          11. count(value)
# Count how many times value appears

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# print(friends.count(5))

#          12. copy()
# Create a shallow copy of the list

# friends = ["apple","orange", 5,346.8, False, "Rameez"]
# new_items = friends.copy()
# print(new_items)

#           Bonus: List Slicing
# Powerful way to access or modify parts of a list

# nums = [0, 1, 2, 3, 4, 5]
# print(nums[1:4])     # [1, 2, 3]
# print(nums[::-1])    # [5, 4, 3, 2, 1, 0] (reversed)