from games import coop
from coops import topcoop as tp
from games import day
from system import guide
from games import person as p

"""
0: first sight
1: 1w
6: 3w
10: 6w, get coop
"""


class coop_p(tp.cp_event):
    coop_level = 0
    def event_level_0(self):
        if coop_p.coop_level == 0:
            self.front_event()
            coop_p.coop_level = self.player.coops[self.cpn]
            return
        elif coop_p.coop_level == 1:
            self.second_event()
            coop_p.coop_level = self.player.coops[self.cpn]
            return
        elif coop_p.coop_level == 4:
            self.third_event()
            coop_p.coop_level = self.player.coops[self.cpn]
        if coop_p.coop_level == 10:
            self.get_coop()
            coop_p.coop_level = self.player.coops[self.cpn]
    def event_level_1(self):
        print('和灵梦一起度过了愉快的时间 1')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_2(self):
        print('和灵梦一起度过了愉快的时间 2')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_3(self):
        print('和灵梦一起度过了愉快的时间 3')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_4(self):
        print('和灵梦一起度过了愉快的时间 4')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_5(self):
        print('和灵梦一起度过了愉快的时间 5')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_6(self):
        print('和灵梦一起度过了愉快的时间 6')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_7(self):
        print('和灵梦一起度过了愉快的时间 7')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_8(self):
        print('和灵梦一起度过了愉快的时间 8')
        self.player.coop_plus(coop.cpn.star,10)

    def event_level_9(self):
        print('和灵梦一起度过了愉快的时间 9')
        self.player.coop_plus(coop.cpn.star,10)

    def front_event(self):
        guide.star_event_1_guide()
        self.ask_money(10000)

    def second_event(self):
        guide.star_event_2_guide()
        self.ask_money(30000)

    def third_event(self):
        guide.star_event_3_guide()
        self.ask_money(60000)

    def get_coop(self):
        guide.star_get_coop_guide()

    def ask_money(self,num):
        while True:
            _input = int(input('1. 捐款, 2. 不捐款: '))
            if _input == 1:
                if self.player.status[p.property.money] >= num:
                    print('谢谢惠顾！')
                    self.player.status[p.property.money] -= num
                    self.player.coop_plus(self.cpn, num/10000)
                else:
                    print('开什么玩笑，你根本没这么多钱嘛')
                return
            elif _input == 2:
                print('什么嘛，新人真不友好')
                return
            else:
                pass


def coop_event(player):
    cpe = coop_p(coop.cpn.star,player)
    cpe.do_coop()

def special_day(td):
    #every night
    if td.day.get_time() > day.time.get(day.t_aftn):
        return True
    #Sunday
    elif td.day.get_day() % 7 == 0:
        print('参拜人数太多，灵梦很忙，还是别去打扰她了')
        return True
    return False

