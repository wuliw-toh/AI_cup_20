
class Mind:

    def __init__(self,id):
        self.id = id
        self.resurse = 0
        self.name_list = []
        #==================================
        self.Entity_Properties = None

        #==================================
        self.building = []
        self.units = []

    def updata(self,pleer_wiew):
        #определили ресус
        for pl in pleer_wiew.players:
            if pl.id == self.id:
                self.resurse = pl.resource

        #Нашли новых юнитов
        old_ent, new_ent = self.chek_unit(pleer_wiew.entities)
        #Распределили по списками
        self.to_list(new_ent)
        

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

    def to_list(self,new_ent):
        for i in new_ent:
            properties = self.Entity_Properties[i.entity_type]
            if properties.can_move:
                self.units.append(i)
            else:
                self.building.append(i)

