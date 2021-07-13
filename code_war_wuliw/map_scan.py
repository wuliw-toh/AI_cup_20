from model import *


class Map_scan:

    map_array = None

    def __init__(self):
        self.first_config = True
        #self.Map = np.array(12,int)

    def update(self,wiew):
        if self.first_config:
            self.first_config = False
            self.Entity_Properties = wiew.entity_properties

        mx, my = self.find_size(wiew.entities)

        self.creature_2d_list(mx+1, my+1)#потестить надо ли тут +1
        self.fill_map(wiew.entities)

    def find_size(self, ent_m):
        max_x = 0
        max_y = 0
        for i in ent_m:
            if i.position.x > max_x: max_x = i.position.x
            if i.position.y > max_y: max_y = i.position.y

        return max_x,max_y

    def creature_2d_list(self,x_max, y_max):
        self.map_array = []
        for i in range(y_max):
            self.map_array.append([])
            for j in range(x_max):
                self.map_array[i].append(0)

    def fill_map(self, ent_m):
        for ent in ent_m:

            if ent.entity_type == EntityType.RESOURCE\
                    or ent.entity_type == EntityType.RANGED_UNIT\
                    or ent.entity_type == EntityType.BUILDER_UNIT:
                self.map_array[ent.position.y][ent.position.x] = 1
            else:
                size_house = self.Entity_Properties[ent.entity_type].size + 2
                for i in range(size_house):
                    for j in range(size_house):
                        self.map_array[ent.position.y + i - 1][ent.position.x + j - 1] = 1

    def sum_list(self,value):
        out = 0
        for i in value:
            out += sum(i)
        return out

    def win_list(self, dx, dy, size):
        out = self.map_array[dy:dy+size]
        for i in range(len(out)):
            out[i] = out[i][dx:dx+size]
        return out

    def find_pos(self, type, unit_pos):
        mas = []

        win_size = self.Entity_Properties[type].size
        for i in range(len(self.map_array) - win_size):
            for j in range(len(self.map_array[0]) - win_size):
                if self.sum_list(self.win_list(i, j, win_size)) == 0:
                    mas.append(Vec2Int(i, j))

        if mas:
            min = 500
            for i in mas:
                if min > self.dlinna(unit_pos,i):
                    min = self.dlinna(unit_pos,i)
                    out = i
        else:
            out = Vec2Int(0, 0)

        return out

    def dlinna(self, vek1, vek2):
        return  abs(vek1.x - vek2.x) + abs(vek1.y - vek2.y)