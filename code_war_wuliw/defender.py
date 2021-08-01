from model import *


class Defender:

    def __init__(self, link_to_lib):
        self.link_to_lib = link_to_lib

    def update(self, target_list, result):
        self.defalt(result)

    def defalt(self, result):
        for hous in self.link_to_lib.houses:
            if hous.entity_type == EntityType.TURRET:
                result.entity_actions[hous.id] = EntityAction(
                    move_action=None,
                    build_action=None,
                    attack_action=AttackAction(None, AutoAttack(100, [])),
                    repair_action=None
                )

        for sold in self.link_to_lib.soldiers:
            result.entity_actions[sold.id] = EntityAction(
                move_action=MoveAction(Vec2Int(15, 15),True, True),
                build_action=None,
                attack_action=AttackAction(None, AutoAttack(500, [])),
                repair_action=None
            )