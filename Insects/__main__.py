"""Insects"""
from Insects.managers.insect_manager import InsectManager
from Insects.models.hornet import Hornet
from Insects.models.mosquito import Mosquito
from Insects.models.buttrfly import Butterfly
from Insects.models.ant import Ant

manager = InsectManager([Hornet("Hornet1", "Vespa crabro", 6, True, True),
                         Hornet("Hornet2", "Vespa crabro", 6),
                         Mosquito("Mosquito1", 4, True, False, True),
                         Mosquito("Mosquito2", 6),
                         Butterfly("Butterfly", "Blue", 4, True, False),
                         Butterfly("Butterfly", "Blue", 4),
                         Ant("Ant", "Fire ant", 6, False, True),
                         Ant("Ant", "Fire ant", 6)])

print(manager.check_condition_all_any(lambda insect: insect.is_dangerous))

# print("All insects:")
# print(manager)

# print("---------------------------------------------")
# print("All dangerous insects:")
# for insect in manager.find_all_dangerous():
#     print(insect)

# print("---------------------------------------------")
# print("All insects with number of legs more then 5:")
# for insect in manager.find_all_with_legs_more_then(5):
#     print(insect)
