from games import coop

def coop_event_reimu(player):
    reimu_event = [0] * coop.max_coop_level
    init_event_reimu(reimu_event)
    reimu_event[player.coops[coop.cpn_reimu]](player)

def init_event_reimu(reimu_event):
        reimu_event[0] = coop_event_reimu_0
        reimu_event[1] = coop_event_reimu_1
        reimu_event[2] = coop_event_reimu_2
        reimu_event[3] = coop_event_reimu_3
        reimu_event[4] = coop_event_reimu_4
        reimu_event[5] = coop_event_reimu_5
        reimu_event[6] = coop_event_reimu_6
        reimu_event[7] = coop_event_reimu_7
        reimu_event[8] = coop_event_reimu_8
        reimu_event[9] = coop_event_reimu_9


def coop_event_reimu_0(player):
    print('认识了巫女：灵梦')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_1(player):
    print('do coop event: reimu 1')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_2(player):
    print('do coop event: reimu 2')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_3(player):
    print('do coop event: reimu 3')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_4(player):
    print('do coop event: reimu 4')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_5(player):
    print('do coop event: reimu 5')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_6(player):
    print('do coop event: reimu 6')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_7(player):
    print('do coop event: reimu 7')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_8(player):
    print('do coop event: reimu 8')
    player.coop_plus(coop.cpn_reimu)

def coop_event_reimu_9(player):
    print('do coop event: reimu 9')
    player.coop_plus(coop.cpn_reimu)
