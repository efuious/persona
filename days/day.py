import system.control as sys

t_morn = 'morning'
t_aftn = 'afternoon'
t_noon = 'noon'
t_befn = 'before noon'
t_nigt = 'night'

time_list = [t_morn,t_befn,t_noon,t_aftn,t_nigt]
ntime = len(time_list)
time = {name:num for name,num in zip(time_list,range(ntime))}

def is_weekend(day):
    if day%6 == 0 or day%7 == 0:
        return True
    return False

def is_morning(time_n):
    if time_n == time.get(t_morn):
        return True
    return False

def is_beforenoon(time_n):
    if time_n == time.get(t_befn):
        return True
    return False

def is_noon(time_n):
    if time_n == time.get(t_noon):
        return True
    return False

def is_afternoon(time_n):
    if time_n == time.get(t_aftn):
        return True
    return False

def is_night(time_n):
    if time_n == time.get(t_nigt):
        return True
    return False

class day_info():
    def __init__(self,day_n,time_n):
        self.dayn = day_n
        self.timen = time_n
    def set_time(self,time_n):
        print('时间被设置为:',time_list[time_n])
        self.timen = time_n
    def set_day(self,day_n):
        print('日期被设置为:',day_n)
        self.dayn = day_n
    def time_pass(self):
        self.timen += 1
        if self.timen > time.get(t_nigt):
            self.day_pass()
            self.timen = time.get(t_morn)
        print('时间到了:', time_list[self.timen])
        sys.press()
    def day_pass(self):
        self.dayn += 1
        print('日期到了:', self.dayn)
        sys.press()
    def get_day(self):
        return self.dayn
    def get_time(self):
        return self.timen
    def to_night(self):
        self.timen = time.get('night')

class day():
    def __init__(self,today):
        self.td = today

    def daying(self):
        self.tdn = self.td.day.get_day()
        print('今天是',self.tdn,'日')
        while self.the_day():
            if self.the_day() and is_morning(self.td.day.get_time()):
                self.morning_event()
            elif self.the_day() and is_beforenoon(self.td.day.get_time()):
                self.beforenoon_event()
            elif self.the_day() and is_noon(self.td.day.get_time()):
                self.noon_event()
            elif self.the_day() and is_afternoon(self.td.day.get_time()):
                self.afternoon_event()
            elif self.the_day() and is_night(self.td.day.get_time()):
                self.night_event()
            else:
                self.td.day.day_pass()

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
