# P2: Custom Module - student_utils
# Name: ASHLEY NAE CABURNAY
# Section: IV-BSIT A

import student_utils
from datetime import datetime

print("===== STUDENT GRADE REPORT =====")
print("Report Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

grades = []

number = int(input("\nHow many grades will you enter? "))

for i in range(number):
    grade = float(input(f"Enter grade {i + 1}: "))
    grades.append(grade)

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