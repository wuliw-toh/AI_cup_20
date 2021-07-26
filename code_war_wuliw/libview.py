import code_war_wuliw
from model import EntityType


def find_ent_type(entities, ent_type, target_id):
    """
    Функция ищет в масиве сущьностей сущьность конкретного типа
    """
    out = []
    for ent in entities:

        if ent.player_id != target_id:
            continue

        if ent.entity_type in ent_type:
            out.append(ent)

    return out


def find_house(entities, target_id, config):
    """
    В списке сущбностей ищем здания
    """
    out = []
    for ent in entities:
        if ent.player_id != target_id:
            continue

        if not config[ent.entity_type].can_move:
            out.append(ent)
    return out


class LibView:

    def __init__(self):
        self.map = MapScan()

    def update(self, player_vive):
        self.my_id = player_vive.my_id
        self.ent_config = player_vive.entity_properties

        # определяем доступный ресурс
        for i in player_vive.players:
            if i.id == self.my_id:
                self.resurce = i.resource
                break

        # формируем списки
        self.builders = find_ent_type(player_vive.entities, [EntityType.BUILDER_UNIT], self.my_id)
        self.soldiers = find_ent_type(player_vive.entities, [EntityType.RANGED_UNIT, EntityType.MELEE_UNIT], self.my_id)
        self.houses = find_house(player_vive.entities, self.my_id, self.ent_config)

        # Определение еды
        eat_max = 0
        for hous in self.houses:
            eat_max += self.ent_config[hous.entity_type].population_provide

        self.eat = (len(self.soldiers) + len(self.builders), eat_max)
        self.map.get_entities(player_vive.entities)


class MapScan:

    def __init__(self):
        self.map = []
        for i in range(code_war_wuliw.MAP_SIZE):
            self.map.append([])
            for j in range(code_war_wuliw.MAP_SIZE):
                self.map[i].append(0)

    def get_entities(self, entities, Entity_Properties):
        for ent in entities:
            if ent.entity_type == EntityType.RESOURCE \
                    or ent.entity_type == EntityType.RANGED_UNIT \
                    or ent.entity_type == EntityType.BUILDER_UNIT:
                self.map_array[ent.position.y][ent.position.x] = 1
            else:
                size_house = Entity_Properties[ent.entity_type].size + 2
                for i in range(size_house):
                    for j in range(size_house):
                        self.map_array[ent.position.y + i - 1][ent.position.x + j - 1] = 1


