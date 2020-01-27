from games import coop


def coop_event_shion(player):
    shion_event = [0] * coop.max_coop_level
    init_event_shion(shion_event)
    shion_event[player.coops[coop.cpn_shion]](player)

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


def coop_event_shion_0(player):
    print('do coop event: shion 0')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_1(player):
    print('do coop event: shion 1')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_2(player):
    print('do coop event: shion 2')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_3(player):
    print('do coop event: shion 3')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_4(player):
    print('do coop event: shion 4')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_5(player):
    print('do coop event: shion 5')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_6(player):
    print('do coop event: shion 6')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_7(player):
    print('do coop event: shion 7')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_8(player):
    print('do coop event: shion 8')
    player.coop_plus(coop.cpn_shion)

def coop_event_shion_9(player):
    print('do coop event: shion 9')
    player.coop_plus(coop.cpn_shion)

if __name__ == '__main__':
    coop_event_shion(3)