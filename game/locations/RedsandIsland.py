from game import location
import game.config as config
from game.display import announce
from game.events import *
import game.items as items
import random

class Island (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "Redsand Island"
        self.symbol = 'R'
        self.visitable = True
        self.starting_location = Beach_with_ship(self)
        self.locations = {}
        self.locations["beach"] = self.starting_location
        self.locations["trees"] = Trees(self)
        self.locations["Sand"] = Sand(self)
        self.locations["Cave"]= Cave(self)
        self.locations["Boulders"] = Boulders(self)
        self.locations["Treasure"] = Treasure
        self.locations["Forest"] = Forest(self)
        # self.locations[""]
        

    def enter (self, ship):
        print ("arrived at an island")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Beach_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "beach"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 50
        self.events.append (seagull.Seagull())
        self.events.append(drowned_pirates.DrownedPirates())

    def enter (self):
        announce ("arrive at the beach. Your ship is at anchor in a small bay to the south.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["trees"]
        elif (verb == "east" or verb == "west"):
            announce ("You walk all the way around the island on the beach. It's not very interesting.")


class Trees (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "trees"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        # Include a couple of items and the ability to pick them up, for demo purposes
        self.verbs['take'] = self
        self.item_in_tree = items.Cutlass()
        self.item_in_clothes = items.Flintlock()

        self.event_chance = 50
        self.events.append(man_eating_monkeys.ManEatingMonkeys())
        self.events.append(drowned_pirates.DrownedPirates())

class Sand(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "Sand"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
        # self.item

class Cave(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "Sand"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
        # self.item

class Boulders(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "Sand"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
        # self.item

class Treasure(location.SubLocation):
    def __init__(self,m):
        super().__init__()
        self.name = "Sand"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
        # self.item

class Forest(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "Sand"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
        # self.item


    def enter (self):
        edibles = False
        for e in self.events:
            if isinstance(e, man_eating_monkeys.ManEatingMonkeys):
                edibles = True
        #The description has a base description, followed by variable components.
        description = "You walk into the small forest on the island."
        if edibles == False:
             description = description + " Nothing around here looks very edible."

        #Add a couple items as a demo. This is kinda awkward but students might want to complicated things.
        if self.item_in_tree != None:
            description = description + " You see a " + self.item_in_tree.name + " stuck in a tree."
        if self.item_in_clothes != None:
            description = description + " You see a " + self.item_in_clothes.name + " in a pile of shredded clothes on the forest floor."
        announce (description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["beach"]
        #Handle taking items. Demo both "take cutlass" and "take all"
        if verb == "take":
            if self.item_in_tree == None and self.item_in_clothes == None:
                announce ("You don't see anything to take.")
            elif len(cmd_list) > 1:
                at_least_one = False #Track if you pick up an item, print message if not.
                item = self.item_in_tree
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You take the "+item.name+" from the tree.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_tree = None
                    config.the_player.go = True
                    at_least_one = True
                item = self.item_in_clothes
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You pick up the "+item.name+" out of the pile of clothes. ...It looks like someone was eaten here.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_clothes = None
                    config.the_player.go = True
                    at_least_one = True
                if at_least_one == False:
                    announce ("You don't see one of those around.")
class RPG(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (100,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class Grenade(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (100,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class GrenadeLauncher(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (100,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class Landmine(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (100,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"


class Glock19(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (56,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class DesertEagle(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (85,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class AK47(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (95,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class AR15(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (98,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class MP5HK(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (88,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class DesertEagle(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (85,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class MicroUzi(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (75,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class Tec9(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (85,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class Mac10(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (85,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class SawnoffShotgun(items.Item):
    def __init__(self):
        super().__init__("", 400)
        self.damage = (55,100)
        self.firearm = True
        self.charges = 1
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"
class Katana(items.Item):
    def __init__(self):
        super().__init__("cutlass", 5)
        self.damage = (10,60)
        self.skill = "swords"
        self.verb = "slash"
        self.verb2 = "slashes"

#Define the map with locations and their descriptions
locations = {"beach": "You are standing on a sandy beach.","cave": "treasure" "You found the treasure" "You are at the entrance of a dark cave." , "forest": "You are in a dense forest with tall trees" "mountain""You are at the foot of a step mountain."}
class Cave(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "Cave"
        self.verbs['read'] = self
        self.tries = 0
        self.solved = False

    def enter (self):
        announce("You defeated the enemies guarding the entrance. You notice a Boulder .")
        announce("The boulder is blocking your path to the Forest. It seems to be a sign on the wall.")
        announce("The sign has a riddle written on it.")

    def process_verb(self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["Cave"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Forest"]
        elif (verb == "read"):
            while self.solved == False:
                print("If you want to make it to the Forest you must first solve this riddle"
                  " The riddle states:'I easy to lift.; but hard to throw.; "
                  "What am I")
                print("You can enter the answer to the riddle or ask for a hint ")
                answer = input("What is the answer to the riddle?: ")
                if answer == "feather":
                   

                    announce("You destoryed the boulder. You can now enter the Forest")
                    config.the_player.next_loc = self.main_location.locations["Forest"]
                    self.solved = True
                elif answer == "hint":
                    print("I'm light")
                
                elif self.tries >= 2:
                    print("You have gotten it wrong. It was an easy riddle!")
                    config.the_player.gameInProgress = False
                    config.the_player.kill_all_pirates("")
                self.tries += 1


