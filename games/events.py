from system import control as sys
from games import person as p
from games import coop
from games import day

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
    if day.is_beforenoon(td.day.get_time()):
        print('晚上')
        td.day.to_night()
    else:
        print('时间流逝中...')
        td.day.time_pass()


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

def coop_reimu(td):
    # if td.day.get_time() > day.time.get(day.t_aftn):
    #     print('夜深了，一个人也没有')
    #     return
    print('看到了巫女')
    coop.coop_to(coop.cpn_reimu, td.player)
#    td.player.show_coop(coop.cpn_reimu)
    event_time_pass(td)

def coop_haruki(td):
    # week = td.day.get_day()%7
    # print(week)
    # if week not in (1,3,5):
    #     print('春树不在')
    #     return
    print('看到了春树')
    coop.coop_to(coop.cpn_haruki, td.player)
    event_time_pass(td)

def coop_erin(td):
    print('看到了永琳')
    coop.coop_to(coop.cpn_erin,td.player)
    event_time_pass(td)

def coop_shion(td):
    print('看到了紫苑')
    coop.coop_to(coop.cpn_shion,td.player)
    event_time_pass(td)

def coop_kappa(td):
    print('看到了河童')
    coop.coop_to(coop.cpn_kappa,td.player)
    event_time_pass(td)