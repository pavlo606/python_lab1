"""Insects"""
from Insects.managers.insect_manager import InsectManager
from Insects.models.hornet import Hornet
from Insects.models.mosquito import Mosquito

manager = InsectManager([Hornet("Hornet1", "Vespa crabro", 6, True, True), \
                         Hornet("Hornet2", "Vespa crabro", 6), \
                         Mosquito("Mosquito1", 6, True, False, True), \
                         Mosquito("Mosquito2", 6)])

print(manager)
