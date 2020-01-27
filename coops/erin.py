from games import coop
from coops import topcoop as tp

class coop_p(tp.cp_event):
    def event_level_0(self):
        print('do coop event: erin 0')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_1(self):
        print('do coop event: erin 1')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_2(self):
        print('do coop event: erin 2')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_3(self):
        print('do coop event: erin 3')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_4(self):
        print('do coop event: erin 4')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_5(self):
        print('do coop event: erin 5')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_6(self):
        print('do coop event: erin 6')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_7(self):
        print('do coop event: erin 7')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_8(self):
        print('do coop event: erin 8')
        self.player.coop_plus(coop.cpn_erin)

    def event_level_9(self):
        print('do coop event: erin 9')
        self.player.coop_plus(coop.cpn_erin)

def coop_event(player):
    cpe = coop_p(coop.cpn_erin,player)
    cpe.do_coop()