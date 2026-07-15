class Pet:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Health Level: {self.health}")

    def care_action(self):
        print(f"{self.name} needs general care.")

    def set_health(self, new_health):
        if 0 <= new_health <= 100:
            self.health = new_health
            print(f"{self.name}'s health updated to {self.health}.")
        else:
            print("Health must be between 0 and 100.")


class Fish(Pet):
    def care_action(self):
        print(f"{self.name} needs a water change and flake food.")


class Dog(Pet):
    def care_action(self):
        print(f"{self.name} needs a walk and some playtime.")


class Cat(Pet):
    def care_action(self):
        print(f"{self.name} needs grooming and quiet rest.")


fish = Fish("Goldie", 85)
dog = Dog("Buddy", 75)
cat = Cat("Misty", 65)

pets = [fish, dog, cat]

print("===== My Pet Care Dashboard =====\n")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print()

print("===== Updating Pet Health =====\n")

fish.set_health(90)
dog.set_health(80)
cat.set_health(70)

print("\n===== Final Pet Care Summary =====\n")

for pet in pets:
    pet.show_info()
    print()