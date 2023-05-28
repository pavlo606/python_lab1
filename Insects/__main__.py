"""Insects"""
from Insects.managers.insect_manager import InsectManager
from Insects.managers.insect_set_manager import InsectSetManager
from Insects.models.hornet import Hornet
from Insects.models.mosquito import Mosquito
from Insects.models.buttrfly import Butterfly
from Insects.models.ant import Ant

manager = InsectManager([Hornet("Hornet1", "Vespa crabro", 6, True, True),
                         Hornet("Hornet2", "Vespa ducalis", 6),
                         Mosquito("Mosquito1", 4, True, False, True),
                         Mosquito("Mosquito2", 6),
                         Butterfly("Butterfly", "Blue", 4, True, False),
                         Butterfly("Butterfly", "Red", 4),
                         Ant("Ant", "Fire ant", 6, False, True),
                         Ant("Ant", "Bullet ant", 6)])

print("---------------------------------------------")
print("Enumerated insects:")
print(manager.get_enumarated())

print("---------------------------------------------")
print("Check condition:")
print(manager.check_condition_all_any(lambda insect: insect.can_inject_poison()))

print("---------------------------------------------")
print("Favourite food of all insects in manager:")
sm = InsectSetManager(manager)

for i in sm:
    print(i)

manager.test()
