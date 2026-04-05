# Replace the double space with single spaces.

string = "This line have  double  space."
print(f"Original string: {string}")

string2 = string.replace("  ", " ") # This line will replace all double space with single space.
print(f"Removed double space: {string2}")
