from games import coop


def coop_event_kappa(player):
    kappa_event = [0] * coop.max_coop_level
    init_event_kappa(kappa_event)
    kappa_event[player.coops[coop.cpn_kappa]](player)

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


def coop_event_kappa_0(player):
    print('do coop event: kappa 0')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_1(player):
    print('do coop event: kappa 1')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_2(player):
    print('do coop event: kappa 2')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_3(player):
    print('do coop event: kappa 3')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_4(player):
    print('do coop event: kappa 4')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_5(player):
    print('do coop event: kappa 5')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_6(player):
    print('do coop event: kappa 6')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_7(player):
    print('do coop event: kappa 7')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_8(player):
    print('do coop event: kappa 8')
    player.coop_plus(coop.cpn_kappa)

def coop_event_kappa_9(player):
    print('do coop event: kappa 9')
    player.coop_plus(coop.cpn_kappa)

if __name__ == '__main__':
    coop_event_kappa(3)