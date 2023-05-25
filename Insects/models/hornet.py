"""Hornet"""
from Insects.models.insect import Insect

class Hornet(Insect):
    """Hornet"""

    def __init__(self, name: str, species: str, number_of_legs: int, has_wings: bool = True, \
                 is_dangerous: bool = True):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.species = species

    def can_inject_poison(self) -> bool:
        return self.is_dangerous

    def survive_over_winter(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"{super().__str__()}, \nspecies: {self.species}\n"
