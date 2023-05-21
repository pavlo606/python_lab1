"""Manager"""
from Insects.models.insect import Insect

class InsectManager:
    """Insect Manager"""
    def __init__(self, insects: list[Insect]):
        self.insects = insects

    def add_insect(self, insect: Insect):
        """Append insects"""
        self.insects.append(insect)

    def del_insect(self, insect: Insect):
        """Delete insect"""
        self.insects.remove(insect)

    def find_all_dangerous(self) -> list[Insect]:
        """Finds all dangerous insects"""
        return list(filter(lambda insect: insect.is_dangerous, self.insects))

    def find_all_with_legs_more_then(self, number_of_legs) -> list[Insect]:
        """Finds all insects with number of legs more then"""
        return list(filter(lambda insect: insect.number_of_legs >= number_of_legs, self.insects))

    def __str__(self) -> str:
        out = str()
        for insect in self.insects:
            out += f"{insect}\n"

        return out
