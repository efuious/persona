import coop

def coop_event_shion(coop_level):
    shion_event = [0]*coop.max_level
    init_event_shion(shion_event)
    shion_event[coop_level]()

def init_event_shion(shion_event):
        shion_event[0] = coop_event_shion_0
        shion_event[1] = coop_event_shion_1
        shion_event[2] = coop_event_shion_2
        shion_event[3] = coop_event_shion_3
        shion_event[4] = coop_event_shion_4
        shion_event[5] = coop_event_shion_5
        shion_event[6] = coop_event_shion_6
        shion_event[7] = coop_event_shion_7
        shion_event[8] = coop_event_shion_8
        shion_event[9] = coop_event_shion_9


def coop_event_shion_0():
    print('do coop event: shion 0')

def coop_event_shion_1():
    print('do coop event: shion 1')

def coop_event_shion_2():
    print('do coop event: shion 2')

def coop_event_shion_3():
    print('do coop event: shion 3')

def coop_event_shion_4():
    print('do coop event: shion 4')

def coop_event_shion_5():
    print('do coop event: shion 5')

def coop_event_shion_6():
    print('do coop event: shion 6')

def coop_event_shion_7():
    print('do coop event: shion 7')

def coop_event_shion_8():
    print('do coop event: shion 8')

def coop_event_shion_9():
    print('do coop event: shion 9')


if __name__ == '__main__':
    coop_event_shion(3)