from games import person as p
from days import day0 as day0
from days import day1 as day1
from days import day

ndays = 2

days = [0]*ndays
days[0] = day0.day0
days[1] = day1.day1

class one_day():
    def __init__(self,day,player):
        self.day = day
        self.player = player

def start_game(day,person):
    today = one_day(day,person)
    gaming(today)


def gaming(td):
    for i in range(ndays):
        print('entering days:',td.day.get_day())
        days[td.day.get_day()](td)
    print('GAME CLEAR...\nCONGRATULATIONS！')
    td.player.show_konwn_coop()

def game_save():
    pass

def game_load():
    pass #connect to start_game()

def new_game():
    print('starting games...')
    persona = p.player(p.init_player('new player'))
    d = day.day_info(0, 0)     #day,time
    start_game(d,persona)

if __name__ == '__main__':
    new_game()