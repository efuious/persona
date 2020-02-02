from days import *
ndays = 3

day_list = [0]*ndays
day_list[0] = day0.theday
day_list[1] = day1.day1
day_list[2] = day2.day2


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

def show_day(td):
    day_list[td.day.get_day()](td)
