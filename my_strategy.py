from model import *
from code_war_wuliw import *

class MyStrategy:

    def __init__(self):
        self.lib = LibView()
        self.earner = Earner(self.lib)
        self.mayor = Mayor(self.lib)
        self.defender = Defender(self.lib)
        self.attack = Attack(self.lib)

        self.strateg = Strategist(
            earner=self.earner,
            mayor=self.mayor,
            defender=self.defender,
            attack=self.attack
        )

    def get_action(self, player_view, debug_interface):
        # мои тулзы
        self.lib.update(player_view)
        return self.strateg.update()

    def debug_update(self, player_view, debug_interface):
        pass