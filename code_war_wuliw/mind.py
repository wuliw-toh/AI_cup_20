from model import *
from code_war_wuliw import map_scan
from code_war_wuliw import Mayor

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
        self.Map = map_scan.Map_scan()
        #==================================
        self.building = []
        self.units = []
        self.need_barak = True
        #==========================================
        self.mayor = Mayor(self)

    def update(self,pleer_wiew):
        self.event_cheak(pleer_wiew)
        if self.need_eat:
            self.Map.update(pleer_wiew)
        #self.debag_print()
        self.mayor.update(pleer_wiew)
        out = self.resurse_craft()



        return out

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

    def event_cheak(self, pleer_wiew):
        #определили ресус
        for pl in pleer_wiew.players:
            if pl.id == self.id:
                self.resurse = pl.resource

        #проверка порога ресурса
        if self.resurse > 600:
            self.a_lot_of_res = True
        else:
            self.a_lot_of_res = False


        #проверка на наличие еды

        my_point = []
        self.building = []
        self.units = []

        for i in pleer_wiew.entities:
            if i.player_id == self.id:
                my_point.append(i)

        self.to_list(my_point)


        self.eat_work()
        if self.max_eat == self.real_eat:
            self.need_eat = True
        else:
            self.need_eat = False



        #проверка на наличие порушеннах зданий
        # НЕ ОБНОВЛЯЕТЬСЯ СПИСКИ!!!!
        self.need_fix = False
        for i in self.building:
            properties = self.Entity_Properties[i.entity_type]
            if properties.max_health > i.health:
                self.need_fix = True

    def resurse_craft(self):
        result = Action({})
        kost_fix = 0
        kost_war = True
        kost = 0

        for unit in self.units:
            move_act = MoveAction(Vec2Int(70, 70), True, True)
            build_act = None
            attack_act = AttackAction(None, AutoAttack(200, [EntityType.RESOURCE]))
            fix_act = None

            if self.need_eat:
                if len(self.units) > 10:
                    if kost == 3:
                        self.need_eat = False
                    else:
                        kost +=1
                else:
                    self.need_eat = False


                vek_act = self.Map.find_pos(EntityType.HOUSE, unit.position)
                #vek_act = self.Map.find_pos(EntityType.HOUSE, Vec2Int(5, 5))
                vek_stop = Vec2Int(vek_act.x + 1, vek_act.y)

                move_act = MoveAction(vek_stop, True, True)
                build_act = BuildAction(EntityType.HOUSE, vek_act)
                attack_act = None

            if self.need_fix:
                target = None
                for i in self.building:
                    properties = self.Entity_Properties[i.entity_type]
                    if properties.max_health > i.health:
                        target = i
                        break
                if kost_fix < 10:
                    # move_act = MoveAction(target.position,True,True)
                    move_act = MoveAction(Vec2Int(target.position.x + 1, target.position.y + 1), True, True)
                    fix_act = RepairAction(target.id)
                    attack_act = None
                    kost_fix += 1

            if len(self.units) >= 40:
                if self.need_barak:
                    self.need_barak = False
                    vek_act = self.Map.find_pos(EntityType.RANGED_BASE, unit.position)
                    vek_stop = Vec2Int(vek_act.x + 1, vek_act.y)

                    move_act = MoveAction(vek_stop, True, True)
                    build_act = BuildAction(EntityType.RANGED_BASE, vek_act)
                    attack_act = None



            result.entity_actions[unit.id] = EntityAction(
                move_action=move_act,
                build_action=build_act,
                attack_action=attack_act,
                repair_action=fix_act
            )

        for house in self.building:
            # Внимание работает только на главном здании.
            # Просто по кд строит рабочих
            if len(self.units) < 300:
                build_act = BuildAction(EntityType.BUILDER_UNIT,
                                        Vec2Int(house.position.x + 5,
                                                house.position.y + 5 - 1))
            else:
                build_act = BuildAction(EntityType.RANGED_UNIT,
                                        Vec2Int(house.position.x + 5,
                                                house.position.y + 5 - 1))

            result.entity_actions[house.id] = EntityAction(
                move_action=None,
                build_action=build_act,
                attack_action=None,
                repair_action=None
            )

        return result


    def debag_print(self):
        print("\n")
        print("Ресурс - ", self.resurse)
        print("Количество юнитов - ", len(self.units))
        print("Количество зданий - ", len(self.building))
        print("Макс еда - ", self.max_eat)
        print("Реал еда - ", self.real_eat)
        print("Надо чинить - ", self.need_fix)

        #отладка постройки
        if self.need_fix:
            print(self.building[1])