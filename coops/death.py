from games import coop
from coops import topcoop as tp

class coop_p(tp.cp_event):
    def event_level_0(self):
        print('do coop event: death 0')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_1(self):
        print('do coop event: death 1')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_2(self):
        print('do coop event: death 2')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_3(self):
        print('do coop event: death 3')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_4(self):
        print('do coop event: death 4')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_5(self):
        print('do coop event: death 5')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_6(self):
        print('do coop event: death 6')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_7(self):
        print('do coop event: death 7')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_8(self):
        print('do coop event: death 8')
        self.player.coop_plus(coop.cpn.death,10)

    def event_level_9(self):
        print('do coop event: death 9')
        self.player.coop_plus(coop.cpn.death,10)

def coop_event(player):
    cpe = coop_p(coop.cpn.death,player)
    cpe.do_coop()

def special_day(td):
    return False
