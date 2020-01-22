import system as sys
import person as p
import days.day0 as day0
import days.day1 as day1

ndays = 2

days = [0]*ndays
days[0] = day0.today
days[1] = day1.today

class one_day():
    def __init__(self,day,player):
        self.day = day
        self.player = player
        self.init_map()
        self.init_time()

    def init_time(self):
        print('init time')

    def init_map(self):
        print('init map')

    def map_move(self):
        print('map move')


def start_game(day,person):
    today = one_day(day,person)
    gaming(today)


def gaming(td):
    for i in range(ndays):
        print('entering days:',td.day.get_day())
        days[td.day.get_day()](td)


def game_save():
    pass

def game_load():
    pass #connect to start_game()

def new_game():
    print('starting game...')
    persona = p.player(p.init_player('new player'))
    day = sys.day_info(0,0)
    start_game(day,persona)

if __name__ == '__main__':
    new_game()