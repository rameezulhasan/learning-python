# write a python program to print the contents of a directory using the os module. search online for the fuction which does that.

import os

# Current working directory ka path lena
directory_path = "Local Disk (E)"

# Directory ke contents list karna
contents = os.listdir(directory_path)

# Print karna contents
print("Contents of the directory:")
for item in contents:
    print(item)
