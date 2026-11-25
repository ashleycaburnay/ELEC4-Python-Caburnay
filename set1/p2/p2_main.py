# P2: Custom Module - student_utils
# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A

import student_utils
from datetime import datetime

print("===== STUDENT GRADE REPORT =====")
print("Report Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

grades = []

# Validate number of grades
while True:
    try:
        number = int(input("\nHow many grades will you enter? "))

        if number > 0:
            break
        else:
            print("Please enter a number greater than zero.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Validate each grade
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

# Calculate results using student_utils module
average = student_utils.calculate_average(grades)
status = student_utils.determine_status(average)
highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)

print("\n===== RESULTS =====")
print("Grades:", grades)
print(f"Average: {average:.2f}")
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Status:", status)