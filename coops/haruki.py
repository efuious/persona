from games import coop
from coops import topcoop as tp

class coop_p(tp.cp_event):
    def event_level_0(self):
        print('认识了同学：春树')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_1(self):
        print('和春树一起度过了愉快的时间')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_2(self):
        print('do coop event: haruki 2')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_3(self):
        print('do coop event: haruki 3')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_4(self):
        print('do coop event: haruki 4')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_5(self):
        print('do coop event: haruki 5')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_6(self):
        print('do coop event: haruki 6')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_7(self):
        print('do coop event: haruki 7')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_8(self):
        print('do coop event: haruki 8')
        self.player.coop_plus(coop.cpn_haruki)
    
    def event_level_9(self):
        print('do coop event: haruki 9')
        self.player.coop_plus(coop.cpn_haruki)

def coop_event(player):
    cpe = coop_p(coop.cpn_haruki,player)
    cpe.do_coop()