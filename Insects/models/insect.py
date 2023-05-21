"""Insect class"""
from abc import ABC, abstractmethod

class Insect(ABC):
    """
    Insect
    """
    def __init__(self, name: str, number_of_legs: int, has_wings: bool = False, \
                 is_dangerous: bool = False) -> None:
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous

    @abstractmethod
    def can_inject_poison(self) -> bool:
        """
        Return if insect is poisonous
        """

    @abstractmethod
    def survive_over_winter(self) -> bool:
        """
        Return if insect can survive over winter
        """

    def __repr__(self) -> str:
        attributes = self.__dict__
        return f"{attributes}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}\nname: {self.name}, \n" \
                + f"number of legs: {self.number_of_legs}, \nhas wings: {self.has_wings}, \n" \
                + f"is dangerous: {self.is_dangerous}"
