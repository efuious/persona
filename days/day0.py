import system as sys
import map
import events as event

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
    print('今天开始就在这里生活了，先跟大家打个招呼吧')
    print('打招呼中。。。')
    print('打完招呼了，去熟悉一下这边的环境吧')
    td.day.time_pass()

def beforenoon_event(td):
    print('上午')
    map.house(td)

def noon_event(td):
    print('中午')
    td.day.time_pass()

def afternoon_event(td):
    print('下午')
    map.house(td)

def night_event(td):
    print('晚上')
    print('今天很累了，就先休息吧')
    event.sleep(td)
