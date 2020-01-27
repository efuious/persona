from games import coop
from coops import topcoop as tp

class coop_p(tp.cp_event):
    def event_level_0(self):
        print('do coop event: shion 0')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_1(self):
        print('do coop event: shion 1')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_2(self):
        print('do coop event: shion 2')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_3(self):
        print('do coop event: shion 3')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_4(self):
        print('do coop event: shion 4')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_5(self):
        print('do coop event: shion 5')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_6(self):
        print('do coop event: shion 6')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_7(self):
        print('do coop event: shion 7')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_8(self):
        print('do coop event: shion 8')
        self.player.coop_plus(coop.cpn_shion)

    def event_level_9(self):
        print('do coop event: shion 9')
        self.player.coop_plus(coop.cpn_shion)

def coop_event(player):
    cpe = coop_p(coop.cpn_shion,player)
    cpe.do_coop()