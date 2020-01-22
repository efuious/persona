import coop

def coop_event_erin(coop_level):
    erin_event = [0]*coop.max_level
    init_event_erin(erin_event)
    erin_event[coop_level]()

def init_event_erin(erin_event):
        erin_event[0] = coop_event_erin_0
        erin_event[1] = coop_event_erin_1
        erin_event[2] = coop_event_erin_2
        erin_event[3] = coop_event_erin_3
        erin_event[4] = coop_event_erin_4
        erin_event[5] = coop_event_erin_5
        erin_event[6] = coop_event_erin_6
        erin_event[7] = coop_event_erin_7
        erin_event[8] = coop_event_erin_8
        erin_event[9] = coop_event_erin_9


def coop_event_erin_0():
    print('do coop event: erin 0')

def coop_event_erin_1():
    print('do coop event: erin 1')

def coop_event_erin_2():
    print('do coop event: erin 2')

def coop_event_erin_3():
    print('do coop event: erin 3')

def coop_event_erin_4():
    print('do coop event: erin 4')

def coop_event_erin_5():
    print('do coop event: erin 5')

def coop_event_erin_6():
    print('do coop event: erin 6')

def coop_event_erin_7():
    print('do coop event: erin 7')

def coop_event_erin_8():
    print('do coop event: erin 8')

def coop_event_erin_9():
    print('do coop event: erin 9')


if __name__ == '__main__':
    coop_event_erin(3)