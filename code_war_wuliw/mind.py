
class Mind:
    #Временные тестовые переменные
    new_unit = False #появился новый юнит?
    a_lot_of_res = False #Проверяет порог ресурса
    need_eat = False #нужна еда
    need_fix = False #есть здания для починки


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

        #проверка порога ресурса
        if self.resurse > 600:
            self.a_lot_of_res = True
        else:
            self.a_lot_of_res = False

        #Нашли новых юнитов
        old_ent, new_ent = self.chek_unit(pleer_wiew.entities)

        #Проверка на появление юнита
        if new_ent:
            self.new_unit = True
            #распределение по спискам
            self.to_list(new_ent)
        else:
            self.new_unit = False

        #проверка на наличие еды
        self.eat_work()
        if self.max_eat == self.real_eat:
            self.need_eat = True
        else:
            self.need_eat = False

        #проверка на наличие порушеннах зданий
        for i in self.building:
            properties = self.Entity_Properties[i.entity_type]
            if properties.max_health > i.health:
                self.need_fix = True
            else:
                self.need_fix = False

        self.debag_print()

    def chek_unit(self, ent_s):
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

    def to_list(self, new_ent):
        for i in new_ent:
            properties = self.Entity_Properties[i.entity_type]
            if properties.can_move:
                self.units.append(i)
            else:
                self.building.append(i)

    def eat_work(self):
        self.max_eat = 0
        for i in self.building:
            properties = self.Entity_Properties[i.entity_type]
            self.max_eat += properties.population_provide

        self.real_eat = len(self.units)


    def debag_print(self):
        print("\n")
        print("Ресурс - ", self.resurse)
        print("Количество юнитов - ", len(self.units))
        print("Количество зданий - ", len(self.building))
        print("Макс еда - ", self.max_eat)
        print("Реал еда - ", self.real_eat)
        print("Надо чинить - ", self.need_fix)