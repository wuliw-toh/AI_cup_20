from model import *
from code_war_wuliw import TargetType

class Strategist:

    def __init__(self, earner, mayor, defender, attack, event):

        # сылки на исполнителей
        self.to_earner = earner
        self.to_mayor = mayor
        self.to_defender = defender
        self.to_attack = attack

        # Внутрение тулзы стратега
        self.targets = []
        # Вресенное представление таргета где масив [тип работы, целевое количество, реальное количество]
        self.targets.append([TargetType.HIRING_BUILDER, 10, 0])

    def update(self):
        result = Action({})
        # Мирная часть
        self.to_mayor.update(self.targets, result)
        self.to_earner.update(self.targets, result)
        # Боевая часть
        self.to_defender.update(self.targets, result)
        self.to_attack.update(self.targets, result)

        return result
