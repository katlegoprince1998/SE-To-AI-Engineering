class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"{self.name} the {self.species} says {sound}" # Example method using self parameter
    
    def get_name(self):
        return self.name
    
    def display_name(self):
        print(f"Animal Name: {self.get_name()}")  # Method calling another method using self parameter

# Example usage:

dog = Animal("Buddy", "Dog")

print(dog.make_sound("Woof"))  # Output: Buddy the Dog says Woof

dog.display_name()  # Output: Animal Name: Buddy
            