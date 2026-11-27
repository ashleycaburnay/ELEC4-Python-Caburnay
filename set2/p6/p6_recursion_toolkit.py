# P6: Recursion Toolkit
# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Activity: P6
# Date: November 25, 2026

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)


def main():
    while True:
        print("\n===== RECURSION TOOLKIT =====")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Countdown")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a number: "))

            if number < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print("Factorial:", factorial(number))

        elif choice == "2":
            number = int(input("Enter the number of terms: "))

            if number <= 0:
                print("Please enter a positive number.")
            else:
                print("Fibonacci sequence:")

                for i in range(number):
                    print(fibonacci(i), end=" ")

                print()

        elif choice == "3":
            number = int(input("Enter countdown starting number: "))
            countdown(number)

        elif choice == "4":
            print("Thank you for using Recursion Toolkit!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    main()