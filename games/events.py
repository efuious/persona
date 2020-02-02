from games import person as p
from games import coop
from games import day
from system import control

thisday = -1

def event_time_pass(td):
    if day.is_beforenoon(td.day.get_time()):
        td.day.to_night()
    else:
        td.day.time_pass()
    control.press()

def study(td):
    if td.day.get_day() == 0:
        print('今天没必要学习')
        return
    if td.player.status[p.property.status] == 0:
        print('今天很疲惫，没能学进去')
    elif td.player.status[p.property.status] == 1:
        print('今天好好学习了，知识 + 1')
        td.player.status[p.property.knowledge] += 1
    elif td.player.status[p.property.status] == 2:
        print('今天学习状态特别好，知识 + 2')
        td.player.status[p.property.knowledge] += 2
    event_time_pass(td)

def sleep(td):
    if td.day.get_time() < day.time.get('night'):
        control.show_back('现在还早，不用睡觉')
        return
    elif day.is_night(td.day.get_time()):
        control.show_back('今天没什么事，就睡了吧')
        td.player.status[p.property.status] += 2
        if td.player.status[p.property.status] > 2:
            td.player.status[p.property.status] = 2
        control.show_back('因为有好好休息，状态上升')
    else:
        td.player.status[p.property.status] += 1
        if td.player.status[p.property.status] > 2:
            td.player.status[p.property.status] = 2
    td.day.day_pass()

def morning(td):
    if day.is_weekend(td.day.get_day()):
        print('今天是周末')
    else:
        print('今天是工作日')
    td.day.time_pass()

def coop_event(cpn,td):
    if coop.special_day(cpn,td):
        print(coop.name_list[cpn],'不在')
        control.press()
        return
    print('看到了',coop.name_list[cpn])
    coop.coop_to(cpn, td.player)
    event_time_pass(td)

def fast_food_challenge(td):
    print('进行了快餐店挑战')
    td.player.status_plus(p.property.brave)
    print('勇气增加了')
    event_time_pass(td)

def worship(td):
    global thisday
    if td.day.get_day() == thisday:
        control.show_back('今天已经拜过神了')
        return
    thisday = td.day.get_day()
    print('诚心拜神了')
    td.player.status_plus(p.property.spirit)
    event_time_pass(td)

def libaray(td):
    if day.is_weekend(td.day.get_day()):
        print('')
    control.show_back('好好学习了')
    td.player.status_plus(p.property.knowledge)
    td.player.status_plus(p.property.potential)
    event_time_pass(td)

def show_data(td):
    print('获得的coop:')
    td.player.show_konwn_coop()
    control.press()
    print('身体状态：')
    td.player.show_all_status()
    control.press()

def school_not_open(td):
    if day.is_weekend(td.day.get_day()):
        control.show_back('今天是周末，学校一个人都没有')
        return True
    elif day.is_night(td.day.get_time()):
        print('夜深了，学校一个人也没有')
        return True
    return False