from model import *
from code_war_wuliw import *


class MyStrategy:
    def __init__(self):
        self.first_config = True
        #ВНИМАНИЕ НЕ ДИНАМИЧНЫЙ ID
        self.mind = Mind(1)

    def get_action(self, player_view, debug_interface):
        #Как то переделать в будующем
        if self.first_config:
            self.mind.Entity_Properties = player_view.entity_properties
            self.first_config = False

        i = 0
        if i % 10 == 0:
            self.mind.updata(player_view)
        i+=1

        result = Action({})
        my_id = player_view.my_id

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
                build_action = BuildAction(
                        EntityType.BUILDER_UNIT,
                        Vec2Int(entity.position.x + properties.size, entity.position.y + properties.size - 1))

            result.entity_actions[entity.id] = EntityAction(
                move_action,
                build_action,
                AttackAction(None, AutoAttack(properties.sight_range, [EntityType.RESOURCE])),
                None
            )

        return result


    def debug_update(self, player_view, debug_interface):
        debug_interface.send(DebugCommand.Clear())
        debug_interface.get_state()