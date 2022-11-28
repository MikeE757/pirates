from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Seagull (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "seagull visitor"
        self.seagulls = 1
        self.verbs['chase'] = self
        self.verbs['health']= self
        self.verbs['fight'] = self
        self.verbs['wave']  = self
        self.verbs['health']= self
        self.verbs['defeat'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
            self.go = True
            r = random.randint(1,10)
            if (r < 5):
                self.result["message"] = "the seagulls don't fly off."
                if (self.seagulls > 1):
                    self.seagulls = self.seagulls - 1
            else:
                c = random.choice(config.the_player.get_pirates())
                if (c.lucky == True):
                    self.result["message"] = "Sorry,the seagulls doesn't fly off."
                else:
                    self.result["message"] = c.get_name() + "seagulls heading towards your direction."
                    if (c.inflict_damage (self.seagulls, "Almost pecked to death by seagulls")):
                        self.result["message"] = ".. " + c.get_name() + " is pecked to death by the seagulls!"

        elif (verb == "fight"):
            self.seagulls = self.seagulls + 1
            self.result["newevents"].append (Seagull())
            self.result["message"] = "the seagulls are more aggressive"
            self.go = True
        elif (verb == "help"):
            print ("the seagulls will pester you until you kill them all")
            self.go = False
        else:
            print ("it seems the only options here are to fight them off")
            self.go = False



    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "The first wave of seagulls are gone. You survived the first wave of seagulls"

        while (self.go == False):
            print (str (self.seagulls) + " seagulls has appeared what do you want to do?")
            Player.get_interaction ([self])

        return self.result
