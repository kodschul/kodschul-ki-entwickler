class Animal:
    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age

    def speak(self) -> str:
        return f"{self.name} makes a sound."

    def celebrate_birthday(self) -> None:
        self.age += 1

    def info(self) -> str:
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"


if __name__ == "__main__":
    animal = Animal("Luna", "Cat", 3)
    print(animal.info())
    print(animal.speak())
    animal.celebrate_birthday()
    print("After birthday:", animal.info())