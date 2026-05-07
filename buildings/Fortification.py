from Entities import Building, Chunk


class Fortification(Building):
    name = "fort"
    defense = 0
    building_quality = 0


    def __init__(self, chunk: Chunk, defense: float, building_quality: float):
        self.chunk = chunk
        self.defense = defense
        self.building_quality =  building_quality

    def delta(self):
        pass

    def to_dict(self):
        return {
            "name": "fort",
            "defense": self.defense,
            "building_quality": self.building_quality
        }
