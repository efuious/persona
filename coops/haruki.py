from games import coop


def coop_event_haruki(player):
    haruki_event = [0] * coop.max_coop_level
    init_event_haruki(haruki_event)
    haruki_event[player.coops[coop.cpn_haruki]](player)

def init_event_haruki(haruki_event):
        haruki_event[0] = coop_event_haruki_0
        haruki_event[1] = coop_event_haruki_1
        haruki_event[2] = coop_event_haruki_2
        haruki_event[3] = coop_event_haruki_3
        haruki_event[4] = coop_event_haruki_4
        haruki_event[5] = coop_event_haruki_5
        haruki_event[6] = coop_event_haruki_6
        haruki_event[7] = coop_event_haruki_7
        haruki_event[8] = coop_event_haruki_8
        haruki_event[9] = coop_event_haruki_9


def coop_event_haruki_0(player):
    print('认识了同学：春树')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_1(player):
    print('和春树一起度过了愉快的时间')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_2(player):
    print('do coop event: haruki 2')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_3(player):
    print('do coop event: haruki 3')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_4(player):
    print('do coop event: haruki 4')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_5(player):
    print('do coop event: haruki 5')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_6(player):
    print('do coop event: haruki 6')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_7(player):
    print('do coop event: haruki 7')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_8(player):
    print('do coop event: haruki 8')
    player.coop_plus(coop.cpn_haruki)

def coop_event_haruki_9(player):
    print('do coop event: haruki 9')
    player.coop_plus(coop.cpn_haruki)
