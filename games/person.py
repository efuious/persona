from games import coop
from system import control as sys

status_list = ['name','brave','charm','strength','knowledge','speed','potential','spirit','status']

zero = 0
nstatus = len(status_list)
s_name = 0
s_brave = 1
s_charm = 2
s_strength = 3
s_knowledge = 4
s_speed = 5
s_potential = 6
s_spirit = 7
s_status = 8

class player:
    def __init__(self,p):
        print('loading player: ',p.status[s_name])
        self.coops = p.coops
        self.status = p.status

    def status_plus(self,status_n):
        print(self.status[s_name],'的',status_list[status_n],'提升了')
        self.status[status_n] += 1
        sys.press()

    def coop_plus(self,coop_n):
        print(coop.name_list[coop_n], '的 coop 提升了')
        self.coops[coop_n] += 1
        sys.press()

    def show_status(self,status_n):
        print(status_list[status_n],':',self.status[status_n])
        return self.status[status_n]

    def show_all_status(self):
        for i in range(nstatus):
            self.show_status(i)

    def show_coop(self,coop_n):
        print(coop.name_list[coop_n], '\' coops is', self.coops[coop_n])
        return self.coops[coop_n]

    def show_konwn_coop(self):
        for i in range(coop.ncoop):
            if self.coops[i] != 0:
                self.show_coop(i)

    def show_all_coop(self):
        for i in range(coop.ncoop):
            self.show_coop(i)


class init_player:
    def __init__(self,p_name):
        print('init player: ', p_name)
        self.init_coops(coop.ncoop)
        self.init_status(nstatus)
        self.init_name(p_name)

    def init_name(self,p_name):
        self.status[s_name] = p_name

    def init_coops(self,coop_n):
        self.coops = [zero] * coop.ncoop

    def init_status(self,nstatus):
        self.status = [zero] * nstatus
        for i in range(1, nstatus):
            self.status[i] = zero

if __name__ == '__main__':
    persona = player(init_player('human'))
    persona.coop_plus(coop.cpn_reimu)
    persona.coop_plus(coop.cpn_reimu)
    persona.coop_plus(coop.cpn_haruki)
    persona.coop_plus(coop.cpn_haruki)
    print('已知的coop:')
    persona.show_konwn_coop()