from games import coop

status_list = ['name','brave','charm','strength','knowledge','speed','potential','spirit','status','money']
zero = 0

class property:
    name        = 0
    brave       = 1
    charm       = 2
    strength    = 3
    knowledge   = 4
    speed       = 5
    potential   = 6
    spirit      = 7
    status      = 8
    money       = 9

class player:
    def __init__(self,p):
        print('loading player: ',p.status[property.name])
        self.coops = p.coops
        self.status = p.status

    def status_plus(self,status_n):
        print(self.status[property.name],'的',status_list[status_n],'提升了')
        self.status[status_n] += 1

    def coop_plus(self,coop_n,level):
        print(coop.name_list[coop_n], '的 coop 提升了',level)
        self.coops[coop_n] += level

    def show_status(self,status_n):
        print(status_list[status_n],':',self.status[status_n])
        return self.status[status_n]

    def show_all_status(self):
        for i in range(len(status_list)):
            self.show_status(i)

    def show_coop(self,coop_n):
        print(coop.name_list[coop_n], '的coop：', self.coops[coop_n])
        return self.coops[coop_n]

    def show_konwn_coop(self):
        for i in range(coop.ncoop):
            if self.coops[i] != 0:
                self.show_coop(i)

    def show_all_coop(self):
        for i in range(coop.ncoop):
            self.show_coop(i)

    def refresh(self):
        self.status[property.status] = 1

class init_player:
    def __init__(self,p_name):
        print('init player: ', p_name)
        self.init_coops(coop.ncoop)
        self.init_status(len(status_list))
        self.init_name(p_name)

    def init_name(self,p_name):
        self.status[property.name] = p_name

    def init_coops(self,coop_n):
        self.coops = [zero] * coop.ncoop

    def init_status(self,nstatus):
        self.status = [zero] * nstatus
        for i in range(1, nstatus):
            self.status[i] = zero
        self.status[property.money] += 100000
