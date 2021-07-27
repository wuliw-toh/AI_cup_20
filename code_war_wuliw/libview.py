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
        #Обновление карты
        self.map.get_entities(player_vive.entities, self.ent_config)

    def remove_builders(self, remove_ent):
        """
        Функция удалаяет из списка строителей переданные сущьности.
        В процессе обработки часть строителей будет заняты.
        """
        for ent in remove_ent:
            self.builders.remove(ent)


class MapScan:

    def __init__(self):
        self.map = []

    def get_entities(self, entities, ent_config):
        self.new_mas()
        for ent in entities:
            if ent.entity_type == EntityType.RESOURCE \
                    or ent.entity_type == EntityType.RANGED_UNIT \
                    or ent.entity_type == EntityType.BUILDER_UNIT \
                    or ent.entity_type == EntityType.MELEE_UNIT:
                self.map[ent.position.x][ent.position.y] = int(ent.entity_type)
            else:
                size_house = ent_config[ent.entity_type].size
                for i in range(size_house):
                    for j in range(size_house):
                        self.map[ent.position.x + i][ent.position.y + j] = int(ent.entity_type)

    def new_mas(self):
        self.map.clear()
        for i in range(code_war_wuliw.MAP_SIZE):
            self.map.append([x for x in range(code_war_wuliw.MAP_SIZE)])

