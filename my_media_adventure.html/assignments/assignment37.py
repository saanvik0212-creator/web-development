from abc import ABC, abstractmethod

class Instrument(ABC):

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        print(f"Instrument Name: {self.name}")
        print(f"Category: {self.category}")

    @abstractmethod
    def play_sound(self):
        pass

class violin(Instrument):

    def __init__(self, name, category, strings):
        super().__init__(name, category)
        self.strings = strings

    def play_sound(self):
        print(f"{self.name} has {self.strings} strings and sounds like: eng-engg-enggg!")


class Cello(Instrument):

    def __init__(self, name, category, drum_type):
        super().__init__(name, category)
        self.drum_type = drum_type

    def play_sound(self):
        print(f"{self.name} is a {self.drum_type} and sounds like: hum-drum!")

class Triangle(Instrument):

    def __init__(self, name, category, material):
        super().__init__(name, category)
        self.material = material

    def play_sound(self):
        print(f"{self.name} is made of {self.material} and sounds like: ting-tinggg!")


instrument_1 = violin("Violin", "String Instrument", 4)
instrument_2 = Cello("Cello", "String Instrument", "bass drum")
instrument_3 = Triangle("Triangle", "Percussion", "steel")


print("=== Music Instrument Sound Show ===")

instrument_1.display_info()
instrument_1.play_sound()

print()

instrument_2.display_info()
instrument_2.play_sound()

print()

instrument_3.display_info()
instrument_3.play_sound()