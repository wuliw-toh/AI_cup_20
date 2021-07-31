import copy


class EventControl:

    def __init__(self, to_link):
        self.lib = to_link

    def first_config(self):
        self.old_lib = copy.deepcopy(self.lib)

    def update(self, target_list=None):
        print(set([x.id for x in self.lib.builders]) - set([x.id for x in self.old_lib.builders]))
        #print([x.id for x in self.lib.builders])
        #print(self.old_lib.builders)

        self.old_lib = copy.deepcopy(self.lib)


