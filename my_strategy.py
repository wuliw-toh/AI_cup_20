from model import *
from code_war_wuliw import *


class MyStrategy:
    def __init__(self):
        self.squad = Squad(1,Vec2Int(6,6),None)
        #ВАЖНО!!! ТУТ НЕ ДИНАМИЧЕКИЙ id
        self.mind = Mind(1)

    def get_action(self, player_view, debug_interface):
        result = Action({})

        my_id = player_view.my_id
        #my_list_ent = self.my_unit(player_view.entities, my_id)
        o_m , n_m = self.mind.chek_unit(player_view.entities)
        print(o_m)
        print(n_m)

        #Стратегия быстрого старта
        for entity in player_view.entities:
            if entity.player_id != my_id:
                continue
            properties = player_view.entity_properties[entity.entity_type]

            move_action = None
            build_action = None

            if properties.can_move:
                move_action = MoveAction(
                    Vec2Int(player_view.map_size - 1,
                            player_view.map_size - 1),
                    True,
                    True)

            elif properties.build is not None:
                entity_type = properties.build.options[0]
                current_units = 0
                for other_entity in player_view.entities:
                    if my_id == other_entity.player_id and other_entity.entity_type == entity_type:
                        current_units += 1
                if (current_units + 1) * player_view.entity_properties[entity_type].population_use <= properties.population_provide:
                    build_action = BuildAction(
                        entity_type,
                        Vec2Int(entity.position.x + properties.size, entity.position.y + properties.size - 1))

            result.entity_actions[entity.id] = EntityAction(
                move_action,
                build_action,
                AttackAction(None, AutoAttack(properties.sight_range, [
                             EntityType.RESOURCE] if entity.entity_type == EntityType.BUILDER_UNIT else [])),
                None
            )

        return result


    def debug_update(self, player_view, debug_interface):
        debug_interface.send(DebugCommand.Clear())
        debug_interface.get_state()