import random

from Entities import Chunk, Faction, Igrok, Task


class StoredTask:
    name: str
    start_invoke: callable[Task] | None = None
    during_invoke: callable[Task] | None = None
    end_invoke: callable[Task] | None = None
    duration: int | None
    def __init__(self, name: str, 
                 start_invoke: callable[Task] | None = None, 
                 during_invoke: callable[Task] | None = None, 
                 end_invoke: callable[Task] | None = None,
                 duration: int | None = None):
        self.name = name
        self.start_invoke = start_invoke
        self.during_invoke = during_invoke
        self.end_invoke = end_invoke
        self.duration = duration

    def task(self, igrok: Igrok, chunk: Chunk, faction: Faction, duration: int | None = None):
        return Task(
            self.name, 
            igrok,
            chunk,
            faction,
            self.duration if self.duration else duration if duration else 1,
            self.start_invoke,
            self.during_invoke,
            self.end_invoke)


def during_foraging(task: Task):
    task.faction.raw_materials += (task.igrok.tech + task.igrok.stamina * 0.2) * (0.2 + random.random() * 0.2)
    task.faction.building_materials += (task.igrok.building + task.igrok.stamina * 0.2) * (0.7 + random.random() * 0.6)
    task.faction.food += (task.igrok.tech * 0.5 + task.igrok.stamina * 0.3) * (0.3 + random.random() * 0.3)
    task.igrok.stamina -= 1.5 / task.igrok.tech + random.random() * 0.1

def during_mining(task: Task):
    task.faction.emeralds += max(0, random.randint(0, 100) - 95)
    task.faction.raw_materials += (task.igrok.tech + task.igrok.stamina * 0.2) * (2 + random.random())
    task.faction.building_materials += (task.igrok.building + task.igrok.stamina * 0.2) * (0.2 + random.random() * 0.6)

    if task.chunk.terrain_type == "mountain":
        task.faction.raw_materials += 10
        task.faction.emeralds + 5


foraging = StoredTask(
    "foraging",
    during_invoke=during_foraging
)

mining = StoredTask(
    "mining",
    during_invoke=during_mining
)

def get_tasks():
    result = {
        foraging.name: foraging,
        mining.name: mining
    }

    return result
