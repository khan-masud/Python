# Write a program to fill in a letter template  with name and date.

letter = '''
            Dear <|Name|>,
            You are selected!
            <|Date|>'''

name = "Abdullah Al Masud"
date = "5 April 2026"

# Chain of replace functions
myLetter = letter.replace("<|Name|>", name).replace("<|Date|>", date)

print(myLetter)
