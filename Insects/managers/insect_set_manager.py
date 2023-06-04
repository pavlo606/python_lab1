"""Set manager"""
from Insects.managers.insect_manager import InsectManager

class InsectSetManager:
    """The manager is aimed only to working with the data of a favourite food set of objects"""
    def __init__(self, regular_manager: InsectManager):
        self.regular_manager = regular_manager
        self.current_insect = 0

    def __len__(self):
        return len(self.regular_manager.insects)

    def __getitem__(self, index):
        return self.regular_manager.insects[index]

    def __iter__(self):
        self.current_insect = 0
        return self

    def __next__(self):
        try:
            return next(self[self.current_insect])

        except StopIteration as exc:
            self.current_insect += 1
            if self.current_insect < len(self):
                return next(self[self.current_insect])

            raise exc
