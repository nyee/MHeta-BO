from Constants import *

class Equipment(object):
    """Class for Equipments which is parent for Charms, Weapons, and Armor"""
    def __init__(self, name, baseDef, rarity, skills, slots, avail):
        self.name = name
        self.baseDef = baseDef
        self.rarity = rarity        # int from (1-8) determines number of augments
        self.skills = skills        # dict of skillsName to levels
        self.slots = slots          # list of slots in ascending levels
        self.avail = avail          # can be base, event, or iceborne


class Weapon(Equipment):
    """Class for Weapons, we may need some subclasses"""
    def __init__(self, name, baseDef, rarity, skills, slots, avail, type, baseAtt, affinity, element, status, hidden):
        Equipment.__init__(self, name, baseDef, rarity, skills, slots, avail)
        self.type = type
        self.baseAtt = baseAtt      # with bloat factor already divided out 
        self.affinity = affinity    # decimal, not percentage
        self.element = element      # tuple of (Elem, elemental baseAtt), not including phials, baseAtt already divided 10
        self.status = status        # tuple of (Status, status baseAtt), not including phials, baseAtt already divided 10
        self.hidden = hidden        # bool is element/status hidden
        self.numAugments = 0        # int number of augments, 0 if rarity is not at least 6

        # set numAugments based on rarity
        if self.rarity >= 6: self.numAugments = 9 - self.rarity
        
        # set self.hidden to False if always nonElemental, so that we can know if it has a hidden element just by the attribute
        if (self.element or self.status): self.hidden = False

    def isAlwaysNonElem(self):
        return not (self.element or self.status)


class MelWeapon(Weapon):
    """Class for melee weapons (includes sharpness)"""
    def __init__(self, name, baseDef, rarity, skills, slots, avail, type, baseAtt, affinity, element, status, hidden, sharpBar, baseSharp):
        Weapon.__init__(self, name, baseDef, rarity, skills, slots, avail, type, baseAtt, affinity, element, status, hidden)
        self.sharpBar = sharpBar    # list of sharpness values per color
        self.baseSharp = baseSharp  # int of unbuffed sharpness value


class Bow(Weapon):
    """Class for bows (includes sharpness)"""
    def __init__(self, name, baseDef, rarity, skills, slots, avail, type, baseAtt, affinity, element, status, hidden, phials):
        Weapon.__init__(self, name, baseDef, rarity, skills, slots, avail, type, baseAtt, affinity, element, status, hidden)
        self.phials = phials    # set of phials that bow can use

class Armor(Equipment):
    """Class for armor"""
    def __init__(self, name, baseDef, rarity, skills, slots, avail, type, elemDef):
        Equipment.__init__(self, name, baseDef, rarity, skills, slots, avail)
        self.type = type
        self.elemDef = elemDef         #list of elemental Defense?


class Charm(Equipment):
    """Class for charms"""
    type = EquipType.CHARM
    def __init__(self, name, baseDef, rarity, skills, slots, avail):
        Equipment.__init__(self, name, baseDef, rarity, skills, slots, avail)


