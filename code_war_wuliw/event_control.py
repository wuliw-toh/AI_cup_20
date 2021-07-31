import copy
from code_war_wuliw.target_type import TargetType


class EventControl:

    def __init__(self, to_link):
        self.lib = to_link
        # внутренние списки
        self.new_builders = []
        self.dead_builders = []

        self.new_houses = []
        self.dead_houses = []

        self.need_fix_houses = []

    def first_config(self):
        self.old_lib = copy.deepcopy(self.lib)

    def update(self, target_list):
        self.check_builder()
        self.check_houses()
        self.check_fix()

        for target in target_list:
            if target[0] == TargetType.HIRING_BUILDER:
                self.hiring_builder(target)


        self.old_lib = copy.deepcopy(self.lib)

    def check_builder(self):
        """Формируем два списка нанятых строителей и убитых строителей"""
        n_set = set([x.id for x in self.lib.builders])
        o_set = set([x.id for x in self.old_lib.builders])

        self.new_builders = []
        self.dead_builders = []

        new_chek = n_set - o_set
        if new_chek:
            for i in new_chek:
                for bl in self.lib.builders:
                    if bl.id == i:
                        self.new_builders.append(bl)

        dead_chek = o_set - n_set
        if dead_chek:
            for i in dead_chek:
                for bl in self.old_lib.builders:
                    if bl.id == i:
                        self.dead_builders.append(bl)

    def check_houses(self):
        self.new_houses = []
        self.dead_houses = []

        n_set = set([x.id for x in self.lib.houses])
        o_set = set([x.id for x in self.old_lib.houses])

        new_chek = n_set - o_set
        if new_chek:
            for i in new_chek:
                for bl in self.lib.houses:
                    if bl.id == i:
                        self.new_houses.append(bl)

        dead_chek = o_set - n_set
        if dead_chek:
            for i in dead_chek:
                for bl in self.old_lib.houses:
                    if bl.id == i:
                        self.dead_houses.append(bl)

    def check_fix(self):
        self.need_fix_houses = []
        for i in self.lib.houses:
            if i.health < self.lib.ent_config[i.entity_type].max_health:
                self.need_fix_houses.append(i)

    def hiring_builder(self, target):
        # увеличиваем число юнитов
        target[2] += len(self.new_builders)
        # проверяем условие завершения задачи
        target[3] = target[1] == target[2]
