
class Target:

    def __init__(self, protokol, id):
        self.active = True
        self.protokol = protokol
        self.point_real = 0
        self.id_squad_work = id

    def set_squad(self,id):
        self.id_squad_work = id

    def get_active(self):
        pass