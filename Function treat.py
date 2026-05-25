print("<<<< Welcome To Student Record Manager >>>>")

students = []

while True:

    print("\nSelect an option:")
    print("a. Add student")
    print("b. Display all students")
    print("c. Update student information")
    print("d. Delete student")
    print("e. Display subjects stored")
    print("f. Exit")

    choice = input("Enter your choice: ").lower()

    # Add Student
    if choice == "a":

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        subjects = input("Enter Subjects: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "subjects": subjects
        }

        students.append(student)

        print("Student Added Successfully")

    # Display Students
    elif choice == "b":

        if len(students) == 0:

            print("No student records found")

        else:

            for student in students:

                print(
                    f"Student ID: {student['id']} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Subjects: {student['subjects']}"
                )

    # Update Student
    elif choice == "c":

        update_id = input("Enter Student ID: ")

        for student in students:

            if student["id"] == update_id:

                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["subjects"] = input("Enter New Subjects: ")

                print("Student Updated Successfully")

    # Delete Student
    elif choice == "d":

        delete_id = input("Enter Student ID: ")

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                print("Student Deleted Successfully")

    # Display Subjects
    elif choice == "e":

        print("\nStored Subjects:")

        for student in students:

            print(student["subjects"])

    # Exit
    elif choice == "f":

        print("Thank You")
        break

    else:
        print("Invalid Choice")
