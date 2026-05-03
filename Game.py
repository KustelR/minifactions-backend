import json

from Grid import Grid
from Entities import Faction, Igrok
from uuid import uuid4, UUID



class Game:
    grid: Grid = None
    factions: dict[UUID, Faction] = {}
    igroks: dict[UUID, Igrok] = {}

    def register_faction(self, faction: Faction) -> UUID:
        if faction.id != None: return faction.id
        id = uuid4()
        faction.id = id
        self.factions[id] = faction


    def unregister_faction(self, faction: Faction):
        if faction.id == None:return
        self.factions.pop(faction.id)
        faction.kill()
        faction.id = None

    def register_igrok(self, igrok: Igrok) -> UUID:
        if igrok.id != None: return igrok.id
        id = uuid4()
        igrok.id = id
        self.igroks[id] = igrok

    def unregister_igrok(self, igrok: Igrok):
        if igrok.id == None:return
        self.igroks.pop(igrok.id)
        igrok.id = None

    def create_faction(self, name: str) -> Faction:
        faction = Faction(name)
        self.register_faction(faction)
        return faction

    def create_igrok(self, m, b, t, p, s) -> Igrok:
        igrok = Igrok(m, b, t, p, s)
        self.register_igrok(igrok)
        return igrok

    def turn(self):
        self.grid.delta()
        for faction in self.factions.values(): faction.delta()
        for igrok in self.igroks.values(): igrok.delta()


    def __init__(self, gridHeight: int, gridWitdht: int):
        self.grid = Grid(gridHeight, gridWitdht)

    def toJSON(self):
        return {
            "grid": list(self.grid),
            "factions": list(map(lambda faction: faction.to_dict(), self.factions.values())),
        }