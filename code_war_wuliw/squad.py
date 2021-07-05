from model import *

MAX_PIOPLE = 5

class Squad:

    def __init__(self,id,pos,tupe):
        self.id = id
        self.position = pos
        self.population = 0
        self.reception = True
        self.entities = []

        #----------------------------------------
        self.result = Action({})

    def go_to_point(self,target):
        for ent in self.entities:
            move_action = MoveAction(
                Vec2Int(player_view.map_size - 1,
                        player_view.map_size - 1),
                True,
                True)

            self.result.entity_actions[ent.id] = EntityAction(
                move_action,
                None,
                None,
                None
            )

    def add_unit(self,ent):
        if self.reception:
            self.entities.append(ent)
            self.population += 1
            if self.population == MAX_PIOPLE:
                self.reception = False

