
class Board:

    def __init__(self):
        self.value = []
        self.populatiun = 0


    def add_point(self,unit):
        self.value.append(unit)
        self.populatiun += 1