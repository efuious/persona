import os

max_time = 6

time_name = ['morning','beforenoon','noon','afternoon','night','deep night']
time = {name:num for name,num in zip(time_name,range(max_time))}

def press():
    _input = input('press a button')
    return 0

def clrscr():
    os.system('cls')

def is_weekend(day):
    if day%6 == 0 or day%7 == 0:
        return True
    return False

def is_morning(time_n):
    if time_n == time.get('morning'):
        return True
    return False

def is_beforenoon(time_n):
    if time_n == time.get('beforenoon'):
        return True
    return False

def is_noon(time_n):
    if time_n == time.get('noon'):
        return True
    return False

def is_afternoon(time_n):
    if time_n == time.get('afternoon'):
        return True
    return False

def is_night(time_n):
    if time_n == time.get('night'):
        return True
    return False

class day_info():
    def __init__(self,day_n,time_n):
        self.dayn = day_n
        self.timen = time_n
    def set_time(self,time_n):
        print('time has set to:',time_name[time_n])
        self.timen = time_n
    def set_day(self,day_n):
        print('today has set to:',day_n)
        self.dayn = day_n
    def time_pass(self):
        self.timen += 1
        if self.timen >= time.get('deep night'):
            self.day_pass()
            self.timen = 0
        print('time passed to:', time_name[self.timen])
        press()
    def day_pass(self):
        self.dayn += 1
        self.timen = 0
        print('day passed to:', self.dayn)
        press()
    def get_day(self):
        return self.dayn
    def get_time(self):
        return self.timen
    def to_night(self):
        self.timen = time.get('night')

if __name__ == '__main__':
    if is_morning(time.get('morning')):
        print('morning')
    if is_beforenoon(time.get('beforenoon')):
        print('before noon')
    if is_noon(time.get('noon')):
        print('noon')
    if is_afternoon(time.get('afternoon')):
        print('afternoon')
    if is_night(time.get('night')):
        print('night')