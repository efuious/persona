from system import control
from games import day as d

class day_info():
    def __init__(self,day_n,time_n):
        self.dayn = day_n
        self.timen = time_n
    def set_time(self,time_n):
        print('时间被设置为:',d.time_list[time_n])
        self.timen = time_n
    def set_day(self,day_n):
        print('日期被设置为:',day_n)
        self.dayn = day_n
    def time_pass(self):
        self.timen += 1
        if self.timen > d.time.get(d.t_nigt):
            self.day_pass()
            self.timen = d.time.get(d.t_morn)
        control.press()
    def day_pass(self):
        self.dayn += 1
        control.press()
    def get_day(self):
        return self.dayn
    def get_time(self):
        return self.timen
    def to_night(self):
        self.timen = d.time.get('night')

class newday():
    def __init__(self,today):
        self.td = today

    def daying(self):
        self.tdn = self.td.day.get_day()
        print('=====第',self.tdn,'日')
        while self.the_day():
            if self.the_day() and d.is_morning(self.td.day.get_time()):
                self.show_time(self.morning_event)
            elif self.the_day() and d.is_beforenoon(self.td.day.get_time()):
                self.show_time(self.beforenoon_event)
            elif self.the_day() and d.is_noon(self.td.day.get_time()):
                self.show_time(self.noon_event)
            elif self.the_day() and d.is_afternoon(self.td.day.get_time()):
                self.show_time(self.afternoon_event)
            elif self.the_day() and d.is_night(self.td.day.get_time()):
                self.show_time(self.night_event)
            else:
                self.td.day.day_pass()
    def show_time(self,event):
        print('---现在是：',d.time_list[self.td.day.get_time()])
        event()

    def the_day(self):
        if self.td.day.get_day() == self.tdn:
            return True
        return False

    def morning_event(self):
        pass
    def beforenoon_event(self):
        pass
    def noon_event(self):
        pass
    def afternoon_event(self):
        pass
    def night_event(self):
        pass
    def show(self):
        print(self.td)
