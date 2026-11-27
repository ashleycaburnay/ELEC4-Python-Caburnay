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


def main():
    print("===== STUDENT CLASS PROGRAM =====")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    student1 = Student(name, age, course)

    student1.display_info()
    student1.introduce()


if __name__ == "__main__":
    main()
