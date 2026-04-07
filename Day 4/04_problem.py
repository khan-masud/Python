# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

m1 = int(input("Enter mark of student 1: "))
marks.append(m1)
m2 = int(input("Enter mark of student 2: "))
marks.append(m2)
m3 = int(input("Enter mark of student 3: "))
marks.append(m3)
m4 = int(input("Enter mark of student 4: "))
marks.append(m4)
m5 = int(input("Enter mark of student 5: "))
marks.append(m5)
m6 = int(input("Enter mark of student 6: "))
marks.append(m6)

print(f"Unsorted marks: {marks}")

marks.sort()

print(f"Sorted marks: {marks}")

