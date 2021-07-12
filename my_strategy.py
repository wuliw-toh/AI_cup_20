from model import *
from code_war_wuliw import *


class MyStrategy:
    def __init__(self):
        self.first_config = True
        #ВНИМАНИЕ НЕ ДИНАМИЧНЫЙ ID
        self.mind = Mind(1)

    def get_action(self, player_view, debug_interface):
        #Как то переделать в будующем
        if self.first_config:
            self.mind.Entity_Properties = player_view.entity_properties
            self.first_config = False
        out = self.mind.updata(player_view)
        return out


    def debug_update(self, player_view, debug_interface):
        debug_interface.send(DebugCommand.Clear())
        debug_interface.get_state()