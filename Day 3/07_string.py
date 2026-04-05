name = "Abdullah Al Masud"

# Find the length of string
print(len(name))

# Upper case 
print(name.upper())

# Lower case 
print(name.lower())

# Capitalize the string
name_lower = "abdullah al masud" 
print(name.capitalize())

# Make a title of a string
print(name.title())

# Print a character from a string
string = "Masud" # Print 'u' from 'Masud'
print("Printed using positive index: ", name[3])
print("Printed using negative index: ", name[-2])

# Print some random characters from a string
string2 = "Abdullah" # Print 'ull' from 'Abdullah'
print("Printed using postive index: ", string2[3:6])
print("Printed using negative index: ", string2[-5:-2])

# startswith() and endswith()
print(name.startswith("Abdullah")) # This will return True
print(name.startswith("AbdullaH")) # This will return False because this function is case-sensitive

print(name.endswith("Masud")) # This will return True
print(name.endswith("MasuD")) # This will return False because this function is case-sensitive

# Find a string in a string
string3 = "This a string." # Find 'string'
print(string3.find("string")) # This will return 7 as the index 's' of 'string'
print(string3.find("an")) # This will return -1 that means string 'an' is not found

# Replace in a string
sentence = "This is made by Abdullah Al Masud"
print("Original sentence: ", sentence)
print(sentence.replace("Abdullah Al Masud", "Masud"))

# Count number of a character in a string
my_name = "Abdullah Al Masud" # Count number of 'a'
print(my_name.count("a")) # This will return '2' as number of small a is 2. Capital A will not count because this is function is case-sensitive.

# Escape sequence character
string4 = "Hello, This is Masud. \nI call myself as The Offline Dreamer." # \n will print a new line
print(string4)
string5 = "I am learning \"Python\"" # \" will print ' "" ' 
print(string5)

