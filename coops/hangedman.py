from games import coop
from coops import topcoop as tp
#from days import day

class coop_p(tp.cp_event):
    def event_level_0(self):
        print('认识了修理工河童')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_1(self):
        print('与河童一起度过了愉快的时间 1')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_2(self):
        print('与河童一起度过了愉快的时间 2')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_3(self):
        print('与河童一起度过了愉快的时间 3')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_4(self):
        print('与河童一起度过了愉快的时间 4')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_5(self):
        print('与河童一起度过了愉快的时间 5')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_6(self):
        print('与河童一起度过了愉快的时间 6')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_7(self):
        print('与河童一起度过了愉快的时间 7')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_8(self):
        print('与河童一起度过了愉快的时间 8')
        self.player.coop_plus(coop.cpn.hangedman,10)

    def event_level_9(self):
        print('与河童一起度过了愉快的时间 9')
        self.player.coop_plus(coop.cpn.hangedman,10)

def coop_event(player):
    cpe = coop_p(coop.cpn.hangedman,player)
    cpe.do_coop()

def special_day(td):
    return False