from uuid import UUID


class Faction:
    name = None
    id: UUID | None = None
    igroks = []
    chunks = []
    emeralds = 0
    building_materials = 0
    food = 0
    raw_materias = 0
    weapons = 0

    def __init__(self, name: str):
        self.name = name
    
    def claim(self, chunk: Chunk):
        chunk.owned_by = self
        self.chunks.append(chunk)

    def add_igrok(self, igrok: Igrok):
        self.igroks.append(igrok)
        igrok.faction = self

    def clear_chunks(self):
        for chunk in self.chunks: chunk.owned_by = None

    def kill(self):
        self.clear_chunks()

    def delta(self):
        pass


class Igrok:
    id: UUID | None = None
    faction: Faction | None = None
    stamina: int = 0
    military: int = 0
    building: int = 0
    tech: int = 0
    psychology: int = 0


    def __init__(self, military: int, building: int, tech: int, psychology: int, stamina: int):
        self.military = military
        self.building = building
        self.psychology = psychology
        self.tech = tech
        self.stamina = stamina


    def delta(self):
        pass


class Chunk:
    owned_by = None
    terrain_type = None


    def __init__(self):
        self.terrain_type = "plains"


    def delta(self):
        pass


