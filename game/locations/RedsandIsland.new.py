from  game import combat, location
import game.config as config
import game.display as display
from   game.events import *
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
        self.locations["Sand"] =  (self)
        self.locations["Cave"]= Cave(self)
        self.locations["Boulder"] = Boulder(self)
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
        display.announce ("arrive at the beach. Your ship is at anchor in a small bay to the south.")

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            display.announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["trees"]
        elif (verb == "east" or verb == "west"):
            display.announce ("You walk all the way around the island on the beach. It's not very interesting.")


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
        #self.events.append(man_eating_monkeys.ManEatingMonkeys())
        self.events.append(drowned_pirates.DrownedPirates())

class Cave(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "Cave Entrance"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
        self.event_chance = 25
        self.events.append(seagull.Seagull())

    def enter (self):
        description = "You walk upon the beach. You entered into a Cave."
        display.announce(description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.location["Cave"]
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["Treasure"]
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["Trees"]
        if (verb == "enter"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["Forest"]
            self.event_chance = 100
        # self.item

class Forest(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "Forest Entrance"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
        # self.item
        self.event_chance = 50
        #self.events.append(Cave())


    def enter (self):
        display.announce("You came arcoss a Forest. You have entered the Forest.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" ):
            config.the_player.next_loc = self.main_location.locations["beach"]
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Cave"]



class Cave(location.SubLocation):
    def __init__(self, m):
        super().__init__(m)
        self.name = "Cave Entrance"
        self.verbs['read'] = self
        self.tries = 0
        self.solved = False
        self.event_chance = 100
        self.events.append(())

def enter (self):
        description = "You walk upon the beach. You entered into a Cave."
        display.announce(description)

def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.location["Sand"]
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["Treasure"]
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["Trees"]
        if (verb == "enter"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["Forest"]


class Boulder(location.SubLocation):
    def __init__(self,m):
        super().__init__(m)
        self.name = "Sand"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.verbs['take'] = self
    def enter (self):
        description = "You walk upon the beach. You entered into a Cave."
        display.announce(description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.location["Sand"]
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["Treasure"]
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["Trees"]
        if (verb == "enter"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["Forest"]
            self.event_chance = 50
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
    def enter (self):
        description = "You walk upon the beach. You entered into a Treasure Room."
        display.announce(description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.location["Cave"]
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["Treasure"]
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["Trees"]
        if (verb == "enter"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["Forest"]
            self.event_chance = 50
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
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.location["Cave"]
        if (verb == "east"):
            config.the_player.next_loc = self.main_location.locations["Treasure"]
        if (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["Trees"]
        if (verb == "enter"):
            config.the_player.go = True
            config.the_player.next_loc = self.main_location.locations["Forest"]
            self.event_chance = 50
        # self.item


    def enter (self):
        edibles = False
        #for e in self.events:
        #    if isinstance(man_eating_monkeys.ManEatingMonkeys):
        #        edibles = True
        #The description has a base description, followed by variable components.
        description = "You walk into the small forest on the island."
        if edibles == False:
             description = description + " Nothing around here looks very edible."

        #Add a couple items as a demo. This is kinda awkward but students might want to complicated things.
        if self.item_in_tree != None:
            description = description + " You see a " + self.item_in_tree.name + " stuck in a tree."
        if self.item_in_clothes != None:
            description = description + " You see a " + self.item_in_clothes.name + " in a pile of shredded clothes on the forest floor."
        display.announce (description)

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["beach"]
        #Handle taking items. Demo both "take cutlass" and "take all"
        if verb == "take":
            if self.item_in_tree == None and self.item_in_clothes == None:
                display.announce ("You don't see anything to take.")
            elif len(cmd_list) > 1:
                at_least_one = False #Track if you pick up an item, print message if not.
                item = self.item_in_tree
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    display.announce ("You take the "+item.name+" from the tree.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_tree = None
                    config.the_player.go = True
                    at_least_one = True
                item = self.item_in_clothes
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    display.announce ("You pick up the "+item.name+" out of the pile of clothes. ...It looks like someone was eaten here.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_clothes = None
                    config.the_player.go = True
                    at_least_one = True
                if at_least_one == False:
                    display.announce ("You don't see one of those around.")
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
treasure_location = random.choice(list(locations.keys()))
#Define the treasure location 
treasure_location = random.choice(list(locations.keys()))

class GiantBugEvent:
    def __init__(self):
        self.name = " Giant Bug attack."  
    def process(self,world):
        result = {}
        Bug = Bug
        display.announce("A giant Bug is coming to attack you and your crew. You have it kill it!")
        combat.combat([Bug]).combat()
        display.announce("The Bug Goes Crazy.")
        result["new events"] =[]
        result ["message"] = " "
        display. announce("In the Sand you can find the gun.")
        config.the_player.add_to_inventory
        (SawnoffShotgun())
        return result
class GiantBigBug:
    def __init_(self):
        attack = {}
        attack["bite"] = ["bite,random(90,100])"]
        attack["cut"] = ["cut", random.randomrange(90,100)]
        super().__init__("GiantBug",random.randint(0,10))
        self.type_name="BugBug"
class Glock19(items):
    def __init__(self):
        super().__init__("Glock19")
        self.damage=(50,100)
        self.verb = "slam"
        self.verb2 = "slams"
        self.NUMBER_OF_ATTACKS=5
    def PickTarget(self,action,attacker,allies,enemies):
        if(len(enemies)<=self.NUMBER_OF_ATTACKS):
          return enemies
        else:
            option=[]
            for "t" in enemies:
            option.append("attack")
            targets = []
            while(len(targets)<self.NUMBER_OF_ATTACKS):
            display.announce(f"Pick target number"len(targets)}, pause= False)
            choice = menu(option):
        if (not choice in targets):
            target.append(enemies[choice])
            return targets
class PiratePuzzleGame:
    def __init__(self):
        self.puzzles = [{"riddle": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
                "answer": "map"},
            {"riddle": "What has keys, but no locks; space, but no room; you can enter, but not go in?",
                "answer": "keyboard"}
            {
                "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
                "answer": "echo"
            }]
        self.max_attempts = 3

    def start_game(self):
        print("PIRATE PUZZLE ISLAND ESCAPE")
        print("\nYou are a stranded pirate on a mysterious island.")
        print("Solve the puzzle to escape, or face certain doom!")
        print("\nYou have 3 attempts to solve the riddle.\n")
        
        self.play_puzzle()

    def play_puzzle(self):
        # Select a random puzzle
        puzzle = random.choice(self.puzzles)
        
        for attempt in range(self.max_attempts):
            print(f"Puzzle: {puzzle['riddle']}")
            print(f"Attempt {attempt + 1} of {self.max_attempts}")
            
            # Get player's answer
            player_answer = input("Your answer: ").lower().strip()
            
            # Check the answer
            if player_answer == puzzle['answer']:
                self.escape_island()
                return
            else:
                remaining_attempts = self.max_attempts - (attempt + 1)
                if remaining_attempts > 0:
                    print(f"\nWrong answer! {remaining_attempts} attempts remaining.\n")
                else:
                    self.die_on_island()

    def escape_island(self):
        print("CONGRATULATIONS!")
        print("You solved the puzzle!")
        print("A magical bridge appears...")
        print("You successfully escape the island!")
        

    def die_on_island(self):
        print("GAME OVER!")
        print("You failed to solve the puzzle...")
        print("The island claims another victim.")
        print("You perish alone, trapped forever!")
        
def main():
    while True:
        game = PiratePuzzleGame()
        game.start_game()
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Farewell, brave pirate!")
            break
def __init__(self):
        self.puzzles = [
            {"riddle": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
                "answer": "map"},
            {"riddle": "What has keys, but no locks; space, but no room; you can enter, but not go in?",
                "answer": "keyboard"},
            {"riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
                "answer": "echo"}
        ]
        self.max_attempts = 5

def start_game(self):
        print("PIRATE PUZZLE ISLAND ESCAPE")
        print("\nYou are a stranded pirate on a mysterious island.")
        print("Solve the puzzle to escape, or face certain doom!")
        print("\nYou have 3 attempts to solve the riddle.\n")
        
        self.play_puzzle()

def play_puzzle(self):
        # Select a random puzzle
        puzzle = random.choice(self.puzzles)
        
        for attempt in range(self.max_attempts):
            print(f"Puzzle: {puzzle['riddle']}")
            print(f"Attempt {attempt + 1} of {self.max_attempts}")
            
            # Get player's answer
            player_answer = input("Your answer: ").lower().strip()
            
            # Check the answer
            if player_answer == puzzle['answer']:
                self.escape_island()
                return
            else:
                remaining_attempts = self.max_attempts - (attempt + 1)
                if remaining_attempts > 0:
                    print(f"\nWrong answer! {remaining_attempts} attempts remaining.\n")
                else:
                    self.die_on_island()

def escape_island(self):
        print("Congratulations!")
        print("You solved the puzzle!")
        print("A magical bridge appears...")
        print("You successfully escape the island!")
        time.sleep(2)
        sys.exit()

def die_on_island(self):
        print("Game Over!")
        print("You failed to solve the puzzle...")
        print("The island claims killed our crew and you .")
        print("You perish alone, trapped forever!")
        time.sleep(2)
        sys.exit()

def main():
    while True:
        game = PiratePuzzleGame()
        game.start_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing pirate!")
            break
import random

# Initialize the game board
board_size = 5
board = [['-' for _ in range(board_size)] for _ in range(board_size)]

# Place the treasure
treasure_x, treasure_y = random.randint(0, board_size-1), random.randint(0, board_size-1)
board[treasure_x][treasure_y] = 'T'

# Function to print the board
def print_board():
    for row in board:
        print(' '.join(row))

# Player's starting position
player_x, player_y = 0, 0
board[player_x][player_y] = 'P'

# Main game loop
while True:
    print_board()
    move = input("Enter your move (up, down, left, right): ").strip().lower()
    
    # Update player's position
    board[player_x][player_y] = '-'
    if move == 'up' and player_x > 0:
        player_x -= 1
    elif move == 'down' and player_x < board_size - 1:
        player_x += 1
    elif move == 'left' and player_y > 0:
        player_y -= 1
    elif move == 'right' and player_y < board_size - 1:
        player_y += 1
    board[player_x][player_y] = 'P'
    
    # Check for treasure
    if player_x == treasure_x and player_y == treasure_y:
        print("Congratulations! You found the treasure!")
        break

