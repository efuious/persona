import system as sys
import person as p
import coop

import events as event
import map
def the_day(tdn,day):
    if day == tdn:
        return True
    return False

def today(td):
    tdn = td.day.get_day()
    while the_day(tdn,td.day.get_day()):
        if the_day(tdn,td.day.get_day()) and sys.is_morning(td.day.get_time()):
            morning_event(td)
        elif the_day(tdn,td.day.get_day()) and sys.is_beforenoon(td.day.get_time()):
            beforenoon_event(td)
        elif the_day(tdn,td.day.get_day()) and sys.is_noon(td.day.get_time()):
            noon_event(td)
        elif the_day(tdn,td.day.get_day()) and sys.is_afternoon(td.day.get_time()):
            afternoon_event(td)
        elif the_day(tdn,td.day.get_day()) and sys.is_night(td.day.get_time()):
            night_event(td)
        else:
            td.day.day_pass()

def morning_event(td):
    print('早上')
    print('今天是转学过来的第一天，决定早点去学校')
    td.day.time_pass()

def beforenoon_event(td):
    print('上午')
    print('老师：今天转学过来一位新同学：',td.player.status[p.name])
    print('介绍完了开始上课')
    td.day.time_pass()

def noon_event(td):
    print('同学过来搭话了')
    coop.coop_to(coop.cpn_haruki,td.player)
    td.day.time_pass()

def afternoon_event(td):
    print('放学了...')
    map.school(td)

def night_event(td):
    td.player.show_konwn_coop()
    td.day.day_pass()