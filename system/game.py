from games import person as p
from days import topday
from games import day

class one_day():
    def __init__(self,dayn,player):
        self.day = dayn
        self.player = player

def start_game(dayn,person):
    today = one_day(dayn,person)
    gaming(today)

def gaming(td):
    for i in range(day.ndays):
        day.show_day(td)
    print('GAME CLEAR...\nCONGRATULATIONS！')
    td.player.show_konwn_coop()
    td.player.show_all_status()

def game_save():
    pass

def game_load():
    pass #connect to start_game()

def new_game():
    print('starting games...')
    persona = p.player(p.init_player('new player'))
    d = topday.day_info(0, 0)     #day,time
    start_game(d,persona)

if __name__ == '__main__':
    new_game()