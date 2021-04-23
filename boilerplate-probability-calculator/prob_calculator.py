import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color in kwargs:
            for _ in range(kwargs[color]):
                self.contents.append(color)
        self.main = copy.deepcopy(self.contents)

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents

        draws = []
        self.contents = copy.deepcopy(self.main)
        for _ in range(num):
            el = random.choice(self.contents)
            draws.append(el)
            self.contents.remove(el)
        return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    for _ in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        expected_result = []
        for ball in expected_balls:
            if result.count(ball) >= expected_balls[ball]:
                expected_result.append(True)
            else:
                expected_result.append(False)
        if all(expected_result):
            matches += 1
    return matches / num_experiments
