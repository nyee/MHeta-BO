
import unittest
from Equipment import *
from Constants import *
from

bloatFactor = {EquipType.GS: 4.8,
               EquipType.SNS: 1.4,
               EquipType.DB: 1.4,
               EquipType.LS: 3.3,
               EquipType.HAM: 5.2,
               EquipType.HH: 4.2,
               EquipType.LAN: 2.3,
               EquipType.GL: 2.3,
               EquipType.SA: 3.5,
               EquipType.CB: 3.6,
               EquipType.IG: 3.1,
               EquipType.BOW: 1.2,
               EquipType.LBG: 1.3,
               EquipType.HBG: 1.5,
               }

def getTrueAtt(printAtt, type):
    # Divides out the bloat factor giving true attack from printed attack for a given weapon type
    return printAtt/bloatFactor[type]

class TestWeapons(unittest.TestCase):

    def testWeaponIsNonElem(self):
        # Test isNonElemental on a elemental weapon
        anguish = MelWeapon(name = "Anguish",
                         baseDef = 0,
                         rarity = 7,
                         slots = [], 
                         skills = {},
                         avail = Avail.BASE,
                         type = EquipType.GS,
                         baseAtt = getTrueAtt(1104, EquipType.GS),
                         affinity = -0.3,
                         element = (Elem.DRAG, 24),
                         status = None,
                         hidden = False,
                         sharpBar = [20, 40, 20, 20, 20, 20],
                         baseSharp = 115
                         )
        
        self.assertFalse(anguish.isAlwaysNonElem(), 
                         "Weapon: " + anguish.name + "failed to return 'False' on isAlwaysNonEle")

        ignition = MelWeapon(name = "Anguish",
                         baseDef = 0,
                         rarity = 7,
                         slots = [], 
                         skills = {},
                         avail = Avail.EV,
                         type = EquipType.GS,
                         baseAtt = getTrueAtt(1104, EquipType.GS),
                         affinity = -0.3,
                         element = None,
                         status = None,
                         hidden = False,
                         sharpBar = [20, 40, 20, 20, 20, 20],
                         baseSharp = 115
                         )
        
        self.assertTrue(ignition.isAlwaysNonElem(), 
                         "Weapon: " + ignition.name + "failed to return 'True' on isAlwaysNonEle")

        cera = Bow(name = "Cera Coilbender",
                      baseDef = 0,
                      rarity = 8,
                      slots = [], 
                      skills = {},
                      avail = Avail.BASE,
                      type = EquipType.BOW,
                      baseAtt = getTrueAtt(264, EquipType.BOW),
                      affinity = -0.3,
                      element = (Elem.ICE, 15),
                      status = None,
                      hidden = True,
                      phials = set([BowPhils.CLOSE, BowPhils.POWER, BowPhils.PARA])
                      )
        
        self.assertFalse(cera.isAlwaysNonElem(), 
                         "Weapon: " + cera.name + "failed to return 'False' on isAlwaysNonEle")

if __name__== '__main__':
    unittest.main()