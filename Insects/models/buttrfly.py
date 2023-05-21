"""Butterfly"""
from Insects.models.insect import Insect

class Butterfly(Insect):
    """Butterfly"""

    def __init__(self, name: str, color: str, number_of_legs: int, has_wings: bool = True, \
                 is_dangerous: bool = True):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.color = color

    def can_inject_poison(self) -> bool:
        return self.is_dangerous

    def survive_over_winter(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"{super().__str__()}, \nspecies: {self.color}\n"
