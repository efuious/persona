import person as p
import system as sys
import coop

def event_time_pass(td):
    if sys.is_beforenoon(td.day.get_time()):
        td.day.to_night()
    else:
        td.day.time_pass()

def study(td):
    if td.day.get_day() == 0:
        print('今天没必要学习')
        return
    if td.player.status[p.status] == 0:
        print('今天很疲惫，没能学进去')
    elif td.player.status[p.status] == 1:
        print('今天好好学习了，知识 + 1')
        td.player.status[p.knowledge] += 1
    elif td.player.status[p.status] == 2:
        print('今天学习状态特别好，知识 + 2')
        td.player.status[p.knowledge] += 2
    if sys.is_beforenoon(td.day.get_time()):
        print('晚上')
        td.day.to_night()
    else:
        print('时间流逝中...')
        td.day.time_pass()


def sleep(td):
    if td.day.get_time() < sys.time.get('night'):
        print('现在还早，不用睡觉')
        return
    elif sys.is_night(td.day.get_time()):
        print('今天没什么事，就睡了吧')
        td.player.status[p.status] += 2
        if td.player.status[p.status] > 2:
            td.player.status[p.status] = 2
        print('因为有好好休息，状态上升：',td.player.status[p.status])
    else:
        td.player.status[p.status] += 1
        if td.player.status[p.status] > 2:
            td.player.status[p.status] = 2
    td.day.day_pass()

def moring(td):
    print('今天是:',td.day.get_day())
    if sys.is_weekend(td.day.get_day()):
        print('今天是周末')
    else:
        print('今天是工作日')
    td.day.time_pass()

def coop_reimu(td):
    if td.day.get_time() > sys.time.get('afternoon'):
        print('夜深了，一个人也没有')
        return
    print('看到了巫女')
    coop.coop_to(coop.cpn_reimu,td.player)
#    td.player.show_coop(coop.cpn_reimu)
    event_time_pass(td)

def coop_haruki(td):
    week = td.day.get_day()%7
    print(week)
    if week not in (1,3,5):
        print('春树不在')
        return
    print('看到了春树')
    coop.coop_to(coop.cpn_haruki,td.player)
    event_time_pass(td)
