from model import *
from enum import IntEnum

class Mayor:

    def __init__(self, top_level):
        self.kol_unit = 0
        self.top = top_level

    def update(self, wiwe):
        self.to_list_find_bilder(wiwe.entities)
        self.kol_unit = len(self.builders)
        self.find_target()
        print(self.target)
        #print(self.houses)

    def to_list_find_bilder(self, ents):
        self.builders = [] #Списк строителя
        self.houses = [] #список построек

        self.name_list = []
        for i in ents:
            if i.player_id == self.top.id:
                if i.entity_type == EntityType.BUILDER_UNIT:
                    self.builders.append(i)
                if not self.top.Entity_Properties[i.entity_type].can_move:
                    self.houses.append(i)

    def find_target(self):
        self.target = []

        if self.top.need_eat:
            self.target.append(Target(Target_type.BUILDING,Vec2Int(30,30),1,None))


#Шиблон таргет
# тип работы - [постройка, ремонт]
# целевой таргет - VecInt
# количество юнитов
# Id цели если нужно

class Target:

    def __init__(self, type, vek, kol, id = None):
        self.type = type
        self.vek = vek
        self.need_unit = kol
        self.id = id

    def work(self):
        out = None
        if self.type == Target_type.BUILDING:
           out = EntityAction(
                move_action=MoveAction(Vec2Int(self.vek.x-1,self.vek.y), True, True),
                build_action=BuildAction(EntityType.HOUSE, self.vek),
                attack_action=None,
                repair_action=None
            )
        if self.type == Target_type.FIX:
            out = EntityAction(
                move_action=MoveAction(Vec2Int(self.vek.x+1, self.vek.y+1), True, True),
                build_action=None,
                attack_action=None,
                repair_action=RepairAction(self.id)
            )

        return out


class Target_type(IntEnum):
    BUILDING = 0
    FIX = 1
