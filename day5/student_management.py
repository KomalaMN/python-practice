students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        students[roll] = {
            "name": name,
            "age": age
        }
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if not students:
            print("No records found.")
        else:
            for roll, details in students.items():
                print("Roll:", roll, "| Name:", details["name"], "| Age:", details["age"])

    # Update Student
    elif choice == "3":
        roll = input("Enter Roll No to update: ")
        if roll in students:
            name = input("Enter new name: ")
            age = input("Enter new age: ")

            students[roll]["name"] = name
            students[roll]["age"] = age
            print("Student updated successfully!")
        else:
            print("Student not found!")

    # Delete Student
    elif choice == "4":
        roll = input("Enter Roll No to delete: ")
        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")
