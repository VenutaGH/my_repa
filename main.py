from itertools import pairwise
import random

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
    def merge(cls, animal1, animal2):
        if type(animal1) != type(animal2):
            print("Cannot merge different types of animals.")
            return None

        animal_cls = type(animal1)

        combined_name = f"{animal1.name}-{animal2.name}"
        new_paws = Paws()
        new_paws.action = f"combo paws of {animal1.name} and {animal2.name}"

        if animal_cls is Kitty:
            combined_ears = f"{animal1.ears}+{animal2.ears}"
            new_animal = animal_cls(combined_ears, combined_name, new_paws)
        else:
            new_animal = animal_cls(combined_name, new_paws)

        new_animal.tail.action = f"merged tails of {animal1.name} and {animal2.name}"
        return new_animal


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

    def add_animal(self, *animals):
        for animal in animals:
            if isinstance(animal, (Kitty, Dogge)):
                self.animals.append(animal)
            else:
                print(f"{animal} — У нас тут только коты и собаки, никаких котопсов.")

    def show_all_animals(self):
        for animal in self.animals:
            animal.perform_actions()

    def animal_hardcore_sex(self, animal1, animal2):
        merged_animal = Animal.merge(animal1, animal2)
        if merged_animal:
            self.add_animal(merged_animal)
            print(f"Жоска переебались,появилось новое животное: {merged_animal.name}")
        else:
            print("поебаться не удалось.")


    @staticmethod
    def no_contraception():
        animal_class = random.choice ([Kitty, Dogge])
        name = 'tyranda'
        paws = Paws()

        if animal_class is Kitty:
                ears = "ripped ears"
                return animal_class(ears, name, paws)
        else:

                return animal_class(name, paws)

    @staticmethod
    def multiple_bithing(n):
        bithed_animals = []
        for i in range(n):
            new_animal = Zoo.no_contraception()
            bithed_animals.append(new_animal)
        return bithed_animals









    # Пример создания животных:
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

    # Создаем зоопарк
zoo = Zoo()

zoo = Zoo()
zoo.add_animal(kitty1, kitty2, dogge1, dogge2)


 # Отображаем всех животных
zoo.show_all_animals()

    # Пример "слияния" двух животных
zoo.animal_hardcore_sex(kitty1, kitty2)
zoo.show_all_animals()

zoo.animal_hardcore_sex(dogge1, dogge2)
zoo.show_all_animals()

    # Пример невозможного слияния
zoo.animal_hardcore_sex(kitty1, dogge1)


new_animal = zoo.no_contraception()

zoo = Zoo()
# zoo.multiple_bithing(1000000000)
pizda_zooparku = zoo.multiple_bithing(50)
print(pizda_zooparku)
zoo.add_animal(*pizda_zooparku)

zoo.show_all_animals()
#
# zoo = Zoo()
# zoo.add_animal(sad asd asd as das d)