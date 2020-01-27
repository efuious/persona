from games import coop
from coops import topcoop as tp

class coop_p(tp.cp_event):
    def event_level_0(self):
        print('do coop event: kappa 0')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_1(self):
        print('do coop event: kappa 1')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_2(self):
        print('do coop event: kappa 2')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_3(self):
        print('do coop event: kappa 3')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_4(self):
        print('do coop event: kappa 4')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_5(self):
        print('do coop event: kappa 5')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_6(self):
        print('do coop event: kappa 6')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_7(self):
        print('do coop event: kappa 7')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_8(self):
        print('do coop event: kappa 8')
        self.player.coop_plus(coop.cpn_kappa)

    def event_level_9(self):
        print('do coop event: kappa 9')
        self.player.coop_plus(coop.cpn_kappa)

def coop_event(player):
    cpe = coop_p(coop.cpn_kappa,player)
    cpe.do_coop()