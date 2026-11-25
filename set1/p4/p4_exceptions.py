# P4: Safe Menu Program
# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Activity: P4
# Date: November 24, 2026

def divide_numbers():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = first_number / second_number

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

    else:
        print("Result:", result)

    finally:
        print("Division operation completed.")


def open_file():
    file_name = input("Enter the file name: ").strip()

    if not file_name:
        print("File name cannot be empty.")
        return

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            contents = file.read()

    except FileNotFoundError:
        print("Error! File not found.")

    except PermissionError:
        print("Error! Permission denied.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(contents)

    finally:
        print("File operation completed.")


# Main menu
while True:
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Divide Numbers")
    print("2. Open a File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        divide_numbers()

    elif choice == "2":
        open_file()

    elif choice == "3":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid menu choice! Please select 1, 2, or 3.")