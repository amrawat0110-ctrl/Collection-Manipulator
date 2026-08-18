# 🎓 Student Data Organizer

## 📖 Project Description

The **Student Data Organizer** is a menu-driven Python application designed to manage student information efficiently. It allows users to add, display, update, and delete student records, as well as display the subjects offered by the students.

Student records are stored in a Python dictionary while the program is running. Each record contains the Student ID, Name, Age, Grade, Date of Birth, and Subjects. The project demonstrates important Python concepts such as dictionaries, lists, sets, loops, conditional statements, functions through built-in operations, and user input. 

## ✨ Features

- ➕ Add a new student
- 📋 Display all student records
- ✏️ Update existing student information
- 🗑️ Delete a student record
- 📚 Display all subjects offered
- 🔎 Prevents duplicate Student IDs
- ⚠️ Displays a message when a student is not found
- 🧹 Removes extra spaces from subject names
- 🔤 Displays subjects in sorted order
- 🚪 Exit option through a menu-driven interface

## 🛠️ Technologies Used

- **Python 3**
- Dictionaries
- Lists
- Sets
- `while` loop
- `if-elif-else` statements
- User input with `input()`
- Type conversion with `int()`
- String methods such as `split()` and `strip()`
- Dictionary operations such as `update()` and `del()`

## 📥 Installation

### Prerequisites

Install **Python 3** on your computer.

### Steps

1. Download or clone the project.
2. Save the Python file in your project folder.
3. Open Command Prompt or Terminal in that folder.
4. Run the program using:

```bash
python "collection manipulator.py"
```

## ▶️ Usage

After starting the program:

1. Select an option from the menu.
2. Choose **Add Student** to enter student details.
3. Choose **Display All Students** to view saved records.
4. Choose **Update Student Information** to modify a record.
5. Choose **Delete Student** to remove a record.
6. Choose **Display Subjects Offered** to see the unique subjects.
7. Choose **Exit** to close the program.

The available menu options are directly implemented in the uploaded project. 

## 📁 Project Structure

```text
Student-Data-Organizer/
│
├── collection manipulator.py
└── README.md
```

## 🔄 Flowchart

```text
                 ┌───────────────┐
                 │     START     │
                 └───────┬───────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Display Main Menu   │
              └──────────┬──────────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Enter Choice  │
                 └───────┬───────┘
                         │
        ┌────────────────┼─────────────────────┐
        │                │                     │
        ▼                ▼                     ▼
   ┌─────────┐     ┌─────────────┐      ┌─────────────┐
   │ Add     │     │ Display /   │      │ Update      │
   │ Student │     │ Manage Data │      │ Information │
   └────┬────┘     └──────┬──────┘      └──────┬──────┘
        │                 │                    │
        ▼                 ▼                    ▼
   Save Record       Show Records         Modify Record
        │                 │                    │
        └─────────────────┼────────────────────┘
                          │
                          ▼
                  ┌─────────────────┐
                  │ Delete Student  │
                  │ or Show Subjects│
                  └────────┬────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Exit?       │
                    └──────┬──────┘
                       No  │  Yes
                           │
              ┌────────────┘ ┌──────────────┐
              ▼              │     END      │
       ┌──────────────┐      └──────────────┘
       │ Display Menu │
       └──────────────┘
```

## 💻 Sample Output

```text
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

--- Display All Students ---
Student ID: 101 | Name: Armin | Age: 20 | Grade: A | Subjects: Python, Java, C

--- Subjects Offered ---
C
Java
Python

Exiting the program. Goodbye!
```

The sample output above is based on the output included with the uploaded Python project. 

## 🚀 Future Improvements

- 💾 Store student records permanently using a file or database
- 🔐 Add a login/authentication system
- 🔍 Add advanced search and filtering
- 📊 Generate student reports
- 🖥️ Create a graphical user interface using Tkinter
- 📁 Export student information to CSV or Excel
- ✅ Add stronger input validation and exception handling

## 👨‍💻 Author

**Name:** Armin Khareghat

**Course:** Python / AI-ML Data Science

**Project:** Student Data Organizer

## 📄 License

This project is created for educational and learning purposes.
