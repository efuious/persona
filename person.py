import coop
import system as sys

zero = 0
nevent = 10
nstatus = 9

name = 0
brave = 1
charm = 2
strength = 3
knowledge = 4
speed = 5
potential = 6
spirit = 7
status = 8
property_list = ['name','brave','charm','strength','knowledge','speed','potential','spirit','status']

class player:
    def __init__(self,player):
        print('loading player: ',player.status[name])
        self.coops = player.coops
#        self.event_list = player.event_list
        self.status = player.status

    def property_plus(self,property_n):
        print(self.status[name],'no',property_list[property_n],'add 1')
        self.status[property_n] += 1

    def coop_plus(self,coop_n):
        print(coop.names[coop_n],'\' coop add 1')
        self.coops[coop_n] += 1
        sys.press()

    # def events_pass(self,event_n):
    #     print('event:',event_n,'passed')
    #     self.event_list[event_n] = 1

    def show_property(self,property_n):
        print(property_list[property_n],':',self.status[property_n])
        return self.status[property_n]

    def show_all_property(self):
        for i in range(nstatus):
            self.show_property(i)

    def show_coop(self,coop_n):
        print(coop.names[coop_n],'\' coops is',self.coops[coop_n])
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
        # self.init_event(nevent)
        self.init_status(nstatus)
        self.init_name(p_name)

    def init_name(self,p_name):
        self.status[name] = p_name

    def init_coops(self,coop_n):
        self.coops = [zero] * coop.ncoop

    # def init_event(self,event_n):
    #     self.event_list = [zero] * nevent

    def init_status(self,nstatus):
        self.status = [zero] * nstatus
        for i in range(1, nstatus):
            self.status[i] = zero

if __name__ == '__main__':
    persona = player(init_player('human'))
    persona.coop_plus(coop.cpn_reimu,2)
    persona.coop_plus(coop.cpn_haruki,4)
    persona.show_coop(coop.cpn_haruki)
    persona.show_coop(coop.cpn_reimu)
    persona.property_plus(brave)
    persona.property_plus(spirit)
    persona.property_plus(speed)
    persona.show_all_property()