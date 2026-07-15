from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name: {self.name}  |  Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
        pass


class Cat(Animal):

    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self.color = color

    def speak(self):
        print(f"{self.name} ({self.color}) says: Meow!")


class Elephant(Animal):

    def __init__(self, name, habitat, tusk_size):
        super().__init__(name, habitat)
        self.tusk_size = tusk_size

    def speak(self):
        print(f"{self.name} ({self.tusk_size} tusks) says: Pawoooon! *Trumpet sound*")


class Wolf(Animal):

    def __init__(self, name, habitat, pack):
        super().__init__(name, habitat)
        self.pack = pack

    def speak(self):
        print(f"{self.name} from the {self.pack} pack says: AWOOOOO!")


cat = Cat("Whiskers", "House", "Calico")
elephant = Elephant("Dumbo", "Savannah", "Large")
wolf = Wolf("Luna", "Forest", "Midnight")

print("=== Animal Sound Show ===\n")
for animal in [cat, elephant, wolf]:
    animal.display()
    animal.speak()
    print()