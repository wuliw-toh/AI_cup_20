from model import *


class Earner:

    def __init__(self, link_to_lib):
        self.link_to_lib = link_to_lib

    def update(self, target_list, result):
        """Примитивная как лом логика всех лишних рабочих автоатачим на ресурс"""
        for unit in self.link_to_lib.builders:
            result.entity_actions[unit.id] = EntityAction(
                move_action=MoveAction(Vec2Int(72, 72), True, True),
                build_action=None,
                attack_action=AttackAction(None, AutoAttack(200, [EntityType.RESOURCE])),
                repair_action=None
            )
