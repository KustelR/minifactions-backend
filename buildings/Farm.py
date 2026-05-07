import random

from Entities import Building


class Farm(Building):
    name = "farm"
    food_gain: int = 0
    building_quality = 0
    defense = 1

    def __init__(self, chunk, food_gain, building_quality):
        self.chunk = chunk
        self.food_gain = food_gain
        self.building_quality = building_quality

    def delta(self):
        self.chunk.owned_by.food += self.food_gain + random.random() * self.food_gain * 0.3