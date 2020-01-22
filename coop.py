import coops.reimu as reimu
import coops.haruki as haruki

ncoop = 5
names = ['reimu','haruki','shion','kappa','erin']
levels = [0]*ncoop
max_level = 10

coop_person = [0]*ncoop
coop_person[0] = reimu.coop_event_reimu
coop_person[1] = haruki.coop_event_haruki

cpn_reimu = 0
cpn_haruki = 1
cpn_shion = 2
cpn_kappa = 3
cpn_erin = 4

def coop_to(coop_p_n,player):
    coop_person[coop_p_n](player)