from days import topday
from games import map

class today(topday.newday):
    def morning_event(self):
        print('今天开始就在这里生活了，先跟大家打个招呼吧')
        print('打招呼中。。。')
        print('打完招呼了，去熟悉一下这边的环境吧')
        self.td.day.time_pass()

    def beforenoon_event(self):
        map.house(self.td)

    def noon_event(self):
        map.house(self.td)

    def afternoon_event(self):
        map.house(self.td)

    def night_event(self):
        map.house(self.td)

def theday(td):
    d0 = today(td)
    d0.daying()
