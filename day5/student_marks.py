students = {}

n = int(input("Enter number of students: "))

# Adding student details
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Display all students
print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Find Topper
topper = max(students, key=students.get)
print("\nTopper:", topper, "-", students[topper])

# Find Average
avg = sum(students.values()) / len(students)
print("Average Marks:", avg)
