"""
This class contains constants to be used throughought the code
"""

from enum import Enum

class Elem(Enum):
    FIRE = 1
    WATER = 2
    THUND = 3
    ICE = 4
    DRAG = 5


class Status(Enum):
    PSN = 1
    PARA = 2
    SLEEP = 3
    BLAST = 4


class EquipType(Enum):
    HELM = 1
    CHEST = 2
    ARM = 3
    WAST = 4
    LEG = 5
    CHARM = 6

    GS = 7      # great sword
    SNS = 8     # sword and shield
    DB = 9      # dual blades
    LS = 10     # long sword
    HAM = 11    # hammer
    HH = 12     # hunting horn
    LAN = 13    # lance
    GL = 14     # gun lance
    SA = 15     # switch axe
    CB = 16     # charge blade
    IG = 17     # insect glaive
    BOW = 18    # bow
    LBG = 19    # light bow gun
    HBG = 20    # heavy bow gun
    KIN = 21    # kinsect