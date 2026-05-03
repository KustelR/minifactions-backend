from Grid import Chunk
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

    def delta(self):
        pass