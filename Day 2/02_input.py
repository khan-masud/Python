first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + last_name
print(full_name)
# This operation will return concat of first_name and last_name

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

summ = num1 + num2
print(summ)
# This operation will also concat of num1 and num2. If user enter 2 and 3 as input then it will return "23" not as expected behaviour "5". Because input is always "string".

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

addition = number1 + number2
print(addition)
# This operation will return the real summation of numbers. If user input "2" and "3" as input then it will return "5" as expected behaviour.