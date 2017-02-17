'''
Created on 16 Feb 2017
@author: Harrison Baillie
'''
#SKYRIM AFTER ALDUIN - VERSION 3, REVISED
locations=["Whiterun","Winterhold","Riften","Markarth","Dawnstar","Morthal","Solitude","Falkreath","Windhelm","Unknown"]
class Location(object):
    def __init__(self, name="Unknown", available=False, enemy=False, bounty=int(0)):
        self.name=name
        self.available=available
        self.enemy=enemy
        self.bounty=bounty

class race(object):
    def __init__(self, title="Unknown", health=int(0), magicka=int(0)):
        self.title=title
        self.health=health
        self.magicka=magicka
R01=race("Nord",40,5)
R02=race("Breton",50,3)
R03=race("Elf",30,10)
R04=race("Khajiit",35,7)
R05=race("Orc",60,2)
racesobj=[R01,R02,R03,R04,R05]
races=["Nord","Breton","Elf","Khajiit","Orc"]

class playerType(object):
    def __init__(self, title="Unknown", magicka=int(0), atk=int(0)):
        self.title=title
        self.magicka=magicka
        self.atk=atk
heavy=playerType("Heavy",5,25)
light=playerType("Light",10,20)
mage=playerType("Mage",30,15)
playertypes=["Heavy","Light","Mage"]
playertypesobj=[heavy,light,mage]
class Player(object):
    def __init__(self, name="Unknown", playertype="Unknown",deceased=False, magicka=int(0),attack=int(0),gold=int(0), health=int(0), location=locations[9], race="Unknown"):
        self.name=name
        self.deceased=deceased
        self.magicka=magicka
        self.attack=attack
        self.gold=gold
        self.health=health
        self.location=location
        self.race=race
        self.playertype=playertype
Player=Player()
def charCreation():
    usin=input("Please enter your character's race.\n- Nord\n- Breton\n- Elf\n- Khajiit\n- Orc\n")
    while usin not in races:
        print("Race not available.")
        usin=input("Please enter your character's race.\n- Nord\n- Breton\n- Elf\n- Khajiit\n- Orc\n")
    loop=int(0)
    for i in range(len(racesobj)):
        if racesobj[loop].title==usin:
            Player.race=racesobj[loop]
        else:
            loop=loop+1
    usin=input("Please enter your character's player type.\n- Heavy\n- Light\n- Mage")
    while usin not in playertypes:
        print("Unavailable player type.")
        usin=input("Please enter your character's player type.\n- Heavy\n- Light\n- Mage\n")
    if usin == playertypes[0].title:
        Player.playertype=heavy
    elif usin == playertypes[1].title:
        Player.playertype=light
    elif usin == playertypes[2].title:
        Player.playertype=mage
    loop=int(0)
    for i in range(len(playertypesobj)):
        if playertypesobj[loop]==usin:
            Player.playertype=playertypesobj[loop]
        else:
            loop=loop+1
    loop=int(0)
    for i in range(len(racesobj)):
        if racesobj[loop].title==Player.race:
            Player.magicka=Player.magicka+(racesobj[loop].magicka)
            Player.health=Player.health+(racesobj[loop].health)
        else:
            loop=loop+1
    loop=int(0)
    for i in range(len(playertypesobj)):
        if playertypesobj[loop].title==Player.playertype:
            Player.attack=Player.attack+(playertypesobj[loop].atk)
        else:
            loop=loop+1
charCreation()
print(Player.race.title,Player.health,Player.magicka,Player.playertype)