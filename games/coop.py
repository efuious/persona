from coops import erin
from coops import reimu
from coops import haruki
from coops import shion
from coops import kappa

name_list = ['reimu','haruki','shion','kappa','erin']
ncoop = len(name_list)
levels = [0]*ncoop
max_coop_level = 10

cpn_reimu = 0
cpn_haruki = 1
cpn_shion = 2
cpn_kappa = 3
cpn_erin = 4

coop_person = [0]*ncoop
coop_person[cpn_reimu]  = reimu.coop_event_reimu
coop_person[cpn_haruki] = haruki.coop_event_haruki
coop_person[cpn_erin]   = erin.coop_event_erin
coop_person[cpn_shion]  = shion.coop_event_shion
coop_person[cpn_kappa]  = kappa.coop_event_kappa

def coop_to(coop_p_n,player):
    coop_person[coop_p_n](player)