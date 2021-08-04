from code_war_wuliw import TargetType
from model import *
from code_war_wuliw.libview import dlinna

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
            elif tg[0] == TargetType.BUILDING_HOUSE:
                self.building_house(result)
            elif tg[0] == TargetType.FIX_HOUSE:
                self.fix_work(result, tg[1], tg[2])
                tg[3] = True

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

    def building_house(self, result):
        target = self.link_to_lib.map.find_position(5)
        min_len = 500
        unit = self.link_to_lib.builders[0]

        for bul in self.link_to_lib.builders:
            if dlinna(bul.position, target) < min_len:
                unit = bul

        result.entity_actions[unit.id] = EntityAction(
            move_action=MoveAction(target, True, True),
            build_action=BuildAction(EntityType.HOUSE, Vec2Int(target.x + 1, target.y)),
            attack_action=None,
            repair_action=None
        )
        self.link_to_lib.remove_builders([unit])

    def defolt(self, result):
        for hous in self.link_to_lib.houses:
            result.entity_actions[hous.id] = EntityAction(
                move_action=None,
                build_action=None,
                attack_action=None,
                repair_action=None
            )

    def fix_work(self, result, id_t, kol_unit):
        max_unit = kol_unit

        for i in range(max_unit):
            result.entity_actions[self.link_to_lib.builders[i].id] = EntityAction(
                move_action=None,
                build_action=None,
                attack_action=None,
                repair_action=RepairAction(id_t)
            )
            self.link_to_lib.remove_builders([self.link_to_lib.builders[i]])
