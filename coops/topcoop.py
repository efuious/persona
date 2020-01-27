from games import coop

class cp_event():
    def __init__(self,cpn,player):
        self.player = player
        self.cpn = cpn
        self.event_level = [0]*coop.max_coop_level
        self.event_level[0] = self.event_level_0
        self.event_level[1] = self.event_level_1
        self.event_level[2] = self.event_level_2
        self.event_level[3] = self.event_level_3
        self.event_level[4] = self.event_level_4
        self.event_level[5] = self.event_level_5
        self.event_level[6] = self.event_level_6
        self.event_level[7] = self.event_level_7
        self.event_level[8] = self.event_level_8
        self.event_level[9] = self.event_level_9
    def do_coop(self):
        self.event_level[self.player.coops[self.cpn]]()
    def event_level_0(self):
        pass
    def event_level_1(self):
        pass
    def event_level_2(self):
        pass
    def event_level_3(self):
        pass
    def event_level_4(self):
        pass
    def event_level_5(self):
        pass
    def event_level_6(self):
        pass
    def event_level_7(self):
        pass
    def event_level_8(self):
        pass
    def event_level_9(self):
        pass
    def show(self):
        return self.player
