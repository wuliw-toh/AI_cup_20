from model import *

class Mayor:

    def __init__(self, top_level):
        self.kol_unit = 0
        self.top = top_level

    def update(self, wiwe):
        self.to_list_find_bilder(wiwe.entities)
        self.kol_unit = len(self.builders)
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




    