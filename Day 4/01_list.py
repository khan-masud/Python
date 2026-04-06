myList = ["Masud", 10, 93, True, "Python"] # This is a list and this is mutable

print(myList)

# Add an element in the last index
myList.append("Appended element")
print(myList)

# Insert an element in specific index
myList.insert(4, "Inserted element")
print(myList)

# Delete an element with specific index
myList.pop(1)
print(myList)

# Sort the list with ascending order
numbers = [34,5,74.5,7.6,3,32,7,10] # Collection of numeric values
numbers.sort()
print(numbers)

# Reverse a list 
numbers.reverse() # This will return sorted list in descending order because previously I sorted the list in ascending order.
print(numbers)

# Remove a specific element from list
myList.remove(True)
print(myList)

# Count total numbers of an element
numbers.count(7)
print(numbers)

numbers.sort() # Get the numbers list again in ascending
print(numbers)


print(numbers[1:6]) # This line will print from index 1 to 5