# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Activity: P5 - Student Information File System
# Date: November 25, 2026

FILE_NAME = "students.txt"


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    student_id, name, section, average = data
                    students.append({
                        "id": student_id,
                        "name": name,
                        "section": section,
                        "average": average
                    })

    except FileNotFoundError:
        print("No existing records found. Starting with an empty list.")

    return students


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for student in students:
            file.write(
                f"{student['id']},{student['name']},"
                f"{student['section']},{student['average']}\n"
            )


def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter full name: ").strip()
    section = input("Enter course/section: ").strip()

    try:
        average = float(input("Enter general average: "))

        if not 0 <= average <= 100:
            print("Average must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid average. Please enter a number.")
        return

    student = {
        "id": student_id,
        "name": name,
        "section": section,
        "average": average
    }

    students.append(student)
    save_students(students)

    print("Student record saved successfully!")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Course/Section: {student['section']}")
        print(f"General Average: {student['average']}")
        print("--------------------------")


def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\n===== STUDENT FOUND =====")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Course/Section: {student['section']}")
            print(f"General Average: {student['average']}")
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Leave blank if you don't want to change a field.")

            new_name = input("Enter new name: ").strip()
            new_section = input("Enter new course/section: ").strip()
            new_average = input("Enter new general average: ").strip()

            if new_name:
                student["name"] = new_name

            if new_section:
                student["section"] = new_section

            if new_average:
                try:
                    average = float(new_average)

                    if 0 <= average <= 100:
                        student["average"] = average
                    else:
                        print("Average must be between 0 and 100.")
                        return

                except ValueError:
                    print("Invalid average.")
                    return

            save_students(students)
            print("Student information updated successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT INFORMATION SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Information")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()