import system as sys
import events as event
import guide as g

def move(td):
    now = td.day.get_time()
    while now == td.day.get_time():
        g.move_guide()
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
            print('error input:',_input)

def house(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：',td.day.get_time(),now)
        g.house_guide()
        _input = int(input('choose:'))
        if _input == 1:
            pass
#            game.save(td)   #only player there, no other information
        elif _input == 2:
            move(td)
        elif _input == 3:
            event.study(td)
            return
        elif _input == 4:
            event.sleep(td)
            return
        else:
            print('error input:',_input)

def repair_shop(td):
    print('entering repair shop...')
    move(td)

def jinja(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：',sys.time_name[td.day.get_time()],now)
        g.jinja_guide()
        _input = int(input('choose: '))
        if _input == 1:
            event.coop_reimu(td)
        elif _input == 2:
            pass
        elif _input == 3:
            move(td)
        else:
            print('error input:',_input)

def school(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        print('现在是：',sys.time_name[td.day.get_time()],now)
        g.school_guide()
        _input = int(input('choose'))
        if _input == 1:
            talk_to_classmate(td)
        elif _input == 2:
            pass
        elif _input == 3:
            move(td)
        else:
            print('error input:',_input)

def talk_to_classmate(td):
    now = td.day.get_time()
    while td.day.get_time() == now:
        g.school_talk_guide()
        _input = int(input('choose:'))
        if _input == 1:
            event.coop_haruki(td)
        elif _input == 2:
            return
        else:
            print('error input: ',_input)



def river(td):
    print('entering river...')
    move(td)

def street(td):
    print('entering street...')
    move(td)



