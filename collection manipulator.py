students = {}

while True:
    print("\nWelcome to the Student Data Organizer!\n")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        student_id = input("Student ID: ")

        if student_id in students:
            print("Student ID already exists!")
        else:
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ").split(",")

            subjects = [subject.strip() for subject in subjects]

            students[student_id] = {
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": subjects
            }

            print("\nStudent added successfully!")

    elif choice == "2":
        print("\n--- Display All Students ---")

        if not students:
            print("No students found.")
        else:
            for sid, info in students.items():
                print(
                    f"Student ID: {sid} | "
                    f"Name: {info['Name']} | "
                    f"Age: {info['Age']} | "
                    f"Grade: {info['Grade']} | "
                    f"Subjects: {', '.join(info['Subjects'])}"
                )

    elif choice == "3":
        sid = input("\nEnter Student ID to update: ")

        if sid in students:
            print("Leave blank if you don't want to change the value.")

            name = input(f"New Name ({students[sid]['Name']}): ")
            age = input(f"New Age ({students[sid]['Age']}): ")
            grade = input(f"New Grade ({students[sid]['Grade']}): ")
            dob = input(f"New DOB ({students[sid]['DOB']}): ")
            subjects = input("New Subjects (comma-separated): ")

            if name:
                students[sid]["Name"] = name
            if age:
                students[sid]["Age"] = int(age)
            if grade:
                students[sid]["Grade"] = grade
            if dob:
                students[sid]["DOB"] = dob
            if subjects:
                students[sid]["Subjects"] = [s.strip() for s in subjects.split(",")]

            print("Student information updated successfully!")
        else:
            print("Student not found!")

    elif choice == "4":
        sid = input("\nEnter Student ID to delete: ")

        if sid in students:
            del students[sid]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("\n--- Subjects Offered ---")

        subject_set = set()

        for info in students.values():
            subject_set.update(info["Subjects"])

        if subject_set:
            for subject in sorted(subject_set):
                print(subject)
        else:
            print("No subjects available.")

    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")


Output:
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1

Enter student details:
Student ID: 101
Name: Armin
Age: 20
Grade: A
Date of Birth (YYYY-MM-DD): 2006-05-10
Subjects (comma-separated): Python, Java, C

Student added successfully!

Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 2

--- Display All Students ---
Student ID: 101 | Name: Armin | Age: 20 | Grade: A | Subjects: Python, Java, C

Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 5

--- Subjects Offered ---
C
Java
Python

Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 6

Exiting the program. Goodbye!        