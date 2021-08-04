from model import *
from code_war_wuliw import TargetType


def end_target(target_list):
    for i in target_list:
        if i[3]:
            target_list.remove(i)


class Strategist:

    def __init__(self, earner, mayor, defender, attack, event):

        # сылки на исполнителей
        self.to_earner = earner
        self.to_mayor = mayor
        self.to_defender = defender
        self.to_attack = attack
        self.to_event = event
        # Внутрение тулзы стратега
        self.takt = 0
        self.targets = []
        # Вресенное представление таргета где масив
        # [тип работы, целевое количество, реальное количество, флаг завершения]

    def update(self):
        result = Action({})

        # задержка активации ивет лога так как на 0 тике он не нужен
        if self.takt == 0:
            self.to_event.first_config()
        else:
            # мы проверяем старые задачи
            self.to_event.update(target_list=self.targets)

        # тут большая часть с постановкой задач
        if self.takt == 0:
            self.targets.append([TargetType.HIRING_BUILDER, 5, 1, False])
        elif self.takt == 15:
            self.targets.append([TargetType.HIRING_RANGED, 5, 1, False])
        elif self.takt == 20:
            self.targets.append([TargetType.HIRING_BUILDER, 5, 1, False])
            self.targets.append([TargetType.BUILDING_HOUSE, 4, 0, False])
        elif self.takt == 150:
            self.targets.append([TargetType.HIRING_RANGED, 100, 0, False])

        # остановка задачи по починке
        if self.to_event.need_fix_houses:
            for i in self.to_event.need_fix_houses:
                # [тип задачи, целевой id, число выделеных рабочих, статус задачи]
                self.targets.append([TargetType.FIX_HOUSE, i.id, 3, False])


        # Мирная часть
        self.to_mayor.update(self.targets, result)
        self.to_earner.update(self.targets, result)
        # Боевая часть
        self.to_defender.update(self.targets, result)
        self.to_attack.update(self.targets, result)

        self.takt += 1
        end_target(self.targets)

        return result
