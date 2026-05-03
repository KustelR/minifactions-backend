from uuid import UUID


class Igrok:
    id: UUID | None = None
    stamina: int = 0
    military: int = 0
    building: int = 0
    tech: int = 0
    psychology: int = 0


    def __init__(self, military, building, tech, psychology, stamina):
        self.military = military
        self.building = building
        self.psychology = psychology
        self.tech = tech
        self.stamina = stamina


    def delta(self):
        pass