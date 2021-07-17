from model import *

class Mayor:

    def __init__(self, top_level):
        self.kol_unit = 0
        self.top = top_level
        self.name_list = []

    def update(self, wiwe):
        self.to_list_find_bilder(wiwe.entities)
        self.kol_unit = len(self.builders)
        print(self.kol_unit)

    def to_list_find_bilder(self, ents):
        self.builders = []
        for i in ents:
            if i.player_id == self.top.id:
                if i.entity_type == EntityType.BUILDER_UNIT:
                    self.builders.append(i)


    