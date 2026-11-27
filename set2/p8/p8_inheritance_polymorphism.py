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


def main():
    print("===== INHERITANCE AND POLYMORPHISM =====")

    dog = Dog("Buddy")
    cat = Cat("Mimi")

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