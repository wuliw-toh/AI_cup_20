from code_war_wuliw import TargetType
from model import *


class Mayor:

    def __init__(self, link_to_lib):
        self.link_to_lib = link_to_lib

    def update(self, target_list, result):
        """Реализованна логика найми рабочих но пока так себе"""
        # На всякий случай забиваем пустые
        self.defolt(result)

        for tg in target_list:
            if tg[3]:
                continue

            if tg[0] == TargetType.HIRING_BUILDER:
                self.hiring_b(result)
            elif tg[0] == TargetType.HIRING_RANGED:
                self.hiring_r(result)

    def hiring_b(self, result):
        """Реализованна логика найми рабочих но пока так себе"""
        for hous in self.link_to_lib.houses:
            if hous.entity_type == EntityType.BUILDER_BASE:
                result.entity_actions[hous.id] = EntityAction(
                    move_action=None,
                    build_action=BuildAction(
                        EntityType.BUILDER_UNIT,
                        # Вот тут кафики фикированой точки, но по уму надо выбирать позицию
                        Vec2Int(hous.position.x + 5, hous.position.y + 5 - 1)),
                    attack_action=None,
                    repair_action=None
                )

    def hiring_r(self, result):
        for hous in self.link_to_lib.houses:
            if hous.entity_type == EntityType.RANGED_BASE:
                result.entity_actions[hous.id] = EntityAction(
                    move_action=None,
                    build_action=BuildAction(
                        EntityType.RANGED_UNIT,
                        # Вот тут кафики фикированой точки, но по уму надо выбирать позицию
                        Vec2Int(hous.position.x + 5, hous.position.y + 5 - 1)),
                    attack_action=None,
                    repair_action=None
                )

    def defolt(self, result):
        for hous in self.link_to_lib.houses:
            result.entity_actions[hous.id] = EntityAction(
                move_action=None,
                build_action=None,
                attack_action=None,
                repair_action=None
            )