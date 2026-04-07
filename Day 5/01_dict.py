dictionary = {
    "name" : "Abdullah Al Masud",
    "nickname" : "The Offline Dreamer",
    "roll" : 10, 
    "batch" : "D-93",
    "list" : [10, 20, 30]
}

print(dictionary)

print(dictionary.items()) # Get all items
print(dictionary.keys()) # Get all keys
print(dictionary.values()) # Get All values
print(dictionary["name"]) # Get values using the key
dictionary.update({"name" : "Masud", "address" : "Dhaka, Bangladesh"}) # Update list for existing and new items

print(dictionary)

dictionary2 = dictionary.copy() # Copy the dictionary
print("This is dictionary 2: ", dictionary2)

dictionary.pop("batch") # Delete values for specific keys
dictionary.popitem() # Delete last element of dictionary 

print(dictionary.get("phone")) # Returns 'None' if not found value for 'phone'
print(dictionary["phone"]) # Returns error if not found value for 'phone'

