# P8: Inheritance and Polymorphism
# Name: ASHLEY MAE CABURNAY
# Section: IV-BSIT A
# Activity: P8
# Date: November 25, 2026

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")


<<<<<<< HEAD
def main():
    print("===== INHERITANCE AND POLYMORPHISM =====")

    dog = Dog("Buddy")
    cat = Cat("Mimi")
=======
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()

        if name:
            return name
        else:
            print("Animal name cannot be empty!")


def main():
    print("===== INHERITANCE AND POLYMORPHISM =====")

    dog_name = get_valid_name("Enter dog name: ")
    cat_name = get_valid_name("Enter cat name: ")

    dog = Dog(dog_name)
    cat = Cat(cat_name)
>>>>>>> 1fcd536 (P8 - Add animal name input validation)

    print("\nDog Information:")
    dog.make_sound()

    print("\nCat Information:")
    cat.make_sound()

    print("\n===== POLYMORPHISM DEMONSTRATION =====")

    animals = [dog, cat]

    for animal in animals:
        animal.make_sound()


if __name__ == "__main__":
    main()