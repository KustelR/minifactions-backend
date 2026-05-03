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

class Task:
    igrok: Igrok
    chunk: Chunk | None
    faction: Faction
    duration: int
    started = False
    start_invoke: Callable
    performing_invoke: Callable
    end_invoke: Callable

    def __init__(self, 
                 igrok: Igrok, 
                 chunk: Chunk, 
                 faction: Faction, 
                 duration: int,
                 start_invoke: Callable,
                 performing_invoke: Callable, 
                 end_invoke: Callable):
        self.igrok = igrok
        self.chunk = chunk
        self.faction = faction
        self.duration = duration
        self.start_invoke = start_invoke
        self.performing_invoke = performing_invoke
        self.end_invoke = end_invoke

    def delta(self):
        if not self.started:
            self.started = True
            self.start_invoke(self)
        if self.duration > 0:
            self.duration -=1
            self.performing_invoke(self)
        else:
            self.end_invoke(self)

    def to_dict(self) -> dict:
        return {
            "igrok": str(self.igrok.id),
            "chunk": self.chunk.pos,
            "faction": str(self.faction.id),
            "duration": self.duration
        }

