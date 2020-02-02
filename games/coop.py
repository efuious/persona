from coops import death
from coops import star
from coops import chariot
from coops import temperance
from coops import hangedman

""" 0. fool:
    1. magician:
    2. high_priestess:
    3. empress:
    4. emperor:
    5. hierophant
    6. lovers
    7. chariot: haruki
    8. strength:
    9. hermit: kaguya
    10. wheel_of_fortune: 
    11. justice:
    12. the_hanged_man: kappa
    13. death: erin
    14. temperance: shion
    15. devil:
    16. tower
    17. star: reimu
    18. moon:
    19. sun
    20. judgement
    21.world
"""

name_list = ['reimu','haruki','shion','kappa','erin']
ncoop = len(name_list)
max_coop_level = 10

class cpn:
    star = 0
    chariot = 1
    temperance = 2
    hangedman = 3
    death = 4

coop_person = [0]*ncoop
coop_special = [0]*ncoop
coop_person[cpn.star]  = star.coop_event
coop_person[cpn.chariot] = chariot.coop_event
coop_person[cpn.death]   = death.coop_event
coop_person[cpn.temperance]  = temperance.coop_event
coop_person[cpn.hangedman]  = hangedman.coop_event

coop_special[cpn.star]  = star.special_day
coop_special[cpn.chariot] = chariot.special_day
coop_special[cpn.death]   = death.special_day
coop_special[cpn.temperance]  = temperance.special_day
coop_special[cpn.hangedman]  = hangedman.special_day

def coop_to(cpn,player):
    coop_person[cpn](player)

def special_day(cpn,td):
    return coop_special[cpn](td)
