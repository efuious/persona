from days import topday
from games import coop
from games import map
from games import person as p

class today(topday.newday):
    def morning_event(self):
        print('今天是转学过来的第一天，决定早点去学校')
        self.td.player.refresh()
        self.td.day.time_pass()
    def beforenoon_event(self):
        print('老师：今天转学过来一位新同学：',self.td.player.status[p.property.name])
        print('介绍完了开始上课')
        self.td.day.time_pass()
    def noon_event(self):
        print('同学过来搭话了')
        coop.coop_to(coop.cpn.chariot, self.td.player)
        self.td.day.time_pass()
    def afternoon_event(self):
        print('放学了...')
        map.school(self.td)
    def night_event(self):
        map.move(self.td)

def day1(td):
    d1 = today(td)
    d1.daying()