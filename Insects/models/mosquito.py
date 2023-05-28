"""Mosquito"""
from Insects.models.insect import Insect

class Mosquito(Insect):
    """Mosquito"""

    def __init__(self, name: str, number_of_legs: int, has_wings: bool = True, \
                 is_dangerous: bool = False, is_vector_of_disease: bool = False):
        super().__init__(name, number_of_legs, {"blood", "nectar"}, has_wings, is_dangerous)
        self.is_vector_of_disease = is_vector_of_disease

    def can_inject_poison(self) -> bool:
        return self.is_dangerous

    def survive_over_winter(self) -> bool:
        return False

    def __str__(self) -> str:
        return f"{super().__str__()}, \nis vector of disease: {self.is_vector_of_disease}\n"
