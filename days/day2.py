from days import topday
from games import events as event
from games import map

class today(topday.newday):
    def morning_event(self):
        event.morning(self.td)
        print('施工中，设定学校放假')
        self.td.player.refresh()
    def beforenoon_event(self):
        map.move(self.td)
    def noon_event(self):
        map.move(self.td)
    def afternoon_event(self):
        map.move(self.td)
    def night_event(self):
        map.move(self.td)

def day2(td):
    d2 = today(td)
    d2.daying()