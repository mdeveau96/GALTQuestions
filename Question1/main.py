import sys
import pprint
from dataclasses import dataclass


@dataclass
class Animal:
    """Animal Super Class"""

    name: str
    age: int
    species: str


@dataclass
class Mammal(Animal):
    """Mammal Subclass

    aquatic: boolean - special attribute of Mammal class
    """

    is_aquatic: bool = False


@dataclass
class Bird(Animal):
    """Bird Subclass

    can_fly: boolean - special attribute of Bird class
    """

    can_fly: bool = True


@dataclass
class Reptile(Animal):
    """
    Reptile Subclass

    venomous: boolean - special attribute of Reptile class
    """

    is_venomous: bool = False


# Zoo Class
class Zoo:
    """
    Zoo class

    __dict_of_animals: Dict - private dictionary of all zoo animals split into categories
    """

    def __init__(self) -> None:
        self.__dict_of_animals = {"Mammals": [], "Birds": [], "Reptiles": []}

    def add_animal(self, new_animal: Animal) -> None:
        """
        Adds new animal from user input to __dict_of_animals. Also used for initializing dictionary

        new_animal: Animal - new animal object of either Mammal, Bird, or Reptile. Inherits attributes from Animal class
        """
        if isinstance(new_animal, Mammal):
            self.__dict_of_animals["Mammals"].append(new_animal)
        elif isinstance(new_animal, Bird):
            self.__dict_of_animals["Birds"].append(new_animal)
        elif isinstance(new_animal, Reptile):
            self.__dict_of_animals["Reptiles"].append(new_animal)
        else:
            return f"Unable to add {new_animal} to Zoo"
        return f"Added {new_animal} to Zoo."

    def get_all_animals_by_category(self) -> str:
        """
        Returns all animals in each category
        """
        return self.__dict_of_animals

    def get_animals_in_category(self, animal_category: str) -> str:
        """
        Returns list of animal objects of specified animals category.
        If no category matches user input, error statement is returned.

        animal_category: str - animal category specified from user input
        """
        for category, animals in self.__dict_of_animals.items():
            if animal_category == category:
                return animals
        return f"There is no category named: {animal_category}."

    def get_animal(self, animal_name: str) -> str:
        """
        Returns animal object specifed from user input.
        If specified animal is not in dictionary, error statement is returned.

        animal_name: str - name of animal object specified from user input
        """
        for animals in self.__dict_of_animals.values():
            for animal in animals:
                if animal_name == animal.name:
                    return animal
        return f"There is no animal with name: {animal_name} in this Zoo"

    def remove_animal_from_category(self, animal_name: str) -> str:
        """
        Removes a selected animal from dictionary.
        If specified animal is not in dictionary, error statement is returned.

        animal_name: str - name of animal object specified from user input
        """
        for animals in self.__dict_of_animals.values():
            for animal in animals:
                if animal_name == animal.name:
                    try:
                        animals.remove(animal)
                        return f"Animal: {animal_name} removed from Zoo."
                    except ValueError:
                        return f"Unable to remove animal: {animal_name} from Zoo."
        return f"There is no animal with name: {animal_name} in this Zoo"
    

def string_to_bool(string: str) -> bool:
    """
    Helper function to handle converting strings to boolean for special attributes

    string: str - input that will be converted to boolean
    """
    if string.lower == "true":
        return True
    else:
        return False


def main():
    """
    Command line tool
    """
    # Intialize Zoo Class
    zoo = Zoo()

    # Populate dictionary
    zoo.add_animal(Mammal(name="Lion", age=5, species="Panthera leo", is_aquatic=False))
    zoo.add_animal(Mammal(name="Tiger", age=3, species="Panthera tigris", is_aquatic=False))
    zoo.add_animal(Mammal(name="Elephant", age=7, species="Loxodonta africana", is_aquatic=False))
    zoo.add_animal(Mammal(name="Zebra", age=10, species="subgenus Hippotigris", is_aquatic=False))
    zoo.add_animal(Mammal(name="Gorilla", age=2, species="Troglodytes gorilla", is_aquatic=False))
    zoo.add_animal(Mammal(name="Panda", age=4, species="Ailuropoda melanoleuca", is_aquatic=False))
    zoo.add_animal(Mammal(name="Koala", age=4, species="Phascolarctos cinereus", is_aquatic=False))
    zoo.add_animal(Mammal(name="Kangaroo", age=6, species="Macropus genus", is_aquatic=False))
    zoo.add_animal(Reptile(name="Crocodile", age=2, species="Crocodylidae", is_venomous=False))
    zoo.add_animal(Mammal(name="Hippopotamus", age=7, species="Hippopotamus amphibius", is_aquatic=True))
    zoo.add_animal(Mammal(name="Rhinoceros", age=5, species="Ceratotherium simum", is_aquatic=False))
    zoo.add_animal(Mammal(name="Polar Bear", age=9, species="Ursus maritimus", is_aquatic=False))
    zoo.add_animal(Mammal(name="Grizzly Bear", age=4, species="Ursus arctos horribilis", is_aquatic=False))
    zoo.add_animal(Bird(name="Penguin", age=8, species="Sphenisciformes", can_fly=False))
    zoo.add_animal(Bird(name="Flamingo", age=7, species="Phoenicopteridae", can_fly=True))
    zoo.add_animal(Bird(name="Parrot", age=13, species="Psittaciformes", can_fly=True))
    zoo.add_animal(Reptile(name="Snake", age=2, species="Serpentes", is_venomous=True))
    zoo.add_animal(Reptile(name="Tortoise", age=40, species="Testudinidae", is_venomous=False))

    # Start Command Line interface
    while True:
        print("\n\033[1mZoo Menu\033[0m")
        print("add - Add new animal")
        print("viewall - View all zoo animals")
        print("viewcat - View all animals in a given category")
        print("view - view list of animals by category")
        print("delete - remove animal from zoo (requires animal name)")
        print("exit - exits application")
        print("=======================================================")

        action = input("Enter your action here: ").strip()

        match action:
            case "add":
                new_animal = (
                    input(
                        "Enter the animal you would like to add. <Ex: name, age, species, special attribute <aquatic=true, can_fly=True, venomous=True>>: "
                    )
                    .strip()
                    .split(", ")
                )
                if new_animal[3].split("=")[0] == "can_fly":
                    zoo.add_animal(
                        Bird(
                            name=new_animal[0],
                            age=new_animal[1],
                            species=new_animal[2],
                            can_fly=string_to_bool(new_animal[3]),
                        )
                    )
                    print(f"Added new animal: {new_animal[0]} to Zoo.")
                elif new_animal[3].split("=")[0] == "aquatic":
                    zoo.add_animal(
                        Mammal(
                            name=new_animal[0],
                            age=new_animal[1],
                            species=new_animal[2],
                            is_aquatic=string_to_bool(new_animal[3]),
                        )
                    )
                    print(f"Added new animal: {new_animal[0]} to Zoo.")
                elif new_animal[3].split("=")[0] == "venomous":
                    zoo.add_animal(
                        Reptile(
                            name=new_animal[0],
                            age=new_animal[1],
                            species=new_animal[2],
                            is_venomous=string_to_bool(new_animal[3]),
                        )
                    )
                    print(f"Added new animal: {new_animal[0]} to Zoo.")
                else:
                    print(f"Could not new animal: {new_animal[0]} to Zoo.")
            case "viewall":
                pp = pprint.PrettyPrinter(indent=2)
                pp.pprint(zoo.get_all_animals_by_category())
            case "viewcat":
                animal_category = input(
                    "Enter the animal category you would like to view: "
                ).strip()
                pp = pprint.PrettyPrinter(indent=2)
                pp.pprint(zoo.get_animals_in_category(animal_category=animal_category))
            case "view":
                animal_name = input(
                    "Enter the animal name you would like to view: "
                ).strip()
                print(zoo.get_animal(animal_name=animal_name))
            case "delete":
                animal_name = input("Enter animal you would like to remove: ").strip()
                print(zoo.remove_animal_from_category(animal_name=animal_name))
            case "exit":
                print("Exiting...")
                sys.exit(0)
            case _:
                print("Invalid command given. Please enter command from list.")


if __name__ == "__main__":
    main()
