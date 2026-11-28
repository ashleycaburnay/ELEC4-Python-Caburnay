# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 24, 2026

# Global variable to store student grades
grades = []


# Function 1: Enter student grades
def enter_grades():
    global grades

    if grades:
        confirm = input("Replace existing grades? (y/n): ").lower()

        if confirm != "y":
            print("Grade entry cancelled.")
            return

    while True:
        try:
            number = int(input("How many grades will you enter? "))

            if number > 0:
                break
            else:
                print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    grades = []

    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    print("Grades successfully entered!")


# Function 2: Calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 3: Get highest grade
def get_highest(grades):
    return max(grades)


# Function 4: Get lowest grade
def get_lowest(grades):
    return min(grades)


# Function 5: Determine pass or fail
def get_status(grades):
    if calculate_average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 6: Display results
def display_results():
    if not grades:
        print("Please enter grades first.")
        return

    print("\n===== STUDENT GRADE RESULTS =====")
    print(f"Number of Grades: {len(grades)}")
    print(f"Average Grade: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest(grades)}")
    print(f"Lowest Grade: {get_lowest(grades)}")
    print(f"Status: {get_status(grades)}")


# Main menu
def main():
    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            enter_grades()
        elif choice == "2":
            display_results()
        elif choice == "3":
            print("Thank you for using the Student Grade Calculator!")
            break
        else:
            print("Invalid choice. Please try again.")


main()


# Local and Global Variables:
# A global variable can be accessed by different functions in a program.
# In this program, grades is a global variable because it is declared
# outside the functions. A local variable exists only inside the function
# where it is created. For example, number is a local variable inside
# the enter_grades() function.