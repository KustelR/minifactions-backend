from uuid import UUID, uuid4
from typing import Callable


class Faction:
    name = None
    id: UUID | None = None
    igroks: list[Igrok] = []
    chunks: list[Chunk] = []
    emeralds = 0
    building_materials = 0.0
    food = 0.0
    raw_materials = 0.0
    weapons = 0.0

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

    def to_dict(self):
        return {
            "name": self.name,
            "id": str(self.id),
            "igroks": list(map(lambda igrok: igrok.to_dict(), self.igroks)),
            "resources": {
                "emeralds": self.emeralds,
                "building_materials": self.building_materials,
                "raw_materials": self.raw_materials,
                "weapons": self.weapons,
                "food": self.food
            },
            "chunks": list(map(lambda chunk: chunk.pos, self.chunks))
        }


class Igrok:
    id: UUID | None = None
    faction: Faction | None = None
    stamina: int = 0
    military: int = 0
    building: int = 0
    tech: int = 0
    psychology: int = 0

    task: Task | None = None

    def assign(self, task: Task):
        if (self.task):
            self.task.interrupt();
        self.task = task


    def __init__(self, military: int, building: int, tech: int, psychology: int, stamina: int):
        self.military = military
        self.building = building
        self.psychology = psychology
        self.tech = tech
        self.stamina = stamina


    def delta(self):
        if self.task:
            self.task.delta()

    def to_dict(self):
        return {
            "id": str(self.id),
            "faction": str(self.faction.id),
            "stats": {
                "stamina": self.stamina,
                "building": self.building,
                "military": self.military,
                "psychology": self.psychology,
                "tech": self.tech,
                "task": self.task.to_dict() if self.task else None
            }
        }


class Chunk:
    owned_by: Faction | None = None
    building: Building | None = None
    terrain_type: str | None  = None
    pos: tuple[int]
    affected_by: list[Task]

    def __init__(self, pos: int | int):
        self.terrain_type = "plains"
        self.pos = pos
        self.affected_by = []

    def delta(self):
        if self.building: self.building.delta();

    def to_dict(self) -> dict:
        return {
            "owned_by": str(self.owned_by.id) if self.owned_by else None,
            "terrain_type": self.terrain_type,
            "pos": self.pos,
            "building": self.building.to_dict() if self.building else None,
            "affected_by": list(map(lambda task: task.to_dict(), self.affected_by))
        }

class Task:
    name: str
    id: UUID
    igrok: Igrok
    chunk: Chunk
    faction: Faction
    duration: int
    started = False
    start_invoke: Callable
    performing_invoke: Callable
    interrupt_invoke: Callable
    end_invoke: Callable

    def __init__(self, 
                 name: str,
                 igrok: Igrok, 
                 chunk: Chunk, 
                 faction: Faction, 
                 duration: int,
                 start_invoke: Callable,
                 performing_invoke: Callable, 
                 interrupt_invoke: Callable,
                 end_invoke: Callable):
        self.name = name
        self.id = uuid4()
        self.igrok = igrok
        self.chunk = chunk
        self.faction = faction
        self.duration = duration
        self.start_invoke = start_invoke
        self.performing_invoke = performing_invoke
        self.interrupt_invoke = interrupt_invoke
        self.end_invoke = end_invoke



    def clear(self):
        ids = list(map(lambda affecting: affecting.id, self.chunk.affected_by))
        index = ids.index(self.id)
        self.chunk.affected_by.pop(index)
        self.igrok.task = None

    def interrupt(self):
        if self.interrupt_invoke: self.interrupt_invoke(self)
        self.clear()

    def delta(self):
        if not self.started:
            self.started = True
            self.chunk.affected_by.append(self)
            if self.start_invoke:
                self.start_invoke(self)


        if self.duration > 0 and self.performing_invoke:
            self.duration -=1
            self.performing_invoke(self)
        else:
            if (self.end_invoke):
                self.end_invoke(self)
            self.clear()


    def to_dict(self):
        return {
            "name": self.name,
            "id": str(self.id),
            "igrok": str(self.igrok.id),
            "chunk": self.chunk.pos,
            "faction": str(self.faction.id),
            "duration": self.duration
        }


class Building:
    name: str
    chunk: Chunk
    defense: int

    def __init__(self, name, chunk: Chunk, defense: int):
        self.name = name
        self.chunk = chunk
        self.defense = defense

    def delta(self):
        pass

    def to_dict(self):
        return {"message": "YA SHOULDN'T SEE THIS. RUN."}