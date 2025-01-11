# Student Grade Tracker

print("Welcome to the Student Grade Tracker")

# Dictionary to store student names and grades
students = {}

# Function to add a student and their grade
def add_student(name, grade):
    students[name] = grade
    print(f"Student {name} with grade {grade} added.")

# Function to view all students and their grades
def view_students():
    if students:
        print("Student List:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No students added yet.")

# Function to display all grades in a list
def get_grades():
    grades = list(students.values())
    print("All Grades:", grades)

# Function to check if a student exists and show their grade
def check_student(name):
    if name in students:
        print(f"{name} has a grade of {students[name]}.")
    else:
        print(f"{name} is not in the list.")

# Function to calculate the average grade of all students
def calculate_average():
    if students:
        total = sum(students.values())
        average = total / len(students)
        print(f"Average grade: {average:.2f}")
    else:
        print("No students to calculate the average.")

# Main program loop
while True:
    print("\nOptions: add, view, check, grades, average, exit")
    choice = input("Enter your choice: ").lower()

    if choice == "add":
        name = input("Enter student name: ")
        grade = int(input("Enter student grade (0-100): "))
        add_student(name, grade)
    elif choice == "view":
        view_students()
    elif choice == "check":
        name = input("Enter student name: ")
        check_student(name)
    elif choice == "grades":
        get_grades()
    elif choice == "average":
        calculate_average()
    elif choice == "exit":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
