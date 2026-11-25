# P3: Student Record Manager
# Name:  ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Date: November 24, 2026

# List stores the original student names.
students = []

# Set prevents duplicate names.
student_names = set()


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name.lower() in student_names:
        print("Student already exists!")
    else:
        students.append(name)
        student_names.add(name.lower())
        print("Student added successfully!")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_names.remove(student.lower())
            print("Student removed successfully!")
            return

    print("Student not found.")


def search_student():
    name = input("Enter name to search: ").strip().lower()

    if not name:
        print("Search name cannot be empty.")
        return

    found = False

    for student in students:
        if name in student.lower():
            print("Found:", student)
            found = True

    if not found:
        print("No matching student found.")

def display_students():
    if not students:
        print("No students in the record.")
        return

    print("\n===== STUDENT LIST =====")

    for number, student in enumerate(sorted(students, key=str.lower), start=1):
        print(f"{number}. {student}")

    print("Total students:", len(students))


# Main menu
while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Thank you for using Student Record Manager!")
        break
    else:
        print("Invalid choice. Please select 1-5.")


# Difference between lists and sets:
# A list stores items in order and allows duplicate values.
# A set stores unique values and automatically prevents duplicates.
# In this program, the students list stores the original student names.
# The student_names set checks if a name already exists.