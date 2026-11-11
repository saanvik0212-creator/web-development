class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health  
    def show_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Health Level: {self.__health}")

    def care_action(self):
        print(f"{self.name} needs general care.")

    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Health must be between 0 and 100.")

class Turtle(Pet):
    def care_action(self):  
        print(f"{self.name}'s wounds need to be taken care of.")

class Dog(Pet):
    def care_action(self):
        print(f"{self.name} needs to go for a quick walk.")

class Cat(Pet):
    def care_action(self):  
        print(f"{self.name} needs to go to the vet for a check up.")

turtle = Turtle("Rose", 80)
dog = Dog("Bluey", 85)
cat = Cat("casy", 70)

pets = [turtle, dog, cat]

print("=== My Pet Care Dashboard ===")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print()

print("===== Updating Pet Health =====")

turtle.set_health(85)
dog.set_health(90)
cat.set_health(80)

print("=== Final Pet Care Summary ===")

for pet in pets:
    pet.show_info()
    print()