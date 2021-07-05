
class Mind:

    def __init__(self,id):
        self.id = id
        self.name_list = []


    def chek_unit(self,ent_s):
        old_unit = []
        new_unit = []

        for ent in ent_s:
            if ent.player_id == self.id:
                if ent.id in self.name_list:
                    old_unit.append(ent)
                else:
                    new_unit.append(ent)
                    self.name_list.append(ent.id)

        return old_unit, new_unit


