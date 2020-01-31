from games import person as p
from games import coop
from days import day
from system import control


def event_time_pass(td):
    if day.is_beforenoon(td.day.get_time()):
        td.day.to_night()
    else:
        td.day.time_pass()

def study(td):
    if td.day.get_day() == 0:
        print('今天没必要学习')
        return
    if td.player.status[p.s_status] == 0:
        print('今天很疲惫，没能学进去')
    elif td.player.status[p.s_status] == 1:
        print('今天好好学习了，知识 + 1')
        td.player.status[p.s_knowledge] += 1
    elif td.player.status[p.s_status] == 2:
        print('今天学习状态特别好，知识 + 2')
        td.player.status[p.s_knowledge] += 2
    event_time_pass(td)

def sleep(td):
    if td.day.get_time() < day.time.get('night'):
        print('现在还早，不用睡觉')
        return
    elif day.is_night(td.day.get_time()):
        print('今天没什么事，就睡了吧')
        td.player.status[p.s_status] += 2
        if td.player.status[p.s_status] > 2:
            td.player.status[p.s_status] = 2
        print('因为有好好休息，状态上升：',td.player.status[p.s_status])
    else:
        td.player.status[p.s_status] += 1
        if td.player.status[p.s_status] > 2:
            td.player.status[p.s_status] = 2
    td.day.day_pass()

def moring(td):
    print('今天是:',td.day.get_day())
    if day.is_weekend(td.day.get_day()):
        print('今天是周末')
    else:
        print('今天是工作日')
    td.day.time_pass()

# def coop_star(td):
#     # if td.day.get_time() > day.time.get(day.t_aftn):
#     #     print('夜深了，一个人也没有')
#     #     return
#     print('看到了',coop.name_list[coop.cpn_star])
#     coop.coop_to(coop.cpn_star, td.player)
# #    td.player.show_coop(coop.cpn_star)
#     event_time_pass(td)
#
# def coop_chariot(td):
#     if coop.special_day(coop.cpn_chariot,td):
#         return
#     print('看到了',coop.name_list[coop.cpn_chariot])
#     coop.coop_to(coop.cpn_chariot, td.player)
#     event_time_pass(td)
#
# def coop_death(td):
#     if coop.special_day(coop.cpn_death,td):
#         return
#     print('看到了',coop.name_list[coop.cpn_death])
#     coop.coop_to(coop.cpn_death,td.player)
#     event_time_pass(td)
#
# def coop_temperance(td):
#     if coop.special_day(coop.cpn_temperance,td):
#         return
#     print('看到了',coop.name_list[coop.cpn_temperance])
#     coop.coop_to(coop.cpn_temperance,td.player)
#     event_time_pass(td)
#
# def coop_hangedman(td):
#     if coop.special_day(coop.cpn_hangedman,td):
#         return
#     print('看到了',coop.name_list[coop.cpn_hangedman])
#     coop.coop_to(coop.cpn_hangedman,td.player)
#     event_time_pass(td)

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
    td.player.status_plus(p.s_brave)
    print('勇气增加了')
    event_time_pass(td)
    control.press()

def worship(td):
    print('诚心拜神了')
    td.player.status_plus(p.s_spirit)
    event_time_pass(td)
    control.press()

def libaray(td):
    print('好好学习了')
    td.player.status_plus(p.s_knowledge)
    td.player.status_plus(p.s_potential)
    event_time_pass(td)
    control.press()

def show_data(td):
    print('获得的coop:')
    td.player.show_konwn_coop()
    control.press()
    print('身体状态：')
    td.player.show_all_status()
    control.press()