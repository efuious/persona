from games import events as event
from system import guide as guide
from days import day as day


def show_error(errn):
            print('error input: ', errn)

def move(td):
    now = td.day.get_time()
    while now == td.day.get_time():
        guide.move_guide()
        _input = int(input('choose:'))
        if _input == 1:
            house(td)
        elif _input == 2:
            jinja(td)
        elif _input == 3:
            river(td)
        elif _input == 4:
            school(td)
        elif _input == 5:
            street(td)
        else:
            show_error(_input)

def house(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：',td.day.get_time(),now)
        guide.house_guide()
        _input = int(input('choose:'))
        if _input == 1:
            pass
#            games.save(td)   #only player there, no other information
        elif _input == 2:
            move(td)
        elif _input == 3:
            event.study(td)
            return
        elif _input == 4:
            event.sleep(td)
            return
        else:
            show_error(_input)

def jinja(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：', day.time_list[td.day.get_time()], now)
        guide.jinja_guide()
        _input = int(input('choose: '))
        if _input == 1:
            event.coop_reimu(td)
        elif _input == 2:
            pass
        elif _input == 3:
            move(td)
        else:
            show_error(_input)

def school(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：', day.time_list[td.day.get_time()], now)
        guide.school_guide()
        _input = int(input('choose'))
        if _input == 1:
            talk_to_classmate(td)
        elif _input == 2:
            pass
        elif _input == 3:
            move(td)
        else:
            show_error(_input)

def talk_to_classmate(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        guide.school_talk_guide()
        _input = int(input('choose:'))
        if _input == 1:
            event.coop_haruki(td)
        elif _input == 2:
            return
        else:
            show_error(_input)

def river(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        guide.river_guide()
        _input = int(input('choose:'))
        if _input == 1:
            repair_shop(td)
        elif _input == 2:
            return
        else:
            show_error(_input)

def repair_shop(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：', day.time_list[td.day.get_time()], now)
        guide.repair_shop_guide()
        _input = int(input('choose: '))
        if _input == 1:
            pass
        elif _input == 2:
            pass
        elif _input == 3:
            pass
        elif _input == 4:
            pass
        elif _input == 5:
           event.coop_kappa(td)
        else:
            show_error(_input)

def street(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：', day.time_list[td.day.get_time()], now)
        guide.street_guide()
        _input = int(input('choose: '))
        if _input == 1:
            clinic(td)
        elif _input == 2:
            fast_food(td)
        elif _input == 3:
            return
        else:
            show_error(_input)


def clinic(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：', day.time_list[td.day.get_time()], now)
        guide.clinic_guide()
        _input = int(input('choose: '))
        if _input == 1:
            pass
        elif _input == 2:
            return
        elif _input == 3:
            event.coop_erin(td)
        else:
            show_error(_input)

def fast_food(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：', day.time_list[td.day.get_time()], now)
        guide.fast_food_guide()
        _input = int(input('choose: '))
        if _input == 1:
            pass
        elif _input == 2:
            event.coop_shion(td)
        elif _input == 3:
            return
        else:
            show_error(_input)



