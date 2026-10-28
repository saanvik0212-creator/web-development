class parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
        print(f"{self.name} sings {song}")
    def dance(self):
        return "{} is now dancing".format(self.name)
        print(f"{self.name} is now dancing")

snowflake = parrot("snowflake", 14)

song = snowflake.sing("wxyz")
print(song)
print(snowflake.dance())

abc=parrot("saanvi", 14)
song = abc.sing("levitating")
print(song)
print(abc.dance())