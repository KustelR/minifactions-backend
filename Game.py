from Grid import Grid
from Faction import Faction
from uuid import uuid4, UUID
from Igrok import Igrok



class Game:
    grid: Grid = None
    factions: dict[UUID, Faction] = {}
    igroks: dict[UUID, Igrok] = {}

    def register_faction(self, faction: Faction) -> UUID:
        id = uuid4()
        faction.id = id
        self.factions[id] = faction


    def unregister_faction(self, faction: Faction):
        self.factions.clear(faction.id)

    def register_igrok(self, igrok: Igrok) -> UUID:
        id = uuid4()
        igrok.id = id
        self.igroks[id] = igrok

    def unregister_igrok(self, igrok: Igrok):
        self.factions.clear(igrok.id)

    def turn(self):
        self.grid.delta()
        for faction in self.factions: faction.delta()
        for igrok in self.igroks: igrok.delta()


    def __init__(self, gridHeight: int, gridWitdht: int):
        self.grid = Grid(gridHeight, gridWitdht)