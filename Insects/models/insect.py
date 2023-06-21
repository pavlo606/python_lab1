"""Insect class"""
from abc import ABC, abstractmethod

from Insects.exceptions_templates.insect_sleeping_exception import InsectSleepingException
from Insects.decorators.write_exc import write_exc

class Insect(ABC):
    """
    Insect
    """
    def __init__(self, name: str, number_of_legs: int, favourite_food_set: set[str],
                 has_wings: bool = False, is_dangerous: bool = False, is_sleeping: bool = False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping
        self.favourite_food_set = favourite_food_set
        self.current_food = 0

    @abstractmethod
    def can_inject_poison(self) -> bool:
        """
        Return true if insect is poisonous
        """

    @abstractmethod
    def survive_over_winter(self) -> bool:
        """
        Return true if insect can survive over winter
        """

    @write_exc
    def hibernate(self):
        """
        Make insect go sleeping
        """
        if self.is_sleeping is False:
            self.is_sleeping = True
        else:
            raise InsectSleepingException("Insect has already hibernated")

    @write_exc
    def wake_up(self):
        """
        Make insect wake up
        """
        if self.is_sleeping is True:
            self.is_sleeping = False
        else:
            raise InsectSleepingException("Insect has already woke up")

    def get_attributes_by_type(self, val_type) -> dict:
        """Return dictionary of attributes that have this val_type"""
        attributes = self.__dict__
        return {key: val for key, val in attributes.items() if isinstance(val, val_type)}

    def __repr__(self):
        return f"{self.__dict__}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}\nname: {self.name}, \n" \
                + f"number of legs: {self.number_of_legs}, \nhas wings: {self.has_wings}, \n" \
                + f"is dangerous: {self.is_dangerous}"

    def __iter__(self):
        self.current_food = 0
        return self

    def __next__(self):
        if self.current_food < len(self.favourite_food_set):
            idx = self.current_food
            self.current_food += 1
            return list(self.favourite_food_set)[idx]
        raise StopIteration
