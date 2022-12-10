from game import event
import random
from game.combat import Combat
from game.combat import Monsterseagulls
from game.display import announce 

class Monsterseagullsattack (event.Event):

    def __init__(self):
        self.name = "Crew under attack"


    def process (self, world):
        result = {}
        result["message"]= "the Crew are under attack by monster seagulls!"
        seagulls = []
        min = 5
        uplim = 7
        if random.randrange(5) == 0:
            min = 2
            uplim = 8
            seagulls.append(attack())
            seagulls[0].speed = 1.5*seagulls[0].speed
            seagulls[0].health = 5*seagulls[0].health
        n_appearing = random.randrange(min,uplim)
        n = 5
        while n <= n_appearing:
            seagulls.append(Monsterseagulls("monster seagulls" +str(n)))
            n +=1
        announce ("the Crew are under attack by monster seagulls!")
        Combat(seagulls).combat()
        result["newevents"] = [self]
        return result

