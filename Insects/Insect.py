class Insect:
    name: str
    numberOfLegs: int
    has_wings: bool
    is_dangerous: bool
    is_sleeping: bool

    def __init__(self, name: str, numberOfLegs: int, has_wings: bool, is_dangerous: bool, is_sleeping: bool) -> None:
        self.name = name
        self.numberOfLegs = numberOfLegs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    def is_poisonous(self) -> bool:
        return self.is_dangerous
    
    def hibernate(self) -> None:
        self.is_sleeping = True

    def wake_up(self) -> None:
        self.is_sleeping = False

    def __str__(self) -> str:
        attributes = list(self.__annotations__.keys())
        result = f"{self.__class__.__name__}("

        for attribute in attributes:
            if attributes.index(attribute) == 0:
                result += f"{attribute}={self.__getattribute__(attribute)}"
                continue
            result += f", {attribute}={self.__getattribute__(attribute)}"

        result += ")"

        return result