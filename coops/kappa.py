import coop

def coop_event_kappa(coop_level):
    kappa_event = [0]*coop.max_level
    init_event_kappa(kappa_event)
    kappa_event[coop_level]()

def init_event_kappa(kappa_event):
        kappa_event[0] = coop_event_kappa_0
        kappa_event[1] = coop_event_kappa_1
        kappa_event[2] = coop_event_kappa_2
        kappa_event[3] = coop_event_kappa_3
        kappa_event[4] = coop_event_kappa_4
        kappa_event[5] = coop_event_kappa_5
        kappa_event[6] = coop_event_kappa_6
        kappa_event[7] = coop_event_kappa_7
        kappa_event[8] = coop_event_kappa_8
        kappa_event[9] = coop_event_kappa_9


def coop_event_kappa_0():
    print('do coop event: kappa 0')

def coop_event_kappa_1():
    print('do coop event: kappa 1')

def coop_event_kappa_2():
    print('do coop event: kappa 2')

def coop_event_kappa_3():
    print('do coop event: kappa 3')

def coop_event_kappa_4():
    print('do coop event: kappa 4')

def coop_event_kappa_5():
    print('do coop event: kappa 5')

def coop_event_kappa_6():
    print('do coop event: kappa 6')

def coop_event_kappa_7():
    print('do coop event: kappa 7')

def coop_event_kappa_8():
    print('do coop event: kappa 8')

def coop_event_kappa_9():
    print('do coop event: kappa 9')


if __name__ == '__main__':
    coop_event_kappa(3)