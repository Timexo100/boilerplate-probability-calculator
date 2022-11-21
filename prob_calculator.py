import copy
import random
# Consider using the modules imported above.
    
class Hat:
    def __init__(self, **hats):
        cl = []
        for key, value in hats.items():
            for i in range(value):
                cl.append(key)
        self.contents = cl
    
    def draw(self, number):
        outed = [] 
        if number >= len(self.contents):
            return self.contents
        for i in range(number):
            index = random.randint(0, len(self.contents) - 1)
            outed.append(self.contents.pop(index))
        return outed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    mtch = 0
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        eb = []
        outed = h.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            for _ in range(value):
                eb.append(key)
        for ball in outed:
            if ball in eb:
                index = eb.index(ball)
                eb.pop(index)
            if not eb:
                mtch += 1
                break
    return mtch/num_experiments