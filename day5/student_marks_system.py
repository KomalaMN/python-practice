students = {}

while True:
    print("\n--- Student Marks System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Show Topper")
    print("6. Show Average")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if not students:
            print("No records found!")
        else:
            print("\nStudent List:")
            for name, marks in students.items():
                print(name, ":", marks)

    # Update Marks
    elif choice == "3":
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated!")
        else:
            print("Student not found!")

    # Delete Student
    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted!")
        else:
            print("Student not found!")

    # Show Topper
    elif choice == "5":
        if students:
            topper = max(students, key=students.get)
            print("Topper:", topper, "-", students[topper])
        else:
            print("No data available!")

    # Show Average
    elif choice == "6":
        if students:
            avg = sum(students.values()) / len(students)
            print("Average Marks:", avg)
        else:
            print("No data available!")

    # Exit
    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
