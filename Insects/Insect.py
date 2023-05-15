"""Insect class"""

class Insect:
    """
    Insect
    """
    __instance = None

    def __init__(self, name: str, number_of_legs: int, has_wings: bool = False, \
                 is_dangerous: bool = False, is_sleeping: bool = False) -> None:
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    @staticmethod
    def get_instance():
        """
        Returns Instance of this class
        """
        if Insect.__instance is None:
            Insect.__instance = Insect("", 0)
        return Insect.__instance

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
