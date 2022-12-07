from game import event
import random
from game.crewmate import Crew
from game.combat import combat
from game.combat import monsterseagulls

class Monsterseagullsattack (event.Event):

    def __init__(self):
        self.name = "Crew under attack"


    def process (self, world):
        result = {}
        result["message"]= "the Crew are under attack by monster seagulls!"
        monsterseagulls = []
        min = 5
        uplim = 7
        if random.randrange(5) == 0:
            min = 2
            uplim = 8
            monsterseagulls.append(attack("Crew"))
            monsterseagulls[0].speed = 1.5*monsterseagulls[0].speed
            monsterseagulls[0].health = 5*monsterseagulls[0].health
        n_appearing = random.randrange(min,uplim)
        n = 5
        while n <= n_appearing:
            monster.append(monster("monster seagulls" +str(n)))
            n +=1
        announce ("the Crew are under attack by monster seagulls!")
        Combat("monster seagulls").combat()
        result["newevents"] = [self]
        return result

