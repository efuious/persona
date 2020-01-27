from games import coop


def coop_event_erin(player):
    erin_event = [0] * coop.max_coop_level
    init_event_erin(erin_event)
    erin_event[player.coops[coop.cpn_erin]](player)

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


def coop_event_erin_0(player):
    print('do coop event: erin 0')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_1(player):
    print('do coop event: erin 1')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_2(player):
    print('do coop event: erin 2')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_3(player):
    print('do coop event: erin 3')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_4(player):
    print('do coop event: erin 4')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_5(player):
    print('do coop event: erin 5')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_6(player):
    print('do coop event: erin 6')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_7(player):
    print('do coop event: erin 7')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_8(player):
    print('do coop event: erin 8')
    player.coop_plus(coop.cpn_erin)

def coop_event_erin_9(player):
    print('do coop event: erin 9')
    player.coop_plus(coop.cpn_erin)

if __name__ == '__main__':
    coop_event_erin(3)