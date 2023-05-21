"""Manager"""
from Insects.models.insect import Insect

class InsectManager:
    """Insect Manager"""
    def __init__(self, insects: list[Insect]):
        self.insects = insects

    def add_insects(self, insects: list[Insect]):
        """Append insects"""
        self.insects += insects

    def del_insect(self, insect: Insect):
        """Delete insect"""
        self.insects.remove(insect)

    def __str__(self) -> str:
        out = str()
        for insect in self.insects:
            out += f"{insect}\n"

        return out
