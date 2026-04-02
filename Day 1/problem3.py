"""
Write a python program to print the contents of a directory using the os module.
Search online for the function which does that. 
"""

import os

# Select the directory path
myDirectory = "/" # Single forward slash (/) means current drive 

# Get list of all contents
myContents = os.listdir(myDirectory)

# Print all contents
print(myContents)