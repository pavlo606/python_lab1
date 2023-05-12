"""Insect class"""

class Insect:
    """
    Insect
    """
    __name: str
    __number_of_legs: int
    __has_wings: bool
    __is_dangerous: bool
    __is_sleeping: bool

    def __init__(self, name: str, number_of_legs: int, \
                 has_wings: bool, is_dangerous: bool, is_sleeping: bool) -> None:
        self.__name = name
        self.__number_of_legs = number_of_legs
        self.__has_wings = has_wings
        self.__is_dangerous = is_dangerous
        self.__is_sleeping = is_sleeping

    @property
    def name(self) -> str:
        """Getter, Setter"""
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def number_of_legs(self) -> int:
        """Getter, Setter"""
        return self.__number_of_legs

    @number_of_legs.setter
    def number_of_legs(self, number_of_legs) -> None:
        self.__number_of_legs = number_of_legs

    @property
    def has_wings(self) -> int:
        """Getter, Setter"""
        return self.__has_wings

    @has_wings.setter
    def has_wings(self, has_wings) -> None:
        self.__has_wings = has_wings

    @property
    def is_dangerous(self) -> bool:
        """Getter, Setter"""
        return self.__is_dangerous

    @is_dangerous.setter
    def is_dangerous(self, is_dangerous) -> None:
        self.__is_dangerous = is_dangerous

    @property
    def is_sleeping(self) -> bool:
        """Getter, Setter"""
        return self.__is_sleeping

    @is_sleeping.setter
    def is_sleeping(self, is_sleeping) -> None:
        self.__is_sleeping = is_sleeping

    def is_poisonous(self) -> bool:
        """
        Return if insect is poisonous
        """
        return self.is_dangerous

    def hibernate(self) -> None:
        """
        Makes insect sleep
        """
        self.is_sleeping = True

    def wake_up(self) -> None:
        """
        Makes insect wake up
        """
        self.is_sleeping = False

    def __repr__(self) -> str:
        attributes = self.__dict__
        return f"{attributes}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name: {self.name}, " \
                + f"number of legs: {self.number_of_legs}, has wings: {self.has_wings}, " \
                + f"is dangerous: {self.is_dangerous}, is sleeping: {self.is_sleeping})"
    