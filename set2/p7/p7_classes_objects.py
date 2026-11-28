# P7: Classes and Objects
# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Activity: P7
# Date: November 25, 2026

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("\n===== STUDENT INFORMATION =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I am taking {self.course}.")


def get_valid_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value
        else:
            print("Input cannot be empty!")


def get_valid_age():
    while True:
        try:
            age = int(input("Enter student age: "))

            if age > 0:
                return age
            else:
                print("Age must be greater than zero.")

        except ValueError:
            print("Invalid input! Please enter a valid age.")


def main():
    print("===== STUDENT CLASS PROGRAM =====")

    name = get_valid_text("Enter student name: ")
    age = get_valid_age()
    course = get_valid_text("Enter student course: ")

    student1 = Student(name, age, course)

    student1.display_info()
    student1.introduce()


if __name__ == "__main__":
    main()