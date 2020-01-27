from games import coop
from coops import topcoop as tp

class coop_p(tp.cp_event):
    def event_level_0(self):
        print('认识了巫女：灵梦')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_1(self):
        print('do coop event: reimu 1')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_2(self):
        print('do coop event: reimu 2')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_3(self):
        print('do coop event: reimu 3')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_4(self):
        print('do coop event: reimu 4')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_5(self):
        print('do coop event: reimu 5')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_6(self):
        print('do coop event: reimu 6')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_7(self):
        print('do coop event: reimu 7')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_8(self):
        print('do coop event: reimu 8')
        self.player.coop_plus(coop.cpn_reimu)

    def event_level_9(self):
        print('do coop event: reimu 9')
        self.player.coop_plus(coop.cpn_reimu)

def coop_event(player):
    cpe = coop_p(coop.cpn_reimu,player)
    cpe.do_coop()