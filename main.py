from itertools import pairwise


class Paws:
    def __init__(self):
        self.action = None

    def do_action(self):
        if self.action:
            print(f"Paws: {self.action}")
        else:
            print("Paws do nothing.")


class Tail:
    def __init__(self):
        self.action = None

    def do_action(self):
        if self.action:
            print(f"Tail: {self.action}")
        else:
            print("Tail does nothing.")


class Animal:
    head = True  # class-level attribute

    def __init__(self, name, paws):
        self.name = name
        self.paws = paws
        self.tail = Tail()

    def perform_actions(self):
        print(f"{self.name} is doing pet things:")
        self.paws.do_action()
        self.tail.do_action()

    @classmethod
    def merge(cls, kitty1, kitty2):
        combined_name = f"{kitty1.name}-{kitty2.name}"
        combined_ears = f"{kitty1.ears}+{kitty2.ears}"
        new_paws = Paws()
        new_paws.action = f"combo paws of {kitty1.name} and {kitty2.name}"

        new_kitty = Kitty(combined_ears, combined_name, new_paws)
        new_kitty.tail.action = f"merged tails of {kitty1.name} and {kitty2.name}"
        cls.head = False
        return new_kitty


class Kitty(Animal):
    def __init__(self, ears, name, paws):
        super().__init__(name, paws)
        self.ears = ears




class Dogge(Animal):
    def __init__(self, name, paws):
        super().__init__(name, paws)
        self.head = True


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, (Kitty, Dogge)):
            self.animals.append(animal)
        else:
            print("У нас тут только коты и собаки.")

    def show_all_animals(self):
        for animal in self.animals:
            animal.perform_actions()

    def merge_animals(self, animal1, animal2):
        if isinstance(animal1, Kitty) and isinstance(animal2, Kitty):
            new_kitty = Animal.merge(animal1, animal2)
            self.add_animal(new_kitty)
            return new_kitty

        elif isinstance(animal1, Dogge) and isinstance(animal2, Dogge):
            combined_name = f"{animal1.name}-{animal2.name}"
            new_dogge = Dogge(combined_name, Paws())
            new_dogge.paws.action = f"giving a paw of {animal1.name} and {animal2.name}"
            self.add_animal(new_dogge)
            return new_dogge

        else:
            print("Cannot merge different types of animals.")
            return None

















paws1 = Paws()
paws1.action = "pawing the ground"
kitty1 = Kitty("Pointy", "Kitty1", paws1)

paws2 = Paws()
paws2.action = "chasing a mouse"
kitty2 = Kitty("Fluffy", "Kitty2", paws2)

paws3 = Paws()
paws3.action = "giving a paw"
dogge1 = Dogge("Rex", paws3)

paws4 = Paws()
paws4.action = "running fast"
dogge2 = Dogge("Max", paws4)

# creating Zoo
zoo = Zoo()
zoo.add_animal(kitty1)
zoo.add_animal(kitty2)
zoo.add_animal(dogge1)
zoo.add_animal(dogge2)

zoo.show_all_animals()

# Merge two cats
merged_kitty = zoo.merge_animals(kitty1, kitty2)
zoo.show_all_animals()

# Merge two dogs
merged_dogge = zoo.merge_animals(dogge1, dogge2)
zoo.show_all_animals()

# trying to merge two different pets (Kitty и Dogge)
zoo.merge_animals(kitty1, dogge1)

